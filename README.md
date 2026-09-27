# Python Problem-Solving Patterns

[![quality](https://github.com/Adeen1607/python-code/actions/workflows/quality.yml/badge.svg)](https://github.com/Adeen1607/python-code/actions/workflows/quality.yml)

A tested collection of Python implementations for common data-structure and algorithm patterns. The repository began as a set of introductory exercises and now documents the progression from small scripts to reusable, typed, and continuously tested modules.

## What this repository demonstrates

- clear function contracts and edge-case handling;
- time and auxiliary-space complexity analysis;
- hash maps, sliding windows, monotonic queues, and binary search;
- breadth-first graph traversal and shortest paths;
- dynamic programming and sequence optimization;
- pytest coverage and automated checks on Python 3.11 and 3.12.

## Implemented problems

| Module | Problems | Core techniques |
| --- | --- | --- |
| `arrays.py` | two sum, maximum subarray, interval merging, sliding-window maximum | hash map, Kadane's algorithm, sorting, monotonic deque |
| `strings.py` | anagram grouping, longest unique substring | frequency grouping, sliding window |
| `search.py` | lower bound, first-match binary search | half-open intervals, logarithmic search |
| `graphs.py` | shortest unweighted path | breadth-first search, parent reconstruction |
| `dynamic_programming.py` | minimum coin change, longest increasing subsequence | tabulation, patience-sorting tails |

## Repository structure

```text
src/problem_solving/      Importable implementations
tests/                    Behaviour and edge-case tests
docs/DEVELOPER_NOTES.md  Reasoning, standards, and growth plan
.github/workflows/        Continuous integration
```

The original `Marklist` and `Wedding couples` exercises remain at the repository root as historical work.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip pytest -e .
pytest
```

On Windows PowerShell, activate the environment with `.venv\\Scripts\\Activate.ps1`.

## Example

```python
from problem_solving.arrays import sliding_window_max
from problem_solving.graphs import shortest_unweighted_path

maxima = sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], window=3)

network = {
    "source": ["a", "b"],
    "a": ["target"],
    "b": ["c"],
    "c": ["target"],
    "target": [],
}
path = shortest_unweighted_path(network, "source", "target")
```

## Engineering notes

Implementation choices, complexity tradeoffs, testing standards, and planned additions are documented in [Developer Notes](docs/DEVELOPER_NOTES.md).
