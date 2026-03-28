<div align="center">

# 🎲 Soc Ops

### _Social Bingo for In-Person Mixers — Powered by GitHub Copilot Agent Mode_

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![HTMX](https://img.shields.io/badge/HTMX-1.9-3D72D7?style=flat-square&logo=htmx&logoColor=white)](https://htmx.org)
[![uv](https://img.shields.io/badge/uv-package%20manager-DE5FE9?style=flat-square)](https://docs.astral.sh/uv/)

**Find people who match the prompts. Mark your squares. Get five in a row. Win.**

[🚀 Start the Lab](#-getting-started) · [📚 Lab Guide](#-lab-guide) · [🛠 Tech Stack](#️-tech-stack) · [🤝 Contributing](CONTRIBUTING.md)

</div>

---

## 🎯 What Is This?

**Soc Ops** is a real, working Social Bingo web app — and the canvas for a hands-on GitHub Copilot workshop.

You'll use **VS Code Agent Mode** with GitHub Copilot to transform this app from a plain bingo board into something creative and uniquely yours: new UI themes, custom quiz categories, and new gameplay features — all built with AI-assisted development workflows.

> _No slides. No lecture. Just you, your editor, and an AI pair-programmer._

---

## 🧪 What You'll Build & Learn

| # | Skill | What You'll Do |
|---|-------|----------------|
| 🧠 | **Context Engineering** | Teach Copilot about your codebase using instructions files |
| 🎨 | **Design-First Development** | Let agents iterate on UI while you guide the creative vision |
| 🤖 | **Custom Agents** | Build a Quiz Master agent that generates themed bingo prompts |
| 🔁 | **Multi-Agent TDD** | Ship new features using Red → Green → Refactor agent workflows |

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI + Python 3.13 |
| **Frontend** | Jinja2 templates + HTMX |
| **State** | Server-side sessions via signed cookies |
| **Packaging** | [uv](https://docs.astral.sh/uv/) |
| **Tests** | pytest |

---

## 📚 Lab Guide

Work through the parts in order — each one builds on the last.

| Part | Title | Time | Description |
|------|-------|------|-------------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Overview & Checklist | — | Prerequisites and environment setup |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Setup & Context Engineering | 15 min | Clone, configure, and teach the AI about your project |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Design-First Frontend | 15 min | Redesign the UI with creative Copilot-driven themes |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Custom Quiz Master | 10 min | Create your own quiz themes using a custom agent |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Multi-Agent Development | 20 min | Build new gameplay features with TDD + design agents |

> 📝 Prefer offline reading? All lab guides live in the [`workshop/`](workshop/) folder.

---

## 🚀 Getting Started

### Prerequisites

- [ ] **VS Code v1.107+** (check for updates before starting)
- [ ] **GitHub Copilot** — Free, Pro, Business, or Enterprise
- [ ] **Git** installed
- [ ] **Python 3.13** and **[uv](https://docs.astral.sh/uv/)** installed

> 💡 Skip the setup entirely — use the **DevContainer** for a pre-configured environment!

### Quick Start

```bash
# 1. Use this template to create your own repo on GitHub
# 2. Clone your repo locally (or open in a Codespace)
git clone https://github.com/<your-username>/copilot-dev-days-agent-lab-python
cd copilot-dev-days-agent-lab-python

# 3. Install dependencies and run
uv sync
uv run uvicorn app.main:app --reload --port 8000
```

Then open **[http://localhost:8000](http://localhost:8000)** and start playing!

Head to **[Part 00: Overview](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview)** for the full setup walkthrough.

---

## 🗂 Project Structure

```
app/
├── main.py          # Routes and HTMX endpoints
├── game_logic.py    # Bingo card generation
├── game_service.py  # Session state management
├── templates/       # Jinja2 HTML views
└── static/          # CSS and assets
tests/               # pytest test suite
workshop/            # Offline lab guide (Markdown)
```

---

## 💡 Pro Tips

1. **Keep the browser open** — Watch live updates as Copilot edits your code
2. **Commit often** — Save working states before big agent runs
3. **Use Chat Checkpoints** — Instantly undo unexpected changes
4. **Iterate on plans** — Ask Copilot to refine its plan 2× before executing

---

<div align="center">

Made with ☕ and 🤖 for the GitHub Copilot Dev Days workshop.

[Code of Conduct](CODE_OF_CONDUCT.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)

</div>
