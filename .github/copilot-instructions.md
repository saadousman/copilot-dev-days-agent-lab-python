# Copilot Workspace Instructions

## Mandatory Development Checklist

- [ ] `uv run ruff check .`
- [ ] `uv run pytest`
- [ ] `uv run uvicorn app.main:app --reload --port 8000`

Soc Ops is a social bingo app built with Python, FastAPI, Jinja2, and HTMX.

Key files:
- `app/main.py` — routes + HTMX endpoints
- `app/game_logic.py` — board generation
- `app/game_service.py` — session state
- `app/templates/` — views
- `tests/` — coverage

Do not use VS Code Simple Browser. If `uv` is unavailable, use:

```bash
python -m uvicorn app.main:app --reload --port 8000
```
