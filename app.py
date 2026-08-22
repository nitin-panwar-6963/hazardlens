import streamlit as st
import cv2
import base64
import numpy as np
from ultralytics import YOLO
from datetime import datetime
import edge_tts
import asyncio
import os
# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="HazardLens | Command Center",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🛡️"
)

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL CSS — Tactical Command-Center Aesthetic
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Inter:wght@300;400;500&family=Share+Tech+Mono&display=swap');

:root {
  --bg:     #050A0F;
  --surf:   #091420;
  --card:   #0C1B28;
  --cyan:   #00E5FF;
  --red:    #FF3A3A;
  --amber:  #FFB800;
  --green:  #39FF14;
  --border: #14253A;
  --text:   #DCE8F0;
  --muted:  #4A6880;
  --label:  #7899B8;
  --d: 'Rajdhani', sans-serif;
  --b: 'Inter', sans-serif;
  --m: 'Share Tech Mono', monospace;
}

/* ── BASE ── */
.stApp, .main  { background: var(--bg) !important; }
#MainMenu, footer { visibility: hidden !important; }
*, *::before, *::after { box-sizing: border-box; }
div.block-container { padding-top: 1rem !important; padding-bottom: 1rem !important; }

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
  background: #03090F !important;
  border-right: 1px solid var(--border) !important;
}

/* ── HEADER ── */
.hz-hdr {
  background: linear-gradient(112deg, #070F18 0%, #0B1928 100%);
  border: 1px solid var(--border);
  border-left: 4px solid var(--cyan);
  border-radius: 6px;
  padding: 18px 24px;
  margin-bottom: 10px;
  display: flex; align-items: center; justify-content: space-between;
  position: relative; overflow: hidden;
}
.hz-hdr::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent 0%, rgba(0,229,255,.45) 50%, transparent 100%);
}
.hz-brand {
  font-family: var(--d);
  font-size: 2rem; font-weight: 700;
  color: var(--text); letter-spacing: 5px; line-height: 1;
  text-transform: uppercase;
}
.hz-brand em { color: var(--cyan); font-style: normal; }
.hz-sub { font-family: var(--m); font-size: 0.6rem; color: var(--muted); letter-spacing: 4px; margin-top: 5px; }
.hz-right { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; justify-content: flex-end; }

.stat-pill {
  background: #03080E; border: 1px solid var(--border);
  border-radius: 4px; padding: 7px 14px; text-align: center; min-width: 72px;
}
.stat-v { display: block; font-family: var(--m); font-size: 1.1rem; color: var(--cyan); line-height: 1.2; }
.stat-l { font-family: var(--b); font-size: 0.5rem; color: var(--muted); letter-spacing: 2.5px; text-transform: uppercase; }

.arm-on  {
  display: inline-flex; align-items: center; gap: 9px;
  background: #040F04; border: 1px solid var(--green); border-radius: 4px;
  padding: 9px 18px; font-family: var(--d); font-size: 0.85rem;
  font-weight: 700; color: var(--green); letter-spacing: 3px; text-transform: uppercase;
}
.arm-off {
  display: inline-flex; align-items: center; gap: 9px;
  background: #100F04; border: 1px solid #1E1E08; border-radius: 4px;
  padding: 9px 18px; font-family: var(--d); font-size: 0.85rem;
  font-weight: 700; color: #36361A; letter-spacing: 3px; text-transform: uppercase;
}

/* PULSING DOTS */
@keyframes blink { 0%,100%{opacity:1;} 50%{opacity:.08;} }
@keyframes blink-fast { 0%,100%{opacity:1;} 50%{opacity:.1;} }
.dot { width:9px; height:9px; border-radius:50%; display:inline-block; flex-shrink:0; animation: blink 1.3s ease-in-out infinite; }
.dot-g { background: var(--green); box-shadow: 0 0 7px var(--green); }
.dot-a { background: var(--amber); box-shadow: 0 0 7px var(--amber); }
.dot-r { background: var(--red);   box-shadow: 0 0 7px var(--red);   animation: blink-fast .7s ease-in-out infinite; }

