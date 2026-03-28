# 🎯 Soc Ops — VS Code GitHub Copilot Agent Lab

> **Social Bingo for in-person mixers** — and a hands-on workshop to master GitHub Copilot's Agent Mode.

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![HTMX](https://img.shields.io/badge/HTMX-powered-3D72D7)](https://htmx.org/)
[![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Agent%20Lab-181717?logo=github)](https://github.com/features/copilot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ What is Soc Ops?

**Soc Ops** is a real, working Social Bingo web app — find people who match the prompts on your card and get five in a row to win! But it's also the foundation for something bigger:

This repository is a **~1-hour hands-on workshop** where you'll use **VS Code's Agent Mode** with **GitHub Copilot** to transform this starter app into something truly your own — through agentic AI workflows, creative UI design, custom quiz themes, and test-driven feature development.

```
🎲  Play Social Bingo at your next event
🤖  Learn GitHub Copilot Agent Mode in depth
🎨  Redesign the UI with AI-driven themes
🧪  Build new features using TDD agents
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) — async Python web framework |
| **Templating** | [Jinja2](https://jinja.palletsprojects.com/) — server-side HTML rendering |
| **Interactivity** | [HTMX](https://htmx.org/) — hypermedia-driven UI updates |
| **State** | Signed cookies + server-side session store |
| **Package Manager** | [uv](https://docs.astral.sh/uv/) — fast Python package manager |
| **Linting/Testing** | [Ruff](https://docs.astral.sh/ruff/) + [pytest](https://pytest.org/) |

---

## 🎯 What You'll Learn

| # | Skill | Description |
|---|-------|-------------|
| 1 | **Context Engineering** | Teach the AI about your codebase using instructions files |
| 2 | **Agentic Primitives** | Use Copilot CLI sessions, cloud agents, and custom workflows |
| 3 | **Design-First Development** | Let AI iterate on UI while you steer the creative vision |
| 4 | **Test-Driven Development** | Use TDD agents to build reliable features with confidence |

---

## 📚 Lab Guide

| Part | Title | Time |
|------|-------|------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Overview & Checklist | — |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Setup & Context Engineering | 15 min |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Design-First Frontend | 15 min |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Custom Quiz Master | 10 min |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Multi-Agent Development | 20 min |

> 📝 Prefer offline reading? All lab guides are available in the [`workshop/`](workshop/) folder.

---

## ✅ Prerequisites

Before you begin, make sure you have:

- [ ] **VS Code v1.107+** — no pending updates
- [ ] **GitHub Copilot** — Free, Pro, Business, or Enterprise
- [ ] **Git** installed
- [ ] **Python 3.13** and **uv** installed
- [ ] Copilot Chat panel open with Agent Mode ready

> ⚠️ **Free-tier Copilot users:** Cloud Agents are not available on free-tier plans. The workshop provides alternative instructions wherever Cloud Agents are used.

> 💡 **Tip:** Use the included [DevContainer](.devcontainer/) for a fully pre-configured environment — no local setup needed!

---

## 🚀 Quick Start

```bash
# 1. Create your own repo from this template (click "Use this template" above)
# 2. Clone your repo locally, or open in Codespaces:
#    Code → Codespaces → Create codespace on main

# 3. Install dependencies
uv sync

# 4. Run the app
uv run uvicorn app.main:app --reload --port 8000
```

Then open http://localhost:8000 in your browser and start the lab!

> 🤖 Once in VS Code, run `/setup` in the Copilot Chat panel to get started with the guided lab experience.

---

## 📁 Project Structure

```
soc-ops/
├── app/
│   ├── main.py          # FastAPI routes & HTMX endpoints
│   ├── game_logic.py    # Bingo board generation & win detection
│   ├── game_service.py  # Session state management
│   ├── models.py        # Pydantic data models
│   ├── data.py          # Bingo question prompts
│   ├── templates/       # Jinja2 HTML templates
│   └── static/          # CSS & frontend assets
├── tests/               # pytest test suite
├── workshop/            # Offline lab guide docs
└── .github/             # Copilot instructions & custom agents
```

---

## 💡 Pro Tips

1. **Keep the browser open** — watch live updates as the AI makes changes
2. **Commit often** — save working states so you can always roll back
3. **Use Checkpoints** — leverage Copilot's Undo feature to revert unexpected changes
4. **Iterate on plans** — ask Copilot to revise its plan 2+ times before implementing
5. **📌 Pin the lab guide** — keep it visible in a split pane while you work

---

## 🔗 Resources

- 📖 [Lab Guide (online)](https://copilot-dev-days.github.io/agent-lab-python/docs/)
- 🎥 [VS Code on YouTube](https://www.youtube.com/code)
- 📚 [GitHub Copilot Docs](https://code.visualstudio.com/docs/copilot/overview)
- ⭐ [Awesome Copilot](https://github.com/github/awesome-copilot)

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

---

<div align="center">

Built with ❤️ for the **GitHub Copilot Dev Days** workshop series.

</div>
