<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0D47A1,00B0FF&height=200&section=header&text=Aura-Sync&fontSize=62&fontColor=ffffff&fontAlignY=36&desc=Real-Time%20Collaborative%20Cloud%20IDE%20for%20Arduino%20Hardware&descSize=14&descAlignY=58" width="100%"/>

<br/>

[![Node.js](https://img.shields.io/badge/Node.js-Runtime-339933?style=flat-square&logo=node.js&logoColor=white)](https://nodejs.org)
[![Docker](https://img.shields.io/badge/Docker-Sandboxed_Compilation-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![WebSockets](https://img.shields.io/badge/WebSockets-Sub_100ms_Sync-00B0FF?style=flat-square)](.)
[![GCP](https://img.shields.io/badge/GCP-Cloud_Deployed-4285F4?style=flat-square&logo=googlecloud&logoColor=white)](https://cloud.google.com)
[![Arduino CLI](https://img.shields.io/badge/Arduino_CLI-Cloud_Compilation-00979D?style=flat-square&logo=arduino&logoColor=white)](https://arduino.cc)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

</div>

---

## Overview

**Aura-Sync** is a real-time collaborative cloud IDE built specifically for Arduino hardware development. Multiple engineers can write, compile, and flash Arduino sketches simultaneously from any browser — with no local IDE installation, no environment setup, and no version conflicts.

Think Google Docs, but for embedded systems engineers.

The project was conceived and built independently — before Arduino officially launched its own cloud editor. Aura-Sync takes the concept further: it is not just a cloud editor, it is a **live collaborative environment** where every keystroke, compilation result, and error is synchronised across all connected participants in under 100ms.

The system was deployed to **Google Cloud Platform (GCP)** and is currently running locally due to cloud billing constraints.

---

## The Problem

Embedded development teams share a set of friction points that no existing tool properly solves:

- Sketches are passed around as `.ino` files over chat, email, or shared drives
- Environment mismatches between team members cause bugs that are impossible to reproduce
- There is no native way for two engineers to work on the same firmware simultaneously
- Reviewing or debugging a colleague's Arduino code requires setting up a matching local environment

Aura-Sync eliminates all of these by moving the entire development environment to the cloud and adding real-time collaboration on top.

---

## System Architecture

<div align="center">

| Layer | Component | Role |
|---|---|---|
| **Client** | Browser-based editor | Code input, error display, session UI |
| **Sync** | WebSocket server (Node.js) | Sub-100ms bi-directional state broadcast |
| **Compilation** | Docker container + Arduino CLI | Sandboxed, consistent cloud compilation |
| **Cloud** | Google Cloud Platform | Scalable deployment via Cloud Run |
| **Hardware** | Arduino (remote) | Target device for compiled firmware |

</div>

### Data Flow

When a user writes code and triggers a compile, the following happens:

1. The sketch is broadcast to all connected clients via WebSocket
2. The server spawns a sandboxed Docker container
3. Arduino CLI inside the container compiles the sketch against the selected board target
4. Compilation output — success or errors — is returned to all connected clients simultaneously
5. On success, the compiled binary is available for download or direct flash to connected hardware

---

## Key Features

**Real-Time Collaborative Editing**
Multiple engineers work on the same sketch at the same time. Every change is reflected across all sessions in under 100ms — no manual syncing, no file sharing.

**Sandboxed Cloud Compilation**
Every compilation runs inside an isolated Docker container. This eliminates local environment dependencies, ensures consistent compiler behaviour across all users, and prevents untrusted sketch code from affecting the host system.

**No Local IDE Required**
The entire development workflow — writing, compiling, error checking, and flashing — runs in the browser. Team members need nothing installed on their machines.

**Shareable Session Links**
Each project session generates a unique link. Any collaborator with the link joins the live environment instantly.

**Remote Hardware Access**
Compiled binaries can be flashed to Arduino hardware connected remotely, enabling distributed hardware debugging without physical co-location.

**GCP-Ready Deployment**
The system was architected for cloud deployment from day one, with containerised services and a stateless backend that scales horizontally on Cloud Run.

---

## Why These Technologies

**WebSockets over HTTP**
Collaborative editing requires persistent, low-latency bi-directional communication. HTTP polling introduces noticeable lag and unnecessary server load. WebSockets maintain a persistent connection and push changes the moment they occur — essential for a sub-100ms sync target.

**Docker for compilation**
Compiling user-submitted Arduino code on a shared server without isolation is a security risk. Docker containers sandbox each compilation job, prevent library version conflicts between users, and ensure every team member compiles against an identical environment regardless of what they have installed locally.

**Arduino CLI over Arduino IDE**
Arduino CLI is headless, scriptable, and version-pinnable — making it ideal for automated server-side compilation. It supports all Arduino board targets, can manage libraries programmatically, and integrates cleanly into Docker-based CI pipelines.

**Node.js for the server**
Node.js is event-driven and non-blocking, which makes it well-suited for managing hundreds of concurrent WebSocket connections without the overhead of threading. Its async model handles real-time broadcast efficiently at scale.

---

## Tech Stack

| Technology | Version | Purpose |
|---|---|---|
| Node.js | 18+ | Server runtime |
| WebSockets | — | Real-time collaborative sync |
| Docker | Latest | Sandboxed compilation environment |
| Arduino CLI | Latest stable | Headless cloud sketch compilation |
| Google Cloud Platform | — | Production deployment (Cloud Run) |
| HTML / CSS / JavaScript | — | Browser-based editor interface |

---

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org) v18 or higher
- [Docker](https://docker.com) installed and running
- Git

### Installation

**Clone the repository:**

```bash
git clone https://github.com/Srevarshan05/Aura-Sync.git
cd Aura-Sync
```

**Install dependencies:**

```bash
npm install
```

**Build the Docker compilation container:**

```bash
docker build -t aura-sync-compiler ./docker
```

**Start the server:**

```bash
npm start
```

The editor will be available at `http://localhost:3000`.

### Starting a Collaborative Session

1. Open `http://localhost:3000` in your browser
2. Create a new sketch session
3. Copy the generated shareable session link
4. Share it with collaborators — they join the live session instantly
5. Write code, compile, and see results in real time across all connected clients

---

## Project Structure

```
Aura-Sync/
│
├── server/
│   ├── index.js              # WebSocket server and session management
│   ├── compiler.js           # Arduino CLI integration and Docker orchestration
│   └── sessions.js           # Live session state
│
├── docker/
│   └── Dockerfile            # Sandboxed Arduino CLI compilation environment
│
├── client/
│   ├── index.html            # Browser editor
│   ├── editor.js             # WebSocket client and real-time sync
│   └── style.css             # Editor interface styles
│
├── .gcp/
│   └── cloudbuild.yaml       # GCP Cloud Run deployment configuration
│
├── package.json
└── README.md
```

---

## Cloud Deployment

Aura-Sync was designed for and deployed to **Google Cloud Platform** using Cloud Run. It is currently running locally due to billing constraints on the GCP project.

### Re-deploying to GCP

```bash
# Authenticate with GCP
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Build and push the container image
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/aura-sync

# Deploy to Cloud Run
gcloud run deploy aura-sync \
  --image gcr.io/YOUR_PROJECT_ID/aura-sync \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

> For persistent WebSocket connections without cold-start interruptions, set `--min-instances=1` in the Cloud Run configuration.

---

## Roadmap

| Status | Feature |
|---|---|
| ✅ Done | Real-time collaborative editing via WebSockets |
| ✅ Done | Sandboxed cloud compilation via Docker + Arduino CLI |
| ✅ Done | Shareable session links |
| ✅ Done | GCP Cloud Run deployment |
| ✅ Done | Remote hardware flash via compiled binary |
| 🔲 Planned | Syntax highlighting and Arduino-aware autocomplete |
| 🔲 Planned | Multi-file sketch support (libraries, headers) |
| 🔲 Planned | Git integration inside the IDE |
| 🔲 Planned | Live serial monitor — read hardware output in browser |
| 🔲 Planned | Board manager UI — select target board from browser |
| 🔲 Planned | User authentication and persistent project storage |
| 🔲 Planned | Re-deploy to GCP with cost-optimised Cloud Run configuration |

---

## Context

Aura-Sync was built as an independent project by a pre-final year student — conceived and developed before Arduino formally entered the cloud IDE space. The architectural decisions made here — sandboxed compilation, WebSocket-first synchronisation, containerised cloud deployment — reflect the same design choices that production embedded development platforms now use commercially.

This is not a demo or an academic exercise. It is a working system that was deployed to production infrastructure, served real sessions, and demonstrated that collaborative embedded development in the browser is both technically viable and genuinely useful.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0D47A1,00B0FF&height=120&section=footer&text=Built%20before%20Arduino%20did%20it.&fontSize=16&fontColor=ffffff&fontAlignY=65" width="100%"/>

**[Sre Varshan](https://github.com/Srevarshan05)** · AI/ML Engineer · SRM Trichy · 2027

</div>
