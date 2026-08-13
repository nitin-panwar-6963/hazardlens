# 🚨 HazardLens

### Real-Time AI Surveillance, Hazard Detection & Emergency Response Platform

> **HazardLens** is an AI-powered real-time surveillance platform that transforms traditional CCTV/IP cameras into intelligent hazard-monitoring systems.

It uses **YOLOv8-based computer vision models** to detect critical situations such as **fire, smoke, and overcrowding** in real time. Detected hazards are immediately presented through a tactical dashboard and can trigger **Hindi voice alerts** to reduce emergency response time.

The project is designed with a **containerized deployment architecture using Docker** and infrastructure automation using **Terraform on AWS**.

---

## 👥 Team

| Member           | Role                        | Responsibility                                                         |
| ---------------- | --------------------------- | ---------------------------------------------------------------------- |
| **Nitin Panwar** | ☁️ DevOps & Cloud Engineer  | Docker, Terraform, AWS Infrastructure, Deployment & Cloud Architecture |
| **Tushar Singh** | 🤖 Backend & AI Integration | AI/ML Integration, Backend Logic, YOLOv8 & Hazard Detection            |

---

## 🎯 Problem Statement

Traditional CCTV systems are mostly passive monitoring tools.

During emergencies, an incident often needs to be:

**Detected → Observed → Verified → Reported → Escalated**

This manual process can introduce critical delays.

HazardLens aims to automate this workflow by continuously analyzing live camera feeds and generating immediate alerts whenever a dangerous situation is detected.

### Our Goal

> **Detect hazards early. Alert people instantly. Reduce emergency response time.**

---

# ✨ Key Features

### 🔥 Real-Time Fire & Smoke Detection

* Custom YOLOv8-based fire and smoke detection model
* Real-time inference on live video streams
* Confidence-based detection filtering
* Optimized for edge-oriented deployment

### 👥 Crowd & Overcrowding Detection

* Real-time person detection
* Crowd density monitoring
* Configurable overcrowding threshold
* Automatic hazard classification

### 🎙️ Hindi Voice Alerts

* Hindi neural voice notifications
* Microsoft Edge-TTS integration
* `hi-IN-SwaraNeural` voice
* Asynchronous audio generation
* Alert collision prevention

### 🚨 Smart Alert Management

* Real-time hazard banners
* Priority-based hazard handling
* `"Latest Hazard Wins"` event logic
* Prevents repeated alert loops
* Prevents overlapping audio alerts

### 📹 CCTV / IP Camera Support

* OpenCV-based video processing
* Live camera stream support
* Frame-by-frame AI inference
* Real-time dashboard visualization

### 🖥️ Tactical Command Center

* Streamlit-based monitoring dashboard
* Live camera feed
* Detection overlays
* Hazard status
* Real-time alerts
* AI monitoring statistics

### 🐳 Containerized Deployment

* Dockerized application
* Reproducible runtime environment
* Portable deployment
* Cloud and edge deployment ready

### ☁️ Infrastructure as Code

* AWS infrastructure managed using Terraform
* Separate Terraform repository
* Repeatable infrastructure provisioning
* DevOps-oriented deployment architecture

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │   CCTV / IP Camera   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   OpenCV Processing  │
                    │   Live Video Frames  │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │ Fire / Smoke AI │        │  Crowd AI Model │
        │   YOLOv8 Model  │        │     YOLOv8n     │
        └────────┬────────┘        └────────┬────────┘
                 │                          │
                 └────────────┬─────────────┘
                              ▼
                  ┌─────────────────────────┐
                  │  Hazard Detection       │
                  │  Engine                 │
                  │  Confidence Filtering   │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Alert & Event Manager   │
                  │ "Latest Hazard Wins"    │
                  └────────────┬────────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
          ┌─────────────────┐   ┌──────────────────┐
          │ Visual Alert    │   │ Hindi Voice      │
          │ Streamlit UI    │   │ Alert - TTS      │
          └─────────────────┘   └──────────────────┘
```

---

# 🧠 AI Detection Pipeline

```text
Live Camera Feed
       │
       ▼
OpenCV Frame Capture
       │
       ▼
Frame Preprocessing
       │
       ├───────────────┐
       ▼               ▼
 Fire/Smoke Model   Crowd Model
       │               │
       └───────┬───────┘
               ▼
        Detection Engine
               │
               ▼
       Confidence Filter
          conf = 0.70
               │
               ▼
        Hazard Classification
               │
               ▼
        Alert State Manager
          ┌────┴─────┐
          ▼          ▼
       Dashboard   Voice Alert
