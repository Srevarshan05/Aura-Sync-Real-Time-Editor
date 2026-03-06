<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0D47A1,00B0FF&height=200&section=header&text=Aura-Sync&fontSize=62&fontColor=ffffff&fontAlignY=36&desc=Real-Time%20Collaborative%20Cloud%20IDE%20for%20Arduino%20Hardware&descSize=14&descAlignY=58" width="100%"/>

<br/>

[![Node.js](https://img.shields.io/badge/Node.js-Runtime-339933?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org)
[![Docker](https://img.shields.io/badge/Docker-Sandboxed_Compilation-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![WebSockets](https://img.shields.io/badge/WebSockets-Sub_100ms_Sync-00B0FF?style=for-the-badge)](.)
[![GCP](https://img.shields.io/badge/GCP-Cloud_Deployed-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)](https://cloud.google.com)
[![Arduino](https://img.shields.io/badge/Arduino_CLI-Cloud_Compilation-00979D?style=for-the-badge&logo=arduino&logoColor=white)](https://arduino.cc)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

<br/>

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  Real-time collaborative coding for Arduino hardware  ·  No local IDE       ║
║  Sandboxed cloud compilation  ·  Sub-100ms WebSocket sync                   ║
║  Built before Arduino officially launched its own cloud IDE                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

</div>

---

## The Idea — Before Arduino Did It

> In 2024, Arduino launched **Arduino Cloud Editor** — a browser-based IDE for writing and managing Arduino sketches online. Aura-Sync was already building this.

The difference: Aura-Sync isn't just a cloud editor. It's a **real-time collaborative environment** — think Google Docs, but for firmware engineers. Multiple developers can write, compile, and flash Arduino code simultaneously, from different locations, on the same project, with sub-100ms synchronisation.

The problem it solves is real and unsolved in the embedded world:

```
┌──────────────────────────────────────────────────────────────────────┐
│  EMBEDDED TEAMS TODAY                                                │
│  ──────────────────────────────────────────────────────────────────  │
│  "Let me send you the .ino file over WhatsApp"                       │
│  "Which version are you on? I made changes last night"               │
│  "My Arduino IDE version throws a different error than yours"        │
│  "I can't reproduce the bug — it only happens on your machine"       │
│                                                                      │
│  AURA-SYNC                                                           │
│  ──────────────────────────────────────────────────────────────────  │
│  One shared session. One cloud compiler. One live environment.       │
│  Everyone sees the same code, the same errors, in real time.         │
└──────────────────────────────────────────────────────────────────────┘
```

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AURA-SYNC — SYSTEM ARCHITECTURE                      │
│                                                                             │
│   CLIENT A  ──┐                                                             │
│   (Browser)   │                                                             │
│               ├──► [WebSocket Server]  ──────────────────────────────────┐  │
│   CLIENT B  ──┤    Node.js             Sub-100ms                         │  │
│   (Browser)   │    Real-time sync      bi-directional                    │  │
│               │    broadcast           sync                              │  │
│   CLIENT C  ──┘                          │                               │  │
│                                          ▼                               │  │
│                              ┌───────────────────────┐                  │  │
│                              │   Docker Container    │                  │  │
│                              │   Sandboxed           │                  │  │
│                              │   Compilation         │                  │  │
│                              │   Environment         │                  │  │
│                              └───────────┬───────────┘                  │  │
│                                          │                               │  │
│                                          ▼                               │  │
│                              ┌───────────────────────┐                  │  │
│                              │   Arduino CLI          │                  │  │
│                              │   · Compile sketch     │                  │  │
│                              │   · Validate libs      │                  │  │
│                              │   · Generate binary    │                  │  │
│                              └───────────┬───────────┘                  │  │
│                                          │                               │  │
│                                          ▼                               │  │
│                              ┌───────────────────────┐                  │  │
│                              │   Flash / Download    │                  │  │
│                              │   Remote hardware     │                  │  │
│                              │   via shareable link  │                  │  │
│                              └───────────────────────┘                  │  │
│                                                                          │  │
│   ┌──────────────────────────────────────────────────────────────────┐  │  │
│   │   GCP  (Production)  →  currently running locally                │◄─┘  │
│   └──────────────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## How It Works — End to End

```bash
aura-sync:~$ explain --how-it-works
```

**1. Session Creation**
A user opens Aura-Sync in the browser and creates a new sketch session. A unique shareable link is generated. Anyone with the link joins the same live editor.

**2. Real-Time Sync**
Every keystroke is broadcast via WebSockets to all connected clients. Changes appear on every collaborator's screen in under 100ms — no polling, no refresh, no manual saves.

**3. Cloud Compilation**
When a user hits **Compile**, the sketch is sent to a sandboxed Docker container on the server. Arduino CLI inside the container compiles the code in an isolated environment — no local Arduino IDE required on any client machine.

**4. Error Feedback**
Compilation errors are returned in real time to all connected clients. Everyone sees the same error output simultaneously — no "works on my machine" situations.

**5. Flash / Download**
The compiled binary is available for direct flashing to connected Arduino hardware via a browser-accessible endpoint, or for download and manual flash.

---

## Why Each Technology Was Chosen

```
┌──────────────────┬─────────────────────────────────────────────────────────┐
│  Technology      │  Why                                                    │
├──────────────────┼─────────────────────────────────────────────────────────┤
│  WebSockets      │  Persistent bi-directional connection — HTTP polling    │
│                  │  can't achieve sub-100ms sync for collaborative editing  │
├──────────────────┼─────────────────────────────────────────────────────────┤
│  Docker          │  Each compilation runs in an isolated container —       │
│                  │  prevents library conflicts, version mismatches, and    │
│                  │  malicious sketch execution on the host system          │
├──────────────────┼─────────────────────────────────────────────────────────┤
│  Arduino CLI     │  Headless compilation without Arduino IDE —             │
│                  │  scriptable, version-pinnable, CI/CD compatible         │
├──────────────────┼─────────────────────────────────────────────────────────┤
│  Node.js         │  Event-driven, non-blocking I/O — handles hundreds of   │
│                  │  simultaneous WebSocket connections without threading   │
├──────────────────┼─────────────────────────────────────────────────────────┤
│  GCP             │  Containerised deployment — scalable, globally          │
│                  │  distributed, paired with Cloud Run for serverless      │
└──────────────────┴─────────────────────────────────────────────────────────┘
```

---

## Features

**Real-Time Collaborative Editor**
Multiple engineers editing the same `.ino` sketch simultaneously. Cursors, changes, and errors visible to all participants in real time.

**Sandboxed Cloud Compilation**
Sketches compile inside Docker — no environment setup, no version conflicts, no local Arduino IDE needed. The compiler is always consistent.

**Shareable Session Links**
One link. Anyone clicks it, joins the live session instantly. No accounts required to collaborate.

**Remote Hardware Access**
Flash compiled firmware to Arduino hardware connected remotely. Teams debug physical devices without being in the same room.

**Sub-100ms Sync Latency**
WebSocket architecture keeps all clients synchronised at under 100ms — fast enough to feel like a local editor.

---

## Tech Stack

```bash
aura-sync:~$ cat package.json --tech-only
```

```json
{
  "runtime":     "Node.js",
  "realtime":    "WebSockets (ws / socket.io)",
  "compilation": "Arduino CLI — inside Docker container",
  "container":   "Docker — sandboxed build environment",
  "cloud":       "Google Cloud Platform (GCP)",
  "frontend":    "HTML + CSS + JS — browser-based editor",
  "deployment":  "GCP Cloud Run (production) → localhost (current)"
}
```

---

## Quickstart — Run Locally

### Prerequisites

- [Node.js](https://nodejs.org) v18+
- [Docker](https://docker.com) installed and running
- [Arduino CLI](https://arduino.github.io/arduino-cli/) (or handled inside container)

### 1. Clone

```bash
git clone https://github.com/Srevarshan05/Aura-Sync.git
cd Aura-Sync
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Build the Docker Compilation Container

```bash
docker build -t aura-sync-compiler ./docker
```

### 4. Start the Server

```bash
npm start
# → WebSocket server running on ws://localhost:3000
# → Browser editor at   http://localhost:3000
```

### 5. Open a Session

```
1. Open http://localhost:3000 in your browser
2. Create a new sketch session
3. Copy the shareable link
4. Open it in a second browser tab (or send to a collaborator)
5. Both editors are now live-synced
```

---

## Project Structure

```
Aura-Sync/
│
├── server/
│   ├── index.js              # WebSocket server + session management
│   ├── compiler.js           # Arduino CLI integration + Docker spawn
│   └── sessions.js           # Live session state management
│
├── docker/
│   └── Dockerfile            # Sandboxed Arduino CLI build environment
│
├── client/
│   ├── index.html            # Browser-based collaborative editor
│   ├── editor.js             # WebSocket client + real-time sync logic
│   └── style.css             # Editor UI
│
├── .gcp/
│   └── cloudbuild.yaml       # GCP Cloud Run deployment config
│
├── package.json
└── README.md
```

---

## Deployment

### Current Status

```
[✓]  Local deployment  —  fully functional on localhost
[ ]  GCP Cloud Run     —  previously deployed, paused due to billing
```

### Re-deploy to GCP

```bash
# Authenticate
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Build and push container
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/aura-sync

# Deploy to Cloud Run
gcloud run deploy aura-sync \
  --image gcr.io/YOUR_PROJECT_ID/aura-sync \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

> **Note:** Cloud Run scales to zero when idle — use `--min-instances=1` if you need persistent WebSocket connections without cold starts.

---

## Roadmap

```bash
aura-sync:~$ cat roadmap.txt
```

```
[✓]  Real-time collaborative editing via WebSockets
[✓]  Sandboxed cloud compilation via Docker + Arduino CLI
[✓]  Shareable session links
[✓]  GCP Cloud Run deployment
[✓]  Remote hardware flash via compiled binary
[ ]  Syntax highlighting + Arduino-aware autocomplete
[ ]  Multi-file sketch support (libraries, headers)
[ ]  Git integration — version control inside the IDE
[ ]  Live serial monitor — read hardware output in browser
[ ]  User authentication + persistent project storage
[ ]  Board manager UI — select target board from browser
[ ]  Re-deploy to GCP with cost-optimised Cloud Run config
```

---

## The Bigger Picture

Aura-Sync was conceived and built as a **pre-final year student project** — before Arduino formally entered the cloud IDE space.

The architectural decisions — sandboxed Docker compilation, WebSocket-first sync, stateless cloud deployment — mirror exactly what production embedded dev platforms now use. This wasn't a tutorial follow-along. It was an original system built from first principles, deployed to production infrastructure, and validated by real usage.

> *"The best way to predict the future is to build it before someone else does."*

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0D47A1,00B0FF&height=120&section=footer&text=Built%20before%20Arduino%20did%20it.&fontSize=16&fontColor=ffffff&fontAlignY=65" width="100%"/>

**[Sre Varshan](https://github.com/Srevarshan05)** · AI/ML Engineer · SRM Trichy · 2027

</div>
