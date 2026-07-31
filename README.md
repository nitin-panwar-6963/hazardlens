# 🚨 HazardLens
### Real-Time AI Surveillance, Hazard Detection & Emergency Response Platform

HazardLens is an edge-optimized, autonomous AI surveillance system that transforms traditional CCTV cameras into intelligent hazard monitoring agents. Built using dual YOLOv8 architectures and a zero-dependency local neural TTS engine, it continuously monitors live video feeds for fire, smoke, and overcrowding, delivering instant visual banners and Hindi voice broadcasts to dramatically reduce emergency response time.

---

## 📌 Problem Statement

Traditional CCTV systems are passive monitoring tools. In emergency situations, incidents are detected only after a human operator notices them, verifies them, and manually escalates the alarm. This critical delay increases physical damage, risks human life, and slows down emergency response.

HazardLens bridges this gap by providing **low-latency automated hazard detection, smart alert prioritization, and instant localized voice broadcasts** at the edge.

---

## ✨ Key Features

- 🔥 **Real-time Fire & Smoke Detection:** Custom fine-tuned AI model with multilingual class mapping.
- 👥 **Crowd Monitoring & Overcrowding Alerts:** Real-time human density tracking and threshold-based alerts.
- 🎙️ **Zero-Dependency Hindi Neural Voice Alerts:** Locally powered by Microsoft Edge-TTS (`hi-IN-SwaraNeural`) — completely free and offline-capable.
- 🎯 **False-Positive Immunity (`conf=0.70`):** Optimized detection thresholds to ignore shadows, lighting changes, and skin tones.
- ⚡ **"Latest Hazard Wins" State Machine:** Prevents UI freezes, alert looping, and audio overlapping.
- 📹 **IP Camera / CCTV Feed Support:** Direct OpenCV frame stream processing.
- 🖥️ **Tactical Command Center Dashboard:** Low-latency interface built on Streamlit shared memory architecture.

---

## 🏗️ System Architecture

```text
               Live CCTV / IP Camera Feed
                           │
                           ▼
              OpenCV Video Frame Processing
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
          Fire / Smoke Model    Crowd Model
         (Custom best.pt 6MB)  (YOLOv8n 6MB)
                 │                   │
                 └─────────┬─────────┘
                           ▼
              Hazard Detection Engine (conf=0.70)
                           │
                           ▼
                 Alert & Event Manager
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
         Visual Alert Banner    Hindi Voice Alert
          (Streamlit UI DOM)   (Edge-TTS Neural Voice)

---

## 🛠️ Tech Stack

### Frontend & Dashboard
- Streamlit (Shared Memory Architecture)

### Computer Vision
- OpenCV (`opencv-python-headless`)
- Ultralytics YOLOv8
- Custom Fire & Smoke Detection Model (`best.pt` - 6MB)

### AI Voice Engine
- Microsoft Edge-TTS (`hi-IN-SwaraNeural` — Local Hindi Neural Voice)

### Core & Backend
- Python 3.10+
- `asyncio` (Asynchronous Audio Generation)

### Utilities
- NumPy
- Pillow

---

## 🚀 Installation & Quick Start

### 1. Clone Repository

```bash
git clone [https://github.com/tusharsingh-sde/HazardLens.git](https://github.com/tusharsingh-sde/HazardLens.git)

cd HazardLens

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Potential Applications

- Smart Cities & Urban Surveillance
- University Campuses
- Railway Stations & Airports
- Shopping Malls & Retail Hubs
- Industrial Facilities & Warehouses
- Public Event & Concert Monitoring
- Traffic & Gate Surveillance

---

## 🔮 Future Roadmap

- Zero-lag real-time CCTV stream processing via shared memory
- Dual-model AI inference architecture (best.pt + yolov8n.pt)
- False-positive mitigation (conf=0.70 threshold tuning)
- Automated offline Hindi voice alerts without cloud API bottlenecks
- Race-condition audio collision and DOM freeze prevention
- "Latest Hazard Wins" priority triage state machine

---

## 💡 Engineering Challenges Solved

- Real-time CCTV stream processing
- Dual-model AI inference architecture
- Crowd density estimation
- Hazard event classification
- Automated voice alert generation
- Low-latency monitoring dashboard

---

## 👨‍💻 Author

**Tushar Singh**

B.Tech CSE Student

Passionate about AI, Computer Vision, Smart Infrastructure and Public Safety Systems.

GitHub: https://github.com/tusharsingh-sde

---

## 📜 License

This project is licensed under the MIT License.
