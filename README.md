# 🚨 HazardLens

### Real-Time AI Surveillance, Hazard Detection & Emergency Response Platform

**HazardLens** is an AI-powered surveillance platform that transforms traditional CCTV/IP cameras into intelligent hazard monitoring systems.

It uses **YOLOv8, OpenCV and Streamlit** to detect **fire, smoke and overcrowding** in real time and provides instant visual and Hindi voice alerts.

The application is **Dockerized** for consistent deployment, while **Terraform + AWS** are used for cloud infrastructure automation.

---

## 🎯 Problem Statement

Traditional CCTV systems depend on human operators to continuously monitor video feeds and identify emergencies.

This can cause delays in:

**Detection → Verification → Alert → Response**

HazardLens automates this process by continuously analyzing live camera feeds and generating alerts whenever a potential hazard is detected.

> **Detect hazards early. Alert instantly. Respond faster.**

---

## ✨ Key Features

* 🔥 **Fire & Smoke Detection** — Custom YOLOv8-based detection model
* 👥 **Crowd Monitoring** — Real-time person detection and overcrowding alerts
* 🚨 **Smart Alert System** — `"Latest Hazard Wins"` event management
* 🎙️ **Hindi Voice Alerts** — Microsoft Edge-TTS integration
* 📹 **CCTV/IP Camera Support** — OpenCV-based live video processing
* 🖥️ **Command Center Dashboard** — Real-time Streamlit interface
* 🎯 **Confidence Filtering** — Configurable detection threshold
* 🐳 **Dockerized Application** — Portable and reproducible deployment
* ☁️ **Terraform + AWS** — Infrastructure as Code

---

## 🏗️ System Architecture

```text
              CCTV / IP Camera
                      │
                      ▼
               OpenCV Processing
                      │
             ┌────────┴────────┐
             ▼                 ▼
      Fire / Smoke AI      Crowd AI
         YOLOv8             YOLOv8
             │                 │
             └────────┬────────┘
                      ▼
              Hazard Detection
                      │
                      ▼
               Alert Manager
                 ┌────┴────┐
                 ▼         ▼
            Streamlit    Hindi Voice
            Dashboard      Alert
```

---

## 🛠️ Tech Stack

| Category            | Technologies          |
| ------------------- | --------------------- |
| 🤖 AI/ML            | YOLOv8, Ultralytics   |
| 👁️ Computer Vision | OpenCV, NumPy, Pillow |
| 🖥️ Dashboard       | Streamlit             |
| 🔊 Voice            | Microsoft Edge-TTS    |
| 🐍 Backend          | Python, AsyncIO       |
| 🐳 DevOps           | Docker                |
| ☁️ Cloud            | AWS                   |
| 🏗️ Infrastructure  | Terraform             |

---

## 🐳 Docker Setup

HazardLens can be deployed as a Docker container.

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

### Open Dashboard

```text
http://localhost:8501
```

---

## ☁️ Terraform & AWS

Cloud infrastructure is maintained separately using Terraform.

### Terraform Repository

https://github.com/nitin-panwar-6963/HazardLens-terraform.git

Basic workflow:

```bash
terraform init
terraform validate
terraform plan
terraform apply
```

Infrastructure is maintained by **Nitin Panwar — DevOps & Cloud Engineer**.

---

## 📁 Project Structure

```text
HazardLens/
│
├── app.py
├── best.pt
├── requirements.txt
├── Dockerfile
├── README.md
│
└── assets/
    ├── dashboard.png
    ├── fire-detection.png
    └── crowd-detection.png
```

---

## 🖼️ Dashboard

Add project screenshots to the `assets/` directory:

```markdown
![HazardLens Dashboard](assets/dashboard.png)
```

---

## 🎯 Potential Applications

* 🏙️ Smart Cities
* 🏫 University Campuses
* 🚉 Railway Stations
* ✈️ Airports
* 🏭 Industrial Facilities
* 🛍️ Shopping Malls
* 🎪 Public Events
* 🏢 Corporate Buildings

---

## 🔮 Future Scope

* Multi-camera monitoring
* Cloud-based emergency notifications
* CI/CD automation
* Kubernetes deployment
* Prometheus & Grafana monitoring
* Historical incident analytics
* Automated emergency escalation

---

## 👥 Team

### ☁️ Nitin Panwar

**DevOps & Cloud Engineer**

Responsible for:

`Docker` • `Terraform` • `AWS` • `Deployment` • `Cloud Infrastructure`

GitHub:
https://github.com/nitin-panwar-6963

Terraform:
https://github.com/nitin-panwar-6963/HazardLens-terraform

---

### 🤖 Tushar Singh

**Backend & AI Integration**

Responsible for:

`Python` • `YOLOv8` • `AI/ML` • `Computer Vision` • `Backend Logic`

GitHub:
https://github.com/tusharsingh-sde

---

## 📜 License

This project is licensed under the **MIT License**.

---

<div align="center">

### 🚨 HazardLens

**See the Hazard. Understand the Risk. Respond Faster.**

Built with **AI + Computer Vision + Cloud + DevOps**

</div>
