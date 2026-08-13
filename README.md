<div align="center">

# 🚨 HazardLens

### Real-Time AI Surveillance & Emergency Response Platform

**Turning CCTV cameras into intelligent hazard detection systems.**

<br/>

<img src="https://img.shields.io/badge/AI-YOLOv8-blue?style=for-the-badge&logo=ai" />
<img src="https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react" />
<img src="https://img.shields.io/badge/Backend-Python-3776AB?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/DevOps-Docker-2496ED?style=for-the-badge&logo=docker" />
<img src="https://img.shields.io/badge/Cloud-AWS-FF9900?style=for-the-badge&logo=amazonaws" />
<img src="https://img.shields.io/badge/IaC-Terraform-7B42BC?style=for-the-badge&logo=terraform" />

<br/><br/>

</div>

---

## 🚨 About HazardLens

<table>
<tr>
<td width="60%">

**HazardLens** is an AI-powered real-time surveillance platform designed to transform traditional **CCTV/IP cameras into intelligent monitoring systems**.

The platform analyzes live video streams using **YOLOv8 and OpenCV** to detect:

* 🔥 Fire
* 💨 Smoke
* 👥 Overcrowding

When a hazard is detected, the system generates **real-time visual alerts and Hindi voice notifications**, helping reduce emergency response time.

</td>

<td width="40%">

```text
📹 CCTV
   ↓
👁️ Computer Vision
   ↓
🤖 AI Detection
   ↓
🚨 Alert Engine
   ↓
🖥️ Dashboard
   +
🎙️ Voice Alert
```

</td>
</tr>
</table>

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🔥 Fire & Smoke Detection

YOLOv8-powered real-time detection for fire and smoke events.

### 👥 Crowd Monitoring

Detects people and identifies potential overcrowding situations.

### 🚨 Smart Alert Engine

Priority-based `"Latest Hazard Wins"` logic prevents repeated and conflicting alerts.

</td>

<td width="50%">

### 🎙️ Hindi Voice Alerts

Generates localized Hindi emergency notifications using Edge-TTS.

### 📹 Live CCTV Support

OpenCV-based processing for CCTV and IP camera streams.

### 🖥️ Real-Time Dashboard

Modern monitoring interface for live detections and alerts.

</td>
</tr>
</table>

---

## 🧠 System Architecture

<div align="center">

```text
                    ┌───────────────────┐
                    │   CCTV / IP Feed  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ OpenCV Processing │
                    └─────────┬─────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
             ┌─────────────┐     ┌─────────────┐
             │ Fire/Smoke  │     │ Crowd Model │
             │   YOLOv8    │     │   YOLOv8    │
             └──────┬──────┘     └──────┬──────┘
                    │                   │
                    └─────────┬─────────┘
                              ▼
                    ┌───────────────────┐
                    │ Hazard Detection  │
                    │    & Alert Engine │
                    └─────────┬─────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
             ┌─────────────┐     ┌─────────────┐
             │ React        │     │ Hindi Voice │
             │ Dashboard    │     │    Alert    │
             └─────────────┘     └─────────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Docker Container  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   AWS + Terraform │
                    └───────────────────┘
```

</div>

---

## 🛠️ Technology Stack

<table>
<tr>
<th>Layer</th>
<th>Technology</th>
</tr>

<tr>
<td>🎨 Frontend Framework</td>
<td>React.js</td>
</tr>

<tr>
<td>🎨 UI Styling</td>
<td>Tailwind CSS</td>
</tr>

<tr>
<td>🤖 AI/ML Framework</td>
<td>Ultralytics YOLOv8</td>
</tr>

<tr>
<td>👁️ Computer Vision</td>
<td>OpenCV, NumPy, Pillow</td>
</tr>

<tr>
<td>⚙️ Backend</td>
<td>Python, AsyncIO</td>
</tr>

<tr>
<td>🔊 Voice Engine</td>
<td>Microsoft Edge-TTS</td>
</tr>

<tr>
<td>🐳 Containerization</td>
<td>Docker</td>
</tr>

<tr>
<td>☁️ Cloud Platform</td>
<td>AWS</td>
</tr>

<tr>
<td>🏗️ Infrastructure as Code</td>
<td>Terraform</td>
</tr>

</table>

---

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t hazardlens .
```

### Run Container

```bash
docker run -d \
  --name hazardlens \
  -p 8501:8501 \
  hazardlens
```

### Check Container

```bash
docker ps
```

### Access Application

```text
http://localhost:8501
```

---

## ☁️ Cloud Infrastructure

The AWS infrastructure is maintained separately using **Terraform**.

<div align="center">

### 🔗 Terraform Repository

<a href="https://github.com/nitin-panwar-6963/HazardLens-terraform">
  <img src="https://img.shields.io/badge/Terraform%20Infrastructure-View%20Repository-7B42BC?style=for-the-badge&logo=terraform" />
</a>

</div>

```bash
terraform init
terraform validate
terraform plan
terraform apply
```

---

## 📁 Project Structure

```text
HazardLens/
│
├── frontend/
│   └── React Application
│
├── backend/
│   ├── app.py
│   └── AI Detection Logic
│
├── models/
│   └── best.pt
│
├── assets/
│   ├── dashboard.png
│   ├── fire-detection.png
│   └── crowd-detection.png
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🎯 Use Cases

<table>
<tr>
<td align="center">🏙️<br/><b>Smart Cities</b></td>
<td align="center">🚉<br/><b>Railway Stations</b></td>
<td align="center">✈️<br/><b>Airports</b></td>
</tr>
<tr>
<td align="center">🏫<br/><b>Campuses</b></td>
<td align="center">🏭<br/><b>Industries</b></td>
<td align="center">🏟️<br/><b>Public Events</b></td>
</tr>
</table>

---

## 🔮 Future Roadmap

* [ ] Multi-camera monitoring
* [ ] Cloud-based emergency notifications
* [ ] CI/CD automation
* [ ] Kubernetes deployment
* [ ] Prometheus & Grafana monitoring
* [ ] Historical incident analytics
* [ ] Automated emergency escalation

---

## 👥 Team

<table>
<tr>

<td align="center" width="50%">

### ☁️ Nitin Panwar

**DevOps & Cloud Engineer**

Docker • Terraform • AWS • Cloud Infrastructure • Deployment

<a href="https://github.com/nitin-panwar-6963">
<img src="https://img.shields.io/badge/GitHub-Nitin%20Panwar-black?style=for-the-badge&logo=github" />
</a>

<br/><br/>

<a href="https://github.com/nitin-panwar-6963/HazardLens-terraform">
<img src="https://img.shields.io/badge/Terraform-Repository-7B42BC?style=for-the-badge&logo=terraform" />
</a>

</td>

<td align="center" width="50%">

### 🤖 Tushar Singh

**Backend & AI Integration**

Python • YOLOv8 • AI/ML • Computer Vision • Backend

<a href="https://github.com/tusharsingh-sde">
<img src="https://img.shields.io/badge/GitHub-Tushar%20Singh-black?style=for-the-badge&logo=github" />
</a>

</td>

</tr>
</table>

---

## 📜 License

This project is licensed under the **MIT License**.

---

<div align="center">

## 🚨 HazardLens

### **See the Hazard. Understand the Risk. Respond Faster.**

**AI • Computer Vision • React • Docker • AWS • Terraform**

<br/>

⭐ **Star the repository if you like the project!**

</div>