```

---

# 🛠️ Technology Stack

## 🤖 Artificial Intelligence

* YOLOv8
* Ultralytics
* Custom Fire & Smoke Detection Model
* Person Detection
* Crowd Density Analysis
* Confidence Thresholding

## 👁️ Computer Vision

* OpenCV
* `opencv-python-headless`
* NumPy
* Pillow

## 🖥️ Dashboard

* Streamlit
* Real-time video rendering
* Interactive hazard monitoring
* Alert state visualization

## 🔊 Voice & Audio

* Microsoft Edge-TTS
* Hindi Neural Voice
* `hi-IN-SwaraNeural`
* Python `asyncio`

## 🐍 Backend

* Python 3.10+
* AsyncIO
* Event Management
* AI Inference Pipeline

## 🐳 DevOps

* Docker
* Dockerfile
* Containerized Deployment
* Docker Hub Compatible

## ☁️ Cloud & Infrastructure

* AWS
* Terraform
* Infrastructure as Code
* Cloud Deployment Automation

---

# 🐳 Docker Setup

HazardLens is fully containerized using Docker, making the application portable and easy to deploy.

## 1. Build Docker Image

```bash
docker build -t hazardlens .
```

## 2. Run Container

```bash
docker run -d \
  --name hazardlens \
  -p 8501:8501 \
  hazardlens
```

## 3. Verify Container

```bash
docker ps
```

## 4. Access Dashboard

Open:

```text
http://localhost:8501
```

## 5. Stop Container

```bash
docker stop hazardlens
```

## 6. Remove Container

```bash
docker rm hazardlens
```

## 7. Remove Image

```bash
docker rmi hazardlens
```

---

# 🐳 Docker Architecture

```text
                 GitHub Repository
                         │
                         ▼
                   Docker Build
                         │
                         ▼
                 HazardLens Image
                         │
                         ▼
                Docker Container
                         │
                         ▼
               Streamlit Dashboard
                         │
                         ▼
                AI Hazard Detection
```

---

# ☁️ Terraform & AWS Infrastructure

The cloud infrastructure configuration is maintained separately from the main application repository.

### Terraform Repository

🔗 **HazardLens Terraform**

https://github.com/nitin-panwar-6963/HazardLens-terraform.git

The Terraform infrastructure is maintained by:

**Nitin Panwar — DevOps & Cloud Engineer**

The repository contains the infrastructure configuration required for cloud deployment and provisioning.

### Terraform Workflow

```bash
terraform init
terraform validate
terraform plan
terraform apply
```

To destroy the provisioned infrastructure:

```bash
terraform destroy
```

---

# 🔄 Cloud Deployment Architecture

```text
                         GitHub
                           │
                           ▼
                 ┌──────────────────┐
                 │  HazardLens App  │
                 └────────┬─────────┘
                          │
                          ▼
                      Docker
                          │
                          ▼
                  Container Image
                          │
                          ▼
                     AWS Cloud
                          │
                 ┌────────┴────────┐
                 │                 │
                 ▼                 ▼
             Terraform          Compute
          Infrastructure        Instance
                 │                 │
                 └────────┬────────┘
                          ▼
                  HazardLens App
                          │
                          ▼
                 Streamlit Dashboard
```

---

# 📁 Project Structure

```text
HazardLens/
│
├── app.py
├── best.pt
├── requirements.txt
├── Dockerfile
├── README.md
│
├── assets/
│   ├── dashboard.png
│   ├── fire-detection.png
│   └── crowd-detection.png
│
└── ...
```

> Terraform infrastructure is maintained separately in:
>
> **HazardLens-terraform**

---

# 🖼️ Application Screenshots

Add project screenshots inside the `assets/` directory.

### 🚨 Tactical Command Center

```markdown
![HazardLens Dashboard](assets/dashboard.png)
```

### 🔥 Fire / Smoke Detection

```markdown
![Fire Detection](assets/fire-detection.png)
```

### 👥 Crowd Monitoring

```markdown
![Crowd Detection](assets/crowd-detection.png)
```

---

# ⚙️ Detection Configuration

HazardLens uses confidence-based filtering to reduce false detections.

```python
CONFIDENCE_THRESHOLD = 0.70
```

This helps reduce unwanted detections caused by:

* Lighting variations
* Shadows
* Background noise
* Low-confidence predictions

The threshold can be adjusted according to the deployment environment.

---

# 🚨 Alert State Management

HazardLens uses a priority-based event management approach.

```text
New Hazard Detected
        │
        ▼
Compare With Current State
        │
        ▼
   Latest Hazard Wins
        │
        ├───────────────┐
        ▼               ▼
 Visual Alert       Voice Alert
        │               │
        └───────┬───────┘
                ▼
          Updated State
