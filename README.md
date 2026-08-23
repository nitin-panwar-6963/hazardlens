<div align="center">

# 🚨 HazardLens

### Real-Time AI Surveillance & Emergency Response Platform

**Turning CCTV cameras into intelligent hazard detection systems.**

<br/>

<img src="https://img.shields.io/badge/AI-YOLOv8-blue?style=for-the-badge&logo=ai" />
<img src="https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react" />
<img src="https://img.shields.io/badge/Backend-Python-3776AB?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/DevOps-Docker-2496ED?style=for-the-badge&logo=docker" />
<img src="https://img.shields.io/badge/CI/CD-Jenkins-D24939?style=for-the-badge&logo=jenkins" />
<img src="https://img.shields.io/badge/Code%20Quality-SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube" />
<img src="https://img.shields.io/badge/Security-Trivy-1904DA?style=for-the-badge&logo=trivy" />
<img src="https://img.shields.io/badge/Cloud-AWS-FF9900?style=for-the-badge&logo=amazonaws" />
<img src="https://img.shields.io/badge/Cloud-Azure-0078D4?style=for-the-badge&logo=microsoftazure" />
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

# ⚙️ DevOps & CI/CD Pipeline

HazardLens uses a **Jenkins-based CI/CD pipeline** to automate application building, security scanning, code-quality analysis, Docker image creation, and deployment.

```text
                    Developer
                        │
                        ▼
                   GitHub Push
                        │
                        ▼
                 ┌──────────────┐
                 │    Jenkins   │
                 └──────┬───────┘
                        │
              ┌─────────┴─────────┐
              │                   │
              ▼                   ▼
        Install Dependencies   SonarQube
              │               Code Analysis
              │                   │
              └─────────┬─────────┘
                        ▼
                 Build Application
                        │
                        ▼
                  Docker Build
                        │
                        ▼
                 ┌──────────────┐
                 │    Trivy     │
                 │Security Scan │
                 └──────┬───────┘
                        │
                        ▼
                Docker Image Push
                        │
                        ▼
                 Cloud Deployment
                  ┌─────┴─────┐
                  ▼           ▼
                 AWS         Azure
                  │           │
                  ▼           ▼
                 EC2       Azure VM
                  │           │
                  └─────┬─────┘
                        ▼
                    HazardLens
```

---

## 🔄 CI/CD Pipeline Stages

| Stage             | Tool          | Purpose                               |
| ----------------- | ------------- | ------------------------------------- |
| 📥 Checkout       | Jenkins + Git | Clone source code                     |
| 📦 Dependencies   | Python / npm  | Install application dependencies      |
| 🧪 Test           | Jenkins       | Run application tests                 |
| 🔍 Code Quality   | SonarQube     | Static code analysis                  |
| 🐳 Docker Build   | Docker        | Build application image               |
| 🛡️ Security Scan | Trivy         | Scan Docker image for vulnerabilities |
| 📤 Image Push     | Docker Hub    | Store container image                 |
| 🚀 Deployment     | Jenkins       | Deploy application                    |
| ☁️ Infrastructure | Terraform     | Provision AWS/Azure infrastructure    |

---

## 🔧 Jenkins

Jenkins is used to automate the complete **CI/CD workflow** of HazardLens.

### Jenkins Pipeline

The repository contains a `Jenkinsfile` that defines the CI/CD stages.

```text
Jenkinsfile
    │
    ├── Checkout
    ├── Install Dependencies
    ├── Test
    ├── SonarQube Analysis
    ├── Docker Build
    ├── Trivy Security Scan
    ├── Docker Push
    └── Deployment
```

### Example Jenkinsfile Structure

```groovy
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t hazardlens:latest .'
            }
        }

        stage('Trivy Security Scan') {
            steps {
                sh 'trivy image --severity HIGH,CRITICAL hazardlens:latest'
            }
        }

        stage('Docker Push') {
            steps {
                sh 'docker push hazardlens:latest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 8501:8501 hazardlens:latest'
            }
        }
    }
}
```

