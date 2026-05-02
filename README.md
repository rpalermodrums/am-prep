# Interview Practice

A small Python practice repo for mock technical interviews using music-flavored problems.

The goal is still standard interview performance:

- clarify the problem
- state assumptions
- write a simple correct solution
- test edge cases
- discuss time and space complexity
- improve the approach when appropriate

## Quick Start

### Option 1: using Python `venv`

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pytest
```

### Option 2: using setup script

```bash
bash scripts/setup.sh
source .venv/bin/activate
bash scripts/test.sh
```

### Run one problem's tests

```bash
pytest tests/test_normalize_note_names.py
pytest tests/test_chord_at_timestamp.py
pytest tests/test_chord_symbol_parser.py
```

## Problems

| # | Problem | Difficulty | Main Pattern |
|---|---------|------------|--------------|
| 1 | Normalize Note Names | Easy | Hash map / parsing |
| 2 | Chord at Timestamp | Easy / Medium | Binary search |
| 3 | Chord Symbol Parser | Medium | String parsing |

Problem statements live in [`problems/`](./problems).

Starter implementations live in [`src/`](./src).

Tests live in [`tests/`](./tests).


## Interview Practice Rules

For mock interviews, the candidate should do these before coding:

1. Restate the problem.
2. Ask about edge cases.
3. Walk through the sample input.
4. Start with the clearest correct solution.
5. Only optimize after correctness is solid.

## Expected Function Names

The tests expect these functions:

```python
normalize_notes(notes: list[str]) -> list[int]
chord_at(changes: list[tuple[int, str]], time: int) -> str | None
parse_chord(symbol: str) -> dict
```

Edit only the files in `src/` unless you are intentionally modifying the test suite.
