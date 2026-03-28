# Copilot Workspace Instructions

## Mandatory Development Checklist


=======
- [ ] uv run ruff check .
- [ ] uv run pytest
- [ ] uv run uvicorn app.main:app --reload --port 8000

## Overview

Soc Ops is a FastAPI + Jinja2 + HTMX social bingo app. It uses server-side state, signed cookies, and HTMX partial updates.

## Key files

- app/main.py — routes and HTMX endpoints
- app/game_logic.py — bingo generation
- app/game_service.py — session state
- app/templates/ — Jinja2 views
- tests/ — API and game logic coverage

## Note

If uv is unavailable, use python -m uvicorn app.main:app --reload --port 8000.