```

This helps prevent:

* Repeated alerts
* Audio overlap
* UI freezing
* Alert loops
* Race conditions

---

# 🎯 Potential Applications

HazardLens can be adapted for:

* 🏙️ Smart Cities
* 🏫 University Campuses
* 🚉 Railway Stations
* ✈️ Airports
* 🛍️ Shopping Malls
* 🏭 Industrial Facilities
* 📦 Warehouses
* 🎪 Public Events
* 🏟️ Stadiums
* 🚧 Construction Sites
* 🚪 Entry & Gate Surveillance
* 🏢 Corporate Buildings

---

# 🔮 Future Roadmap

* [ ] Real-time multi-camera monitoring
* [ ] Multi-stream CCTV support
* [ ] Advanced crowd-density estimation
* [ ] Fire severity classification
* [ ] Smoke density estimation
* [ ] Automated emergency escalation
* [ ] SMS / Email notifications
* [ ] Cloud-based monitoring dashboard
* [ ] Centralized event logging
* [ ] AWS CloudWatch integration
* [ ] CI/CD pipeline
* [ ] Kubernetes deployment
* [ ] Prometheus & Grafana monitoring
* [ ] Role-based dashboard access
* [ ] Historical incident analytics

---

# 🧩 Engineering Challenges Solved

### 🎥 Real-Time Video Processing

Processing live CCTV frames while maintaining responsive dashboard performance.

### 🤖 Dual AI Model Architecture

Running dedicated models for fire/smoke and crowd detection.

### 🎯 False Positive Reduction

Using confidence thresholds and detection logic to reduce unwanted alerts.

### 🔊 Alert Race Conditions

Managing multiple hazard events without allowing audio and UI alerts to collide.

### 🎙️ Automated Voice Alerts

Generating localized Hindi voice notifications based on detected hazards.

### 🐳 Containerized Deployment

Packaging the application into a reproducible Docker environment.

### ☁️ Cloud Infrastructure

Managing deployment infrastructure through Terraform and AWS.

---

# 📊 Project Highlights

| Capability          | Technology                  |
| ------------------- | --------------------------- |
| 🔥 Fire Detection   | YOLOv8                      |
| 💨 Smoke Detection  | Custom AI Model             |
| 👥 Person Detection | YOLOv8                      |
| 🚨 Crowd Monitoring | Detection + Threshold Logic |
| 🎥 Video Processing | OpenCV                      |
| 🖥️ Dashboard       | Streamlit                   |
| 🎙️ Voice Alerts    | Microsoft Edge-TTS          |
| ⚡ Async Processing  | Python AsyncIO              |
| 🐳 Containerization | Docker                      |
| ☁️ Infrastructure   | Terraform                   |
| 🌐 Cloud            | AWS                         |
| 🐍 Programming      | Python                      |

---

# 🔐 Security & Deployment Considerations

For production deployment:

* Use environment variables for secrets
* Restrict exposed cloud ports
* Configure AWS Security Groups properly
* Never commit API keys
* Use private networking where possible
* Enable HTTPS for public deployments
* Store sensitive configuration outside Git
* Follow least-privilege IAM policies

---

# 👨‍💻 Team

## ☁️ Nitin Panwar

### DevOps & Cloud Engineer

Responsible for:

* AWS Cloud Infrastructure
* Terraform
* Docker
* Deployment
* Infrastructure Automation
* Cloud Architecture

**GitHub:**
https://github.com/nitin-panwar-6963

**Terraform Repository:**
https://github.com/nitin-panwar-6963/HazardLens-terraform.git

---

## 🤖 Tushar Singh

### Backend & AI Integration

Responsible for:

* AI/ML Integration
* YOLOv8 Models
* Fire & Smoke Detection
* Crowd Detection
* Python Backend Logic
* Voice Alert Integration

**GitHub:**
https://github.com/tusharsingh-sde

---

# 🤝 Contribution

Contributions, suggestions, and improvements are welcome.

```bash
# Fork the repository

# Clone your fork
git clone <your-fork-url>

# Create a new branch
git checkout -b feature/new-feature

# Make your changes

# Commit
git add .
git commit -m "Add new feature"

# Push
git push origin feature/new-feature

# Open a Pull Request
```

---

# 📜 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you find **HazardLens** interesting or useful:

⭐ Star the repository
🍴 Fork the project
🐛 Report issues
💡 Suggest improvements
🤝 Contribute to the project

---

<div align="center">

# 🚨 HazardLens

### See the Hazard. Understand the Risk. Respond Faster.

**AI + Computer Vision + Cloud + DevOps**

**Tushar Singh — Backend & AI Integration**
**Nitin Panwar — DevOps & Cloud Engineer**

</div>
