## Repo purpose

This repository is a small ICS3U student workspace containing short Python exercise files (e.g. `day 1.py`). The projects are single-file exercises rather than a multi-module app.

## Quick start — how humans run this code

- This repo has no build system. Run individual exercises with the system Python:

  python3 'day 1.py'

- Note: some filenames contain spaces (e.g. `day 1.py`). Quote paths when running from a POSIX shell.

## Big picture

- Single-file Python exercises. Files mostly contain short imperative scripts that print results. There are no services, frameworks, or external dependencies recorded in this repository.
- The "why": these are classroom examples and small practice programs. Changes should be minimal and preserve the educational intent (clear, readable single-file examples).

## Project-specific patterns you should preserve

- Keep examples short and focused. Most files demonstrate a single concept (printing, arithmetic). Avoid turning examples into libraries unless instructed.
- Preserve existing naming and simple formatting (spaces in filenames are permitted but require quoting in shell commands).
- The code uses numeric literal readability (underscores in large integers) — follow that style when editing numbers (e.g. use `1_000_000` instead of `1000000`).

## What to do when editing

- Make minimal, backward-compatible changes. If you add a file, put it at the repository root or in a clearly named subfolder (e.g. `exercises/`).
- Do not rename existing exercise files without confirming with the repo owner. If you must rename, keep a copy and update README with migration notes.
- If you introduce imports or external packages, also add a `requirements.txt` and update the README with run instructions.

## Examples from this repo (to show patterns)

- `day 1.py` — short script printing values and arithmetic; uses underscores in numeric literals:

  print(1_000_000)
  print(1_234_005)
  print(7 + 5)

Use similar short, self-contained examples when adding files.

## Testing / debugging guidance

- There are no automated tests. Use quick manual checks by running the script with `python3 'filename.py'` and use `python3 -m pdb 'filename.py'` when needing an interactive debugger.

## When to ask the user for clarification

- Before introducing project-level changes: adding a test harness, modifying filenames en masse, changing directory layout, or adding external dependencies.

## Where to look

- Root: `day 1.py` — canonical example of code style and purpose.
- `README.md` — short project description (update if you change repo scope).

If anything in this file is unclear or you want more detailed rules (naming, folder layout, test convention), tell me which area to expand and I will update this guidance.
