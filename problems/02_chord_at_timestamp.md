# Problem 2: Chord at Timestamp

## Difficulty

Easy / Medium

## Pattern

Binary search over sorted intervals

## Prompt

You are given a sorted list of chord changes. Each chord change is a pair:

```python
(start_time, chord_symbol)
```

A chord remains active from its `start_time` until the next chord change begins.

Given a timestamp, return the chord active at that timestamp.

Implement:

```python
def chord_at(changes: list[tuple[int, str]], time: int) -> str | None:
    pass
```

If the timestamp is before the first chord change, return `None`.

If the timestamp lands exactly on a chord change, return the new chord.

## Examples

### Example 1

```python
changes = [(0, "Dm7"), (4, "G7"), (8, "Cmaj7")]
time = 7

Output: "G7"
```

Explanation:

```text
0 <= time < 4  -> Dm7
4 <= time < 8  -> G7
8 <= time      -> Cmaj7
```

Since `time = 7`, the active chord is `"G7"`.

### Example 2

```python
changes = [(0, "Dm7"), (4, "G7"), (8, "Cmaj7")]
time = 4

Output: "G7"
```

The timestamp lands exactly on the `G7` change.

### Example 3

```python
changes = [(4, "G7"), (8, "Cmaj7")]
time = 2

Output: None
```

The timestamp is before the first chord change.

## Constraints

```text
0 <= len(changes) <= 100_000
changes is sorted by start_time in ascending order
start_time and time are integers
```

## Clarifying Questions to Ask

- What should happen if the timestamp is before the first chord?
- Are the changes guaranteed sorted?
- If time lands exactly on a chord change, should we return the new chord?
- Can two changes share the same timestamp?

## Expected Approach

Find the rightmost chord change whose `start_time <= time`.

A linear scan works, but binary search is better for one query against a long list.

## Target Complexity

```text
Time:  O(log n)
Space: O(1)
```

## Follow-ups

1. Answer many timestamp queries.
2. If timestamp queries are sorted, solve all queries with two pointers in `O(n + q)`.
3. Handle duplicate chord-change times by treating the last duplicate as the active override.