> 🔐 Docker Hub credentials, SonarQube credentials, and cloud credentials should be stored securely using **Jenkins Credentials Manager** rather than hard-coded inside the Jenkinsfile.

---

# 🔍 SonarQube — Code Quality

**SonarQube** is integrated into the Jenkins pipeline to perform automated static code analysis.

### SonarQube checks

* 🔎 Code smells
* 🐛 Bugs
* 🔐 Security vulnerabilities
* 📊 Code quality
* ♻️ Duplicated code
* 📈 Maintainability

```text
Jenkins
   │
   ▼
Source Code
   │
   ▼
SonarQube Scanner
   │
   ▼
SonarQube Server
   │
   ▼
Quality Analysis
```

Example command:

```bash
sonar-scanner
```

---

# 🛡️ Trivy — Container Security

**Trivy** is used to scan Docker images for known security vulnerabilities before deployment.

### Security workflow

```text
Docker Build
     │
     ▼
HazardLens Image
     │
     ▼
Trivy Scan
     │
     ├── LOW
     ├── MEDIUM
     ├── HIGH
     └── CRITICAL
            │
            ▼
      Security Report
```

Example:

```bash
trivy image hazardlens:latest
```

For high and critical vulnerabilities:

```bash
trivy image --severity HIGH,CRITICAL hazardlens:latest
```

This helps prevent vulnerable container images from reaching the deployment environment.

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
             │ React       │     │ Hindi Voice │
             │ Dashboard   │     │    Alert    │
             └─────────────┘     └─────────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Docker Container  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Jenkins CI/CD     │
                    └─────────┬─────────┘
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
            ┌──────────┐              ┌──────────┐
            │ SonarQube│              │  Trivy   │
            │  Quality │              │ Security │
            └──────────┘              └──────────┘
                              │
                              ▼
                     AWS / Azure Cloud
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
<td>🔄 CI/CD</td>
<td>Jenkins</td>
</tr>

<tr>
<td>🔍 Code Quality</td>
<td>SonarQube</td>
</tr>

<tr>
<td>🛡️ Security Scanning</td>
<td>Trivy</td>
</tr>

<tr>
<td>☁️ Cloud Platforms</td>
<td>AWS & Microsoft Azure</td>
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

### Security Scan

```bash
trivy image hazardlens
```

### Access Application

```text
http://localhost:8501
```

---

## ☁️ Cloud Infrastructure

The cloud infrastructure is managed separately using **Terraform**.

### 🟠 AWS Infrastructure

<a href="https://github.com/nitin-panwar-6963/HazardLens-terraform">

<img src="https://img.shields.io/badge/AWS%20Terraform-Infrastructure-7B42BC?style=for-the-badge&logo=terraform" />

</a>

### 🔵 Azure Infrastructure

<a href="https://github.com/nitin-panwar-6963/hazardlens-terraform-ansible">

<img src="https://img.shields.io/badge/AWS%20%26%20Azure%20Terraform-Infrastructure-7B42BC?style=for-the-badge&logo=terraform" />

</a>

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
├── Jenkinsfile
├── sonar-project.properties
├── Dockerfile
├── requirements.txt
├── .dockerignore
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
* [x] Jenkins CI/CD pipeline
* [x] SonarQube code quality analysis
* [x] Trivy container security scanning
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

Docker • Jenkins • Terraform • AWS • Azure • SonarQube • Trivy • Cloud Infrastructure

<a href="https://github.com/nitin-panwar-6963">
<img src="https://img.shields.io/badge/GitHub-Nitin%20Panwar-black?style=for-the-badge&logo=github" />
</a>

<br/><br/>

<a href="https://github.com/nitin-panwar-6963/hazardlens-terraform-ansible">
<img src="https://img.shields.io/badge/Cloud%20Infrastructure-Repository-7B42BC?style=for-the-badge&logo=terraform" />
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

**AI • Computer Vision • React • Docker • Jenkins • SonarQube • Trivy • AWS • Azure • Terraform**

<br/>

⭐ **Star the repository if you like the project!**

</div>
