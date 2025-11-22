# Copilot Instructions

This file contains concise instructions for GitHub Copilot and Copilot Chat
when suggesting code, documentation, or repository changes for `python-uv`.

Scope

- Applies to suggestions that touch `tools/`, `docs/`, tests in `tests/`, and
  repository configuration files.

Primary Rules

- **Follow project conventions**: Use Python 3.14 typing, explicit type
  hints where helpful, and Ruff formatting (line length 88).
- **Prefer existing utilities**: Reuse `tools.logger`, `tools.config`, and
  `tools.tracer` rather than adding new cross-cutting utilities.
- **Use repo tooling**: Recommend `uv` and `nox` for package and task
  management (examples: `uv sync`, `uv run nox -s test`).
- **Tests required**: When adding or changing behavior, include or update
  pytest tests under `tests/` using the `test__*.py` naming pattern.
- **Do not change CI**: Avoid edits to `.github/workflows/` unless explicitly
  requested.

Coding Style & Quality

- **Formatting**: Suggestions should be Ruff-friendly. Prefer code that passes
  `uv run ruff check . --fix`.
- **Type checking**: Ensure Pyright passes for the `tools/` package.
- **Small, focused changes**: Keep diffs minimal; avoid unrelated edits.
- **Include imports and examples**: Show required imports and a 1–3 line
  usage snippet in suggestions.

Documentation

- When adding features, add or update a short guide in `docs/` under the
  appropriate section (`docs/guides/`, `docs/configurations/`, etc.).
- Examples in docs should use the repository's commands (prefer `uv run`).

Safety & Constraints

- **No secrets**: Never add secrets, credentials, or private keys to code or
  docs — use environment variables (`.env.local`) for sensitive values.
- **API compatibility**: Avoid breaking public APIs in `tools/` without a
  migration note and tests.

PR / Multi-file Changes

- Provide a one-line summary and a short rationale (1–2 lines).
- Include tests and a minimal usage example.
- Show the code snippet or diff and list files changed.

Suggested Response Format

1. One-line summary.
2. One-sentence rationale.
3. Code block (with imports) and a short usage example.
4. Tests to add/update (path to test file).

Local validation commands

```pwsh
uv sync
uv run ruff check . --fix
uv run nox -s test
```

If you want stricter conventions (stricter typing, different line length,
or different test policies), state them explicitly at the top of this file.