/* ── ALERT BANNERS ── */
@keyframes si   { from{transform:translateY(-8px);opacity:0;} to{transform:translateY(0);opacity:1;} }
@keyframes f-r  { 0%,100%{border-color:var(--red);  box-shadow:0 0 16px rgba(255,58,58,.18);}  50%{box-shadow:0 0 34px rgba(255,58,58,.38);  border-color:rgba(255,58,58,.55);} }
@keyframes f-a  { 0%,100%{border-color:var(--amber);box-shadow:0 0 16px rgba(255,184,0,.18);} 50%{box-shadow:0 0 34px rgba(255,184,0,.38); border-color:rgba(255,184,0,.55);} }

.a-fire {
  background: linear-gradient(135deg, #140303, #1B0505);
  border: 1px solid var(--red); border-radius: 5px;
  padding: 14px 18px; display: flex; align-items: center; gap: 14px; margin: 6px 0;
  animation: si .3s ease, f-r 1.5s ease-in-out infinite;
}
.a-crwd {
  background: linear-gradient(135deg, #130D00, #191100);
  border: 1px solid var(--amber); border-radius: 5px;
  padding: 14px 18px; display: flex; align-items: center; gap: 14px; margin: 6px 0;
  animation: si .3s ease, f-a 1.5s ease-in-out infinite;
}
.a-ico  { font-size: 1.8rem; flex-shrink: 0; }
.a-ttl  { font-family: var(--d); font-size: 1rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; }
.a-msg  { font-family: var(--b); font-size: 0.72rem; margin-top: 2px; opacity: .85; }
.a-fire .a-ttl { color: var(--red);   } .a-fire .a-msg { color: #FFA5A5; }
.a-crwd .a-ttl { color: var(--amber); } .a-crwd .a-msg { color: #FFD888; }

/* ── SECTION DIVIDER ── */
.sdiv { display: flex; align-items: center; gap: 12px; margin: 10px 0 8px; }
.sdiv::before,.sdiv::after { content: ''; flex: 1; height: 1px; background: var(--border); }
.sdiv-t { font-family: var(--m); font-size: 0.57rem; color: var(--muted); letter-spacing: 3px; white-space: nowrap; text-transform: uppercase; }

/* ── CAMERA CARD HEADER ── */
.cam-hdr {
  background: #04090F;
  border: 1px solid var(--border); border-bottom: none;
  border-radius: 5px 5px 0 0;
  padding: 10px 14px; margin-bottom: 0;
  display: flex; align-items: center; justify-content: space-between;
}
.cam-hdr.live { border-color: var(--cyan); }
.cam-nm  { font-family: var(--d); font-size: 0.85rem; font-weight: 600; color: var(--text); letter-spacing: 1.5px; text-transform: uppercase; }
.cam-loc { font-family: var(--m); font-size: 0.57rem; color: var(--muted); letter-spacing: 1.5px; margin-top: 2px; }

.badge-live  { display: inline-flex; align-items: center; gap: 5px; background: #090404; border: 1px solid #9A0000; border-radius: 3px; padding: 3px 9px; font-family: var(--m); font-size: 0.57rem; color: #FF5555; letter-spacing: 1px; }
.badge-stdby { display: inline-flex; align-items: center; gap: 5px; background: #0A0A0A; border: 1px solid #182030; border-radius: 3px; padding: 3px 9px; font-family: var(--m); font-size: 0.57rem; color: var(--muted); letter-spacing: 1px; }

/* ── METRIC STRIP ── */
.mstrip {
  background: #03080D; border: 1px solid var(--border); border-top: none; border-bottom: none;
  padding: 7px 14px; display: flex; align-items: center; justify-content: space-between;
}
.mstrip .ml { font-family: var(--m); font-size: 0.57rem; color: var(--muted); letter-spacing: 2px; text-transform: uppercase; }
.mstrip .mv { font-family: var(--m); font-size: 0.88rem; color: var(--cyan); font-weight: bold; }
.mstrip .mv.off { color: var(--muted); }

/* ── IMAGE — connects to card header and metric strip ── */
div[data-testid="stImage"] { margin: 0 !important; padding: 0 !important; position: relative; }
div[data-testid="stImage"] img {
  display: block; width: 100%;
  border: 1px solid var(--border); border-top: none; border-radius: 0;
}

/* ── CRT Scanline Overlay ── */
div[data-testid="stImage"]::after {
  content: '';
  position: absolute; inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent, transparent 2px,
    rgba(0, 229, 255, 0.013) 2px, rgba(0, 229, 255, 0.013) 4px
  );
  pointer-events: none; z-index: 5;
}

/* ── BUTTONS ── */
div[data-testid="stButton"] > button {
  font-family: var(--d) !important;
  font-size: 0.7rem !important; font-weight: 600 !important;
  letter-spacing: 1.5px !important; text-transform: uppercase !important;
  border-radius: 0 0 4px 4px !important;
  border: 1px solid var(--border) !important; border-top: none !important;
  width: 100% !important;
  background: #030810 !important; color: var(--label) !important;
  padding: 9px 12px !important; transition: all .2s ease !important;
}
div[data-testid="stButton"] > button:hover {
  background: #07131E !important; color: var(--cyan) !important;
  border-color: var(--cyan) !important;
}

/* ── TEXT INPUT ── */
div[data-testid="stTextInput"] input {
  background: #03080D !important; border: 1px solid var(--border) !important;
  color: var(--cyan) !important; font-family: var(--m) !important;
  font-size: 0.77rem !important; letter-spacing: 1px !important; border-radius: 3px !important;
}
div[data-testid="stTextInput"] input:focus {
  border-color: var(--cyan) !important; box-shadow: 0 0 0 1px rgba(0,229,255,.28) !important;
}
div[data-testid="stTextInput"] label {
  font-family: var(--m) !important; font-size: 0.57rem !important;
  color: var(--muted) !important; letter-spacing: 3px !important; text-transform: uppercase !important;
}

/* ── SIDEBAR COMPONENTS ── */
.sb-title { font-family: var(--d); font-size: 1.1rem; font-weight: 700; color: var(--cyan); letter-spacing: 4px; padding-bottom: 12px; margin-bottom: 12px; border-bottom: 1px solid var(--border); text-transform: uppercase; }
.sb-lbl   { font-family: var(--m); font-size: 0.55rem; color: var(--muted); letter-spacing: 3px; text-transform: uppercase; padding: 12px 0 7px; }
.sb-row   { display: flex; justify-content: space-between; align-items: center; padding: 7px 10px; margin: 3px 0; background: #060C14; border: 1px solid var(--border); border-radius: 3px; }
.sb-rn    { font-family: var(--d); font-size: 0.78rem; font-weight: 600; color: var(--label); }
.sb-rloc  { font-family: var(--m); font-size: 0.55rem; color: var(--muted); letter-spacing: 1px; margin-top: 1px; }
.sb-rs    { font-family: var(--m); font-size: 0.57rem; }
.sysinfo  { font-family: var(--m); font-size: 0.62rem; color: var(--muted); line-height: 2.1; padding: 10px 12px; background: #060C14; border: 1px solid var(--border); border-radius: 3px; }

/* ── FOOTER STATUS BAR ── */
.ftr {
  background: #03080D; border: 1px solid var(--border); border-top-color: var(--cyan);
  border-radius: 4px; padding: 8px 18px; margin-top: 16px;
  display: flex; justify-content: space-between; align-items: center;
  font-family: var(--m); font-size: 0.57rem; color: var(--muted); letter-spacing: 1px;
  flex-wrap: wrap; gap: 6px;
}
.ftr .online { color: var(--green); }

/* ── TOAST ── */
div[data-testid="stToast"] {
  background: #041004 !important; border: 1px solid var(--green) !important;
  color: var(--green) !important; font-family: var(--b) !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }

section[data-testid="stSidebar"] div[data-testid="stButton"] > button {
  border-radius: 3px !important;
  border: 1px solid var(--border) !important;
  border-top: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
  border-color: var(--cyan) !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# STATE MANAGEMENT
# ─────────────────────────────────────────────────────────────────────────────
if 'alert_sent'       not in st.session_state: st.session_state.alert_sent       = False
if 'crowd_alert_sent' not in st.session_state: st.session_state.crowd_alert_sent = False
if 'audio_loop'       not in st.session_state: st.session_state.audio_loop       = False
if 'system_armed'     not in st.session_state: st.session_state.system_armed     = False
if 'do_clear_alert'   not in st.session_state: st.session_state.do_clear_alert   = False

# ─────────────────────────────────────────────────────────────────────────────
# MODEL LOADING  (cached for zero-lag reloads)
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_resource
def load_twin_models():
    fire_mod = YOLO('best.pt')      # Custom Fire / Smoke model
    base_mod = YOLO('yolov8n.pt')   # Standard model for crowd counting
    return fire_mod, base_mod

fire_model, base_model = load_twin_models()

# ─────────────────────────────────────────────────────────────────────────────
# CALLBACKS
# ─────────────────────────────────────────────────────────────────────────────
def dummy_silence(cam_name):
    st.toast(f"ℹ️ {cam_name} is on STANDBY — no active alerts to silence.")

def silence_alerts():
    st.session_state.audio_loop       = False
    st.session_state.alert_sent       = False
    st.session_state.crowd_alert_sent = False
    st.session_state.do_clear_alert   = True

def disarm_system():
    st.session_state.system_armed   = False
    st.session_state.do_clear_alert = True

def arm_system():
    st.session_state.system_armed = True

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def create_placeholder(cam_name, status="STANDBY"):
    """Tactical-style placeholder with reticle, grid, and corner brackets."""
    h, w = 360, 640
    img = np.zeros((h, w, 3), dtype=np.uint8) + 10

    for x in range(0, w, 64):
        cv2.line(img, (x, 0), (x, h), (15, 28, 42), 1)
    for y in range(0, h, 64):
        cv2.line(img, (0, y), (w, y), (15, 28, 42), 1)

    cx, cy = w // 2, h // 2
    cv2.line(img, (cx - 50, cy), (cx - 12, cy), (26, 50, 68), 1)
    cv2.line(img, (cx + 12, cy), (cx + 50, cy), (26, 50, 68), 1)
    cv2.line(img, (cx, cy - 40), (cx, cy - 12), (26, 50, 68), 1)
    cv2.line(img, (cx, cy + 12), (cx, cy + 40), (26, 50, 68), 1)
    cv2.circle(img, (cx, cy), 20, (26, 50, 68), 1)
    cv2.circle(img, (cx, cy), 55, (18, 34, 50), 1)
    cv2.circle(img, (cx, cy), 3, (28, 54, 72), -1)

    bs = 20
    corners = [(40, 30, 1, 1), (w - 40, 30, -1, 1),
               (40, h - 30, 1, -1), (w - 40, h - 30, -1, -1)]
    for bx, by, dx, dy in corners:
        cv2.line(img, (bx, by), (bx + bs * dx, by), (26, 50, 68), 1)
        cv2.line(img, (bx, by), (bx, by + bs * dy), (26, 50, 68), 1)

    lw = cv2.getTextSize(cam_name, cv2.FONT_HERSHEY_SIMPLEX, 0.44, 1)[0][0]
    cv2.putText(img, cam_name, (cx - lw // 2, cy - 14),
                cv2.FONT_HERSHEY_SIMPLEX, 0.44, (36, 68, 88), 1)
    sw = cv2.getTextSize(f"[ {status} ]", cv2.FONT_HERSHEY_SIMPLEX, 0.38, 1)[0][0]
    cv2.putText(img, f"[ {status} ]", (cx - sw // 2, cy + 76),
                cv2.FONT_HERSHEY_SIMPLEX, 0.38, (22, 44, 60), 1)

    return img

# ─────────────────────────────────────────────────────────────────────────────
# ─── EDGE-TTS HINDI NEURAL VOICE (LIFETIME FREE) ───
# ('hi-IN-SwaraNeural')
# ─────────────────────────────────────────────────────────────────────────────
def trigger_hindi_alert(text, filename="alert.mp3"):
    async def _generate():
        # for Female = "hi-IN-SwaraNeural" | for Male = "hi-IN-MadhurNeural"
        communicate = edge_tts.Communicate(text, "hi-IN-SwaraNeural")
        await communicate.save("temp_alert.mp3")

    try:
        asyncio.run(_generate())

        with open("temp_alert.mp3", "rb") as f:
            audio_b64 = base64.b64encode(f.read()).decode()

        audio_pos.markdown(
            f'<audio id="alarm-audio" autoplay loop>'
            f'<source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3"></audio>',
            unsafe_allow_html=True
        )
        st.session_state.audio_loop = True
    except Exception:
        pass

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR — Control Panel
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sb-title">⬡ Control Panel</div>', unsafe_allow_html=True)

    st.markdown('<div class="sb-lbl">▸ Feed Source</div>', unsafe_allow_html=True)
    ip_url = st.text_input(
        "IP Camera Stream URL",
        "http://10.60.88.135:8080/video",
        label_visibility="collapsed"
    )

    st.markdown('<div class="sb-lbl">▸ System Control</div>', unsafe_allow_html=True)
    ca, cb = st.columns(2)
    with ca:
        st.button("🔴 ARM",    on_click=arm_system,    use_container_width=True)
    with cb:
        st.button("⬛ DISARM", on_click=disarm_system, use_container_width=True)

    st.markdown('<div class="sb-lbl">▸ Camera Status</div>', unsafe_allow_html=True)
    armed_now = st.session_state.system_armed
    cam_registry = [
        ("CAM 01", "MIET COLLEGE MAIN GATE",        True),
        ("CAM 02", "RAILWAY STATION ENTRANCE",  False),
        ("CAM 03", "METRO STATION ENTRANCE",         False),
        ("CAM 04", "Server Room Backend",   False),
    ]
    for cn, loc, active in cam_registry:
        is_live  = active and armed_now
        s_text   = "LIVE"  if is_live else "STDBY"
        s_color  = "var(--green)" if is_live else "var(--muted)"
        dot_html = (
            '<span class="dot dot-r" style="width:6px;height:6px;"></span> '
            if is_live else "● "
        )
        st.markdown(f"""
        <div class="sb-row">
          <div>
            <div class="sb-rn">{cn}</div>
            <div class="sb-rloc">{loc}</div>
          </div>
          <span class="sb-rs" style="color:{s_color};">{dot_html}{s_text}</span>
        </div>""", unsafe_allow_html=True)

    # ─── UPDATED:  EDGE-TTS ───
    st.markdown('<div class="sb-lbl">▸ System Info</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sysinfo">
    LOCATION &nbsp;&nbsp; : MIET CAMPUS<br>
    AI ENGINES : TWIN (FIRE + CROWD)<br>
    TTS ENGINE : EDGE-TTS (HINDI NEURAL)<br>
    LANGUAGE &nbsp;&nbsp; : HI-IN<br>
    FRAME SKIP : 4 FRAMES<br>
    CROWD LIM &nbsp;: 10 PERSONS<br>
    </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# MASTER HEADER
# ─────────────────────────────────────────────────────────────────────────────
armed = st.session_state.system_armed
arm_cls  = "arm-on"  if armed else "arm-off"
dot_cls  = "dot-g"   if armed else "dot-a"
arm_txt  = "ARMED"   if armed else "STANDBY"

st.markdown(f"""
<div class="hz-hdr">
  <div>
    <div class="hz-brand">⬡ HAZARD<em>LENS</em></div>
    <div class="hz-sub">AI-POWERED SMART CITY SURVEILLANCE COMMAND</div>
  </div>
  <div class="hz-right">
    <div class="stat-pill">
      <span class="stat-v">04</span>
      <span class="stat-l">Cameras</span>
    </div>
    <div class="{arm_cls}">
      <span class="dot {dot_cls}"></span>{arm_txt}
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL ALERT & AUDIO PLACEHOLDERS
# ─────────────────────────────────────────────────────────────────────────────
alert_pos = st.empty()
audio_pos = st.empty()

if st.session_state.do_clear_alert:
    alert_pos.empty()
    audio_pos.empty()
    st.session_state.alert_sent       = False
    st.session_state.crowd_alert_sent = False
    st.session_state.do_clear_alert   = False

# ─────────────────────────────────────────────────────────────────────────────
# CAMERA GRID
# ─────────────────────────────────────────────────────────────────────────────
st.markdown('<div class="sdiv"><span class="sdiv-t">Active Monitoring Grid</span></div>',
            unsafe_allow_html=True)

live_badge = '<span class="badge-live"><span class="dot dot-r" style="width:6px;height:6px;"></span>LIVE</span>'
stdby_badge = '<span class="badge-stdby">● STDBY</span>'

col1, col2 = st.columns(2)

metric_cpu    = None
feed_01_frame = None

with col1:
    hdr_cls = "cam-hdr live" if armed else "cam-hdr"
    badge1  = live_badge if armed else stdby_badge
    st.markdown(f"""
    <div class="{hdr_cls}">
      <div>
        <div class="cam-nm">📹 CAM 01</div>
        <div class="cam-loc">MIET COLLEGE MAIN GATE · AI-MONITORED</div>
      </div>
      {badge1}
    </div>""", unsafe_allow_html=True)

    metric_cpu = st.empty()
    metric_cpu.markdown(
        '<div class="mstrip"><span class="ml">Crowd Count</span>'
        '<span class="mv off">—</span></div>',
        unsafe_allow_html=True
    )

    feed_01_frame = st.empty()
    feed_01_frame.image(create_placeholder("CAM 01"), use_container_width=True)

    st.button("🔕 SILENCE CAM 01", key="silence_1",
              on_click=silence_alerts, use_container_width=True)

with col2:
    st.markdown(f"""
    <div class="cam-hdr">
      <div>
        <div class="cam-nm">📷 CAM 02</div>
        <div class="cam-loc">RAILWAY STATION ENTRANCE · STANDBY</div>
      </div>
      {stdby_badge}
    </div>""", unsafe_allow_html=True)
    st.markdown(
        '<div class="mstrip"><span class="ml">Crowd Count</span>'
        '<span class="mv off">—</span></div>', unsafe_allow_html=True)
    st.image(create_placeholder("CAM 02"), use_container_width=True)
    st.button("🔕 SILENCE CAM 02", key="silence_2",
              on_click=dummy_silence, args=("CAM 02",), use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown(f"""
    <div class="cam-hdr">
      <div>
        <div class="cam-nm">📷 CAM 03</div>
        <div class="cam-loc">METRO STATION ENTRANCE · STANDBY</div>
      </div>
      {stdby_badge}
    </div>""", unsafe_allow_html=True)
    st.markdown(
        '<div class="mstrip"><span class="ml">Crowd Count</span>'
        '<span class="mv off">—</span></div>', unsafe_allow_html=True)
    st.image(create_placeholder("CAM 03"), use_container_width=True)
    st.button("🔕 SILENCE CAM 03", key="silence_3",
              on_click=dummy_silence, args=("CAM 03",), use_container_width=True)

with col4:
    st.markdown(f"""
    <div class="cam-hdr">
      <div>
        <div class="cam-nm">📷 CAM 04</div>
        <div class="cam-loc">SERVER ROOM BACKEND · STANDBY</div>
      </div>
      {stdby_badge}
    </div>""", unsafe_allow_html=True)
    st.markdown(
        '<div class="mstrip"><span class="ml">Crowd Count</span>'
        '<span class="mv off">—</span></div>', unsafe_allow_html=True)
    st.image(create_placeholder("CAM 04"), use_container_width=True)
    st.button("🔕 SILENCE CAM 04", key="silence_4",
              on_click=dummy_silence, args=("CAM 04",), use_container_width=True)

# ─────────────────────────────────────────────────────────────────────────────
# FOOTER STATUS BAR
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ftr">
  <span>⬡ HAZARDLENS COMMAND v2.0 · MIET CAMPUS, MEERUT</span>
  <span><span class="online">●</span> TWIN AI ONLINE · EDGE-TTS ENABLED</span>
  <span id="ftr-dt">—</span>
</div>
<script>
(function(){{
  var el = document.getElementById('ftr-dt');
  if(el) el.textContent = new Date().toLocaleDateString('en-IN',
    {{weekday:'short', year:'numeric', month:'short', day:'numeric'}});
}})();
</script>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# LIVE LOGIC LOOP
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.system_armed:
    cap = cv2.VideoCapture(ip_url)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    count      = 0
    frame_skip = 4
    CROWD_THRESHOLD = 10  # Threshold yahan upar cleanly define kar diya

    while cap.isOpened() and st.session_state.system_armed:
        ret, frame = cap.read()
        if not ret:
            break

        count += 1

        if count % frame_skip == 0:
            # Engine 1: Custom Fire / Smoke model
            fire_results    = fire_model(frame, conf=0.68)
            annotated_frame = fire_results[0].plot()
            annotated_rgb   = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

            # REAL-TIME CCTV TIMESTAMP
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cctv_text = f"REC | CAM 01 | {now}"

            cv2.putText(annotated_rgb, cctv_text, (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 0), 4, cv2.LINE_AA)
            cv2.putText(annotated_rgb, cctv_text, (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 255), 2, cv2.LINE_AA)

            # Engine 2: Base model for crowd counting
            base_results = base_model(frame)
            person_count = sum(
                1 for box in base_results[0].boxes
                if base_model.names[int(box.cls[0])] == 'person'
            )

            # Update metric strip
            if metric_cpu is not None:
                metric_cpu.markdown(
                    f'<div class="mstrip">'
                    f'<span class="ml">Crowd Count</span>'
                    f'<span class="mv">👥 {person_count}</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )

            # Update live camera feed
            if feed_01_frame is not None:
                feed_01_frame.image(annotated_rgb, channels="RGB", use_container_width=True)

            # ── HAZARD DETECTION LOGIC ──
            # Handles both Chinese ('火', '烟') and English ('fire', 'smoke') labels
            fire_spotted = any(
                fire_model.names[int(b.cls[0])].lower() in ('fire', 'smoke', '火', '烟')
                for b in fire_results[0].boxes
            )

            # ── 1. FIRE / SMOKE ALERT (Top Priority) ──
            if fire_spotted:
                if st.session_state.get("active_alert") != "FIRE":
                    alert_pos.markdown("""
                    <div class="a-fire">
                      <span class="a-ico">🔥</span>
                      <div>
                        <div class="a-ttl">Fire / Smoke Hazard Detected — CAM 01</div>
                        <div class="a-msg">MIET Main Gate · High-confidence AI detection · Fire Safety Team Dispatched</div>
                      </div>
                    </div>""", unsafe_allow_html=True)

                    trigger_hindi_alert(
                        "कृपया ध्यान दें। मेन गेट पर आग डिटेक्ट हुई है। तुरंत फायर सेफ्टी टीम डिस्पैच करें।",
                        filename="fire_alert.mp3"
                    )
                    st.session_state.active_alert = "FIRE"

            # ── 2. OVERCROWDING ALERT (Latest Override) ──
            elif person_count > CROWD_THRESHOLD:
                if st.session_state.get("active_alert") != "CROWD":
                    alert_pos.markdown(f"""
                    <div class="a-crwd">
                      <span class="a-ico">🚨</span>
                      <div>
                        <div class="a-ttl">Overcrowding Detected — CAM 01</div>
                        <div class="a-msg">MIET Main Gate · Live Count: {person_count} persons · Security Team Dispatch Triggered</div>
                      </div>
                    </div>""", unsafe_allow_html=True)

                    trigger_hindi_alert(
                        "कृपया ध्यान दें। मेन गेट एंट्रेंस पर ओवरक्राउडिंग डिटेक्ट हुई है। तुरंत सिक्योरिटी स्टाफ डिस्पैच करें।",
                        filename="crowd_alert.mp3"
                    )
                    st.session_state.active_alert = "CROWD"

            # ── 3. RESET (When frame is clear & normal) ──
            else:
                if st.session_state.get("active_alert") is not None:
                    alert_pos.empty()  # <-- CRITICAL: Screen se purana alert banner clear karega
                st.session_state.active_alert = None

    cap.release()
