# Developer Notes

## How solutions are selected

Each module groups problems by the main technique rather than by difficulty. A solution is included when it demonstrates a reusable pattern:

- hash maps for constant-time complement and frequency lookup;
- monotonic queues for fixed-window extrema;
- two-bound binary search for insertion and duplicate handling;
- breadth-first search for minimum-hop paths;
- dynamic programming for optimal substructure;
- patience-sorting tails for subquadratic sequence analysis.

## Review checklist

Before a solution is committed:

1. State the input contract and invalid-input behaviour.
2. Include time and auxiliary-space complexity.
3. Cover an ordinary case, boundary case, and failure or empty case.
4. Prefer clear names and standard-library data structures.
5. Avoid mutating caller-owned inputs unless the function contract requires it.
6. Run the complete test suite on supported Python versions.

## Design decisions

### Return values instead of printing

The historical exercises at the repository root were written as small scripts. New modules return values so they can be composed, imported, and tested.

### Deterministic outputs

Functions return the first valid result when multiple solutions exist. This keeps tests stable and makes behaviour explicit.

### Type hints and docstrings

Public functions include type hints, concise behaviour descriptions, and complexity notes. These are part of the interface, not decoration.

## Growth plan

Future additions will focus on heaps, union-find, topological sorting, prefix sums, tries, backtracking, and SQL-style data transformations in Python.
