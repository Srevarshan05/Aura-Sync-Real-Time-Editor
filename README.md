<div align="center">

# 🚀 Aura Sync
### AI-Powered Real-Time Collaborative Cloud IDE for Arduino Development

<img src="assets/banner.png" width="100%"/>

[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?style=for-the-badge&logo=node.js&logoColor=white)]()
[![Docker](https://img.shields.io/badge/Docker-Latest-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![Arduino](https://img.shields.io/badge/Arduino-CLI-00979D?style=for-the-badge&logo=arduino&logoColor=white)]()
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Cloud%20Run-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)]()
[![WebSockets](https://img.shields.io/badge/WebSockets-Real--Time-blue?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)]()

*A browser-based collaborative Arduino IDE with real-time editing, AI-assisted code generation, cloud compilation, and remote hardware access.*

</div>

---

# 🌟 Overview

Aura Sync is a **real-time collaborative cloud IDE** built for **embedded systems and Arduino development**, enabling multiple engineers to write, compile, execute, and interact with hardware simultaneously from anywhere in the world.

Unlike traditional Arduino workflows that rely on locally installed IDEs and manually sharing `.ino` files, Aura Sync brings the entire embedded development workflow into the browser.

Think of it as:

> **Google Docs × Visual Studio Code × Arduino IDE**

but purpose-built for embedded systems.

Every participant in a session views the exact same editor, receives live updates in real time, observes identical compiler output, and can collaboratively build firmware together.

The platform combines:

- ⚡ Real-time collaborative editing
- 🤖 AI-powered Arduino C++ generation
- 🐳 Sandboxed cloud compilation
- 🔗 Shareable collaboration sessions
- 🌍 Remote hardware access
- ☁️ Cloud-native deployment

---

# 💡 The Story Behind Aura Sync

Embedded systems development has traditionally been an individual workflow.

One engineer writes code.

Another engineer receives the project.

Someone else tries compiling it.

Eventually someone says...

> "It works on my machine."

That single sentence inspired Aura Sync.

Our goal was simple:

> **Make embedded development collaborative, reproducible, and accessible entirely from the browser.**

Months before Arduino introduced its browser-first cloud development experience, our student team independently designed and built Aura Sync around these very ideas.

Later, seeing Arduino publicly engage with our project was an incredibly motivating milestone that validated the direction we had taken as student engineers exploring the future of embedded software development.

Aura Sync is the result of months of experimentation, cloud deployment, hardware integration, and collaborative engineering.

---

# 🎯 The Problem

Traditional embedded development introduces several challenges:

❌ Sharing `.ino` files manually

❌ Different library versions

❌ Different compiler versions

❌ Environment setup issues

❌ Impossible to collaborate simultaneously

❌ Hardware tied to one physical computer

❌ Difficult remote debugging

These limitations slow teams down significantly.

---

# ✅ Our Solution

Aura Sync transforms Arduino development into a collaborative cloud workflow.

Developers simply open a browser and instantly gain access to:

- Shared real-time editor
- AI code assistant
- Cloud compiler
- Remote hardware
- Live collaboration
- Shareable sessions

No local Arduino IDE.

No setup.

No dependency conflicts.

No "works on my machine."

---

# ✨ Key Features

## ⚡ Real-Time Collaborative Editing

Multiple developers can edit the same Arduino sketch simultaneously.

Every keystroke is synchronized across all connected users in **under 100ms** using persistent WebSocket connections.

---

## 🤖 AI-Powered Arduino Code Generation

Aura Sync integrates an AI-powered backend capable of generating Arduino C++ code directly inside the editor.

Developers can rapidly prototype firmware, generate boilerplate code, and accelerate development without leaving the IDE.

---

## 🐳 Sandboxed Cloud Compilation

Every compile request runs inside an isolated Docker container.

This provides:

- identical compiler environments
- secure execution
- reproducible builds
- isolated user sessions

---

## 🌍 Remote Hardware Access

One of Aura Sync's most unique capabilities is remote hardware interaction.

Arduino boards connected to one machine can be securely accessed from anywhere using a shareable session URL.

This allows distributed teams to upload firmware and interact with physical hardware remotely.

---

## 🔗 Shareable Sessions

Every collaborative project generates a unique session link.

Simply share the URL.

Anyone joining immediately becomes part of the live collaborative workspace.

---

## ☁️ Cloud Native Deployment

Aura Sync was designed for deployment on **Google Cloud Platform (Cloud Run)** using containerized services.

Although the current public deployment is paused due to cloud billing limitations, the complete cloud deployment pipeline remains part of the project.

---

# 🏗 System Architecture

```
                    ┌──────────────────────┐
                    │     Web Browser      │
                    │ Collaborative Editor │
                    └──────────┬───────────┘
                               │
                    Real-Time WebSockets
                               │
             ┌─────────────────▼──────────────────┐
             │        Node.js Collaboration       │
             │ Session Management + Sync Engine   │
             └───────────────┬────────────────────┘
                             │
          ┌──────────────────┴───────────────────┐
          │                                      │
          ▼                                      ▼

  AI Code Generation                     Docker Compiler

 (AI Server Endpoint)              Arduino CLI Sandbox

          │                                      │
          └──────────────────┬───────────────────┘
                             ▼

                  Compiled Arduino Binary

                             │
                             ▼

                   Remote Arduino Hardware

```

---

# 🔄 How Aura Sync Works

### Step 1

A user creates a collaborative session.

---

### Step 2

A shareable URL is generated.

---

### Step 3

Collaborators join the session.

---

### Step 4

Every code change is synchronized instantly using WebSockets.

---

### Step 5

Users can request AI-generated Arduino code.

---

### Step 6

The AI server generates optimized Arduino C++.

---

### Step 7

Compilation occurs inside a Docker sandbox using Arduino CLI.

---

### Step 8

Compiler logs are streamed back to every participant.

---

### Step 9

The compiled firmware can be uploaded to remotely connected Arduino hardware.

---

# 🚀 Why Aura Sync?

Aura Sync isn't simply another Arduino editor.

It combines several production-grade concepts into one platform:

- Real-time collaboration
- Cloud-native compilation
- AI-assisted programming
- Hardware virtualization
- Remote embedded development
- Browser-first workflow

The result is an end-to-end collaborative development experience for embedded systems.

# 🛠️ Technology Stack

Aura Sync combines modern web technologies, cloud infrastructure, containerization, and embedded tooling into a unified collaborative development platform.

| Technology | Purpose |
|------------|---------|
| **Node.js** | Backend server & WebSocket communication |
| **Express.js** | REST APIs |
| **WebSockets** | Real-time collaborative editing |
| **Docker** | Isolated compilation sandbox |
| **Arduino CLI** | Headless Arduino compilation |
| **Google Cloud Run** | Cloud deployment |
| **HTML / CSS / JavaScript** | Browser IDE |
| **Serial Communication** | Remote hardware access |
| **AI Server** | Dynamic Arduino C++ code generation |

---

# 📂 Project Structure

```text
Aura-Sync/
│
├── client/
│   ├── index.html
│   ├── editor.js
│   ├── websocket.js
│   ├── hardware.js
│   ├── ai.js
│   └── style.css
│
├── server/
│   ├── index.js
│   ├── compiler.js
│   ├── websocket.js
│   ├── sessions.js
│   ├── routes.js
│   └── config.js
│
├── docker/
│   ├── Dockerfile
│   └── compile.sh
│
├── ai-server/
│   ├── app.py
│   ├── prompts/
│   ├── models/
│   └── requirements.txt
│
├── hardware/
│   ├── serialBridge.js
│   └── tunnel.js
│
├── assets/
│
├── package.json
│
└── README.md
```

---

# ⚙️ Getting Started

## Prerequisites

Before running Aura Sync, ensure the following are installed:

- Node.js **18+**
- Docker
- Git
- Arduino CLI
- Google Cloud SDK *(optional for deployment)*

---

## Clone the Repository

```bash
git clone https://github.com/Srevarshan05/Aura-Sync.git

cd Aura-Sync
```

---

## Install Dependencies

```bash
npm install
```

---

## Build the Docker Compiler

```bash
docker build -t aura-sync-compiler ./docker
```

---

## Start the Development Server

```bash
npm start
```

The editor will now be available at

```
http://localhost:3000
```

---

# 🚀 Running Aura Sync

## Create a Session

Create a new collaborative workspace.

---

## Share the Link

A unique collaboration URL is generated.

Send it to your teammates.

---

## Collaborate

Every participant joins the same editor.

Typing, deleting, compiling and AI interactions occur live.

---

## Compile

Compilation happens inside Docker using Arduino CLI.

Results are streamed back to everyone.

---

## Upload

Compiled firmware can be flashed directly to connected Arduino hardware.

---

# 🔌 Hardware Integration

One of Aura Sync's most unique engineering achievements is remote hardware accessibility.

Instead of restricting Arduino boards to the machine physically connected over USB, Aura Sync virtualizes hardware access through the collaboration server.

This enables:

- Remote flashing
- Remote serial communication
- Distributed hardware testing
- Shared embedded development sessions

Developers can access connected hardware from anywhere using nothing more than the shared session link.

---

# 🌍 Remote Hardware Workflow

```text
Remote User

      │

      ▼

Collaborative Browser IDE

      │

      ▼

Node.js Collaboration Server

      │

      ▼

Serial Bridge

      │

      ▼

USB Connected Arduino

```

Every collaborator interacts with the same physical hardware regardless of geographical location.

---

# 🤖 AI Code Generation

Aura Sync includes an AI-powered programming assistant designed specifically for Arduino development.

The AI server accepts prompts from the collaborative editor and dynamically generates Arduino C++ code.

Generated code is inserted directly into the live editor, where every connected participant immediately sees the changes.

Typical use cases include:

- Sensor initialization
- LCD programming
- WiFi connectivity
- Servo control
- Robotics
- Motor drivers
- IoT applications
- Interrupt handling
- Embedded algorithms

The AI server is deployed independently and consumed through REST endpoints by the collaborative editor.

---

# 🐳 Docker Compilation Engine

Compiling arbitrary user code directly on the host machine introduces security and reproducibility concerns.

Aura Sync solves this using isolated Docker containers.

Every compilation request follows this lifecycle:

```
User Code

      │

      ▼

Temporary Workspace

      │

      ▼

Docker Container

      │

      ▼

Arduino CLI

      │

      ▼

Compiler Output

      │

      ▼

Browser
```

Advantages include:

- Secure execution
- Environment consistency
- Version locking
- User isolation
- Easy scalability

---

# ☁️ Google Cloud Deployment

Aura Sync was designed as a cloud-native application.

The production deployment targeted **Google Cloud Run**, enabling stateless containerized execution with automatic scaling.

Deployment pipeline:

```text
GitHub

     │

     ▼

Cloud Build

     │

     ▼

Docker Image

     │

     ▼

Cloud Run

     │

     ▼

Public IDE
```

---

## Deploy to Cloud Run

Authenticate:

```bash
gcloud auth login

gcloud config set project YOUR_PROJECT_ID
```

Build:

```bash
gcloud builds submit \
--tag gcr.io/YOUR_PROJECT_ID/aura-sync
```

Deploy:

```bash
gcloud run deploy aura-sync \
--image gcr.io/YOUR_PROJECT_ID/aura-sync \
--platform managed \
--region us-central1 \
--allow-unauthenticated
```

For uninterrupted WebSocket sessions:

```bash
--min-instances=1
```

is recommended.

---

# 🔒 Security Considerations

Aura Sync was engineered with security in mind.

### ✔ Docker Isolation

Every compilation occurs inside its own container.

---

### ✔ Session Isolation

Each collaborative workspace maintains an independent session state.

---

### ✔ Stateless Backend

The backend stores only active session information in memory.

---

### ✔ Hardware Gateway

Hardware communication is mediated through a controlled bridge rather than exposing USB devices directly.

---

### ✔ Cloud-Ready Design

Containerized services enable secure deployment behind managed cloud infrastructure.

---

# 📈 Scalability

Aura Sync was designed to scale horizontally.

Future deployments can support:

- Multiple collaboration servers
- Distributed WebSocket routing
- Container pools
- Dedicated AI inference servers
- Kubernetes deployment
- Load balancing
- Persistent storage
- Authentication services

The architecture intentionally separates:

- Collaboration
- AI generation
- Compilation
- Hardware communication

allowing each service to scale independently.

---
# 👥 Contributors

Aura Sync was built by a passionate team of student engineers, with each contributor owning a critical subsystem of the platform. Every major component was independently engineered and later integrated into one cohesive collaborative development environment.

---

## 👨‍💻 Sre Varshan

### Project Integration • Hardware Systems • Platform Engineering

Sre Varshan led the end-to-end integration of Aura Sync, bringing together the collaboration backend, AI services, cloud infrastructure, and physical hardware into one seamless platform.

### Responsibilities

- Integrated all independently developed subsystems into a unified platform
- Designed the complete system architecture and integration workflow
- Connected the collaborative editor with the AI code generation server
- Integrated the remote hardware communication layer
- Solved USB/Serial Port conflict issues for concurrent hardware access
- Implemented remote Arduino accessibility through shareable collaboration sessions
- Built the hardware communication workflow enabling users to control Arduino boards from anywhere in the world
- Managed deployment, testing, debugging and system validation
- Coordinated project execution and feature integration

> *Focused on transforming individual engineering components into a production-ready collaborative platform.*

---

## 👨‍💻 Nicholas Christo T

### Backend Engineering • Real-Time Collaboration Infrastructure

Nicholas designed and implemented the complete collaboration backend powering Aura Sync.

### Responsibilities

- Architected the real-time collaboration backend
- Implemented WebSocket communication
- Developed live collaborative editing synchronization
- Engineered multi-user session management
- Designed concurrent editing workflows
- Built the sandboxed code execution engine
- Implemented isolated compilation handling
- Developed backend APIs
- Optimized low-latency synchronization across connected users

His backend architecture enables multiple developers to work together on the same Arduino sketch with near real-time synchronization.

---

## 👨‍💻 Karthik KS

### AI Systems Engineering • Intelligent Code Generation

Karthik designed and developed the AI backend responsible for generating Arduino C++ code dynamically inside Aura Sync.

### Responsibilities

- Designed the AI server architecture
- Built the Arduino code generation pipeline
- Developed prompt processing logic
- Integrated AI inference workflows
- Deployed the AI server as an independent API endpoint
- Optimized generated Arduino C++ for embedded development
- Exposed APIs consumed by the collaborative editor

The AI server accelerates firmware development by generating Arduino-ready code directly inside the live collaborative editor.

---

# 🏆 Engineering Highlights

Aura Sync combines several complex systems into a single collaborative embedded development platform.

### Real-Time Collaboration

- Live collaborative editing
- Multi-user synchronization
- Low-latency WebSocket communication
- Shared compiler output

---

### AI-Assisted Programming

- Dynamic Arduino C++ generation
- AI-assisted embedded development
- Live insertion into collaborative sessions

---

### Cloud Compilation

- Docker sandboxing
- Arduino CLI automation
- Secure compilation environment
- Reproducible builds

---

### Remote Hardware

- Browser-to-Arduino communication
- Remote firmware upload
- Distributed hardware testing
- Shareable hardware sessions

---

### Cloud Native Infrastructure

- Containerized services
- Google Cloud deployment
- Stateless backend
- Horizontally scalable architecture

---

# 🚀 Why Aura Sync is Unique

Aura Sync is more than an online code editor.

It combines ideas typically found across several independent platforms into a single integrated experience.

✔ Collaborative IDE

✔ AI Programming Assistant

✔ Cloud Compiler

✔ Remote Hardware Access

✔ Browser IDE

✔ Real-Time Synchronization

✔ Containerized Execution

✔ Embedded Development Platform

Few student-built projects combine all of these capabilities into one cohesive system.

---

# 📈 Project Roadmap

| Status | Feature |
|---------|----------|
| ✅ | Real-time collaborative editing |
| ✅ | WebSocket synchronization |
| ✅ | AI-powered Arduino code generation |
| ✅ | Docker sandboxed compilation |
| ✅ | Remote hardware communication |
| ✅ | Shareable collaboration sessions |
| ✅ | Google Cloud deployment |
| 🔲 | Authentication & user accounts |
| 🔲 | Persistent project storage |
| 🔲 | Multi-file Arduino projects |
| 🔲 | Arduino library manager |
| 🔲 | Live serial monitor |
| 🔲 | Git integration |
| 🔲 | Syntax highlighting improvements |
| 🔲 | Board manager UI |
| 🔲 | Team workspaces |
| 🔲 | Kubernetes deployment |

---

# 💡 Inspiration

Aura Sync began with a simple question:

> **Why can't embedded systems engineers collaborate as easily as software developers?**

That question led to months of research, experimentation, cloud deployment, hardware integration, and countless iterations.

Our team independently explored browser-based collaborative embedded development several months before Arduino publicly introduced its own browser-focused cloud development experience.

While both projects were developed independently, it was incredibly motivating to later see Arduino engage with our work on social media. For our student team, that recognition validated the direction we had taken and encouraged us to continue building ambitious engineering projects.

---

# ❤️ Acknowledgements

Aura Sync represents the combined efforts of three student engineers, each contributing a specialized subsystem to create one unified platform.

Special thanks to:

- **Nicholas Christo T** — Backend Engineering & Real-Time Collaboration
- **Karthik KS** — AI Systems & Arduino Code Generation
- **Sre Varshan** — Platform Integration, Hardware Systems & Deployment

This project would not have been possible without the dedication, collaboration, and engineering contributions of every team member.

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve Aura Sync, feel free to:

- Fork the repository
- Create a feature branch
- Commit your changes
- Submit a Pull Request

Bug reports, feature suggestions, and improvements are always appreciated.

---

# 📜 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for additional information.

---

# ⭐ Support the Project

If you found Aura Sync interesting or useful:

- ⭐ Star this repository
- 🍴 Fork the project
- 💬 Share feedback
- 🤝 Contribute improvements

Every contribution helps make collaborative embedded development more accessible.

---

<div align="center">

# 🚀 Aura Sync

### Building the Future of Collaborative Embedded Development

*"From browser to hardware — together, in real time."*

---

**Made with ❤️ by**

**Sre Varshan**

**Nicholas Christo T**

**Karthik KS**

---

*SRM Institute of Science and Technology, Tiruchirappalli*

</div>
