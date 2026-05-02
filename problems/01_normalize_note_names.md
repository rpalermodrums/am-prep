# Problem 1: Normalize Note Names

## Difficulty

Easy

## Pattern

Hash map, string normalization, basic parsing

## Prompt

You are given a list of musical note names. Return a list of pitch classes for those notes.

Use this pitch-class system:

```text
C = 0
C# / Db = 1
D = 2
D# / Eb = 3
E / Fb = 4
F / E# = 5
F# / Gb = 6
G = 7
G# / Ab = 8
A = 9
A# / Bb = 10
B / Cb = 11
B# = 0
```

Enharmonic spellings should map to the same value.

Implement:

```python
def normalize_notes(notes: list[str]) -> list[int]:
    pass
```

## Examples

### Example 1

```python
Input:  ["C", "Db", "F#", "Cb", "B#"]
Output: [0, 1, 6, 11, 0]
```

### Example 2

```python
Input:  []
Output: []
```

### Example 3

```python
Input:  ["A", "Bb", "C#", "E#", "Fb"]
Output: [9, 10, 1, 5, 4]
```

## Constraints

```text
0 <= len(notes) <= 10_000
Each note is intended to be one of the supported spellings above.
```

## Invalid Input Rule

If a note name is not supported, raise `ValueError`.

For example:

```python
normalize_notes(["C", "H"])
```

should raise `ValueError`.

## Clarifying Questions to Ask

- Are all note names valid?
- Should enharmonic spellings map to the same value?
- Do we need to support double sharps or double flats?
- Should invalid tokens raise an error or be skipped?

## Expected Approach

Use a dictionary from note spelling to pitch class. Then scan the input list once.

## Target Complexity

```text
Time:  O(n)
Space: O(n) for the output list
```

The dictionary itself has fixed size, so it is `O(1)` auxiliary space.

## Follow-ups

1. Support lowercase input like `"c#"`.
2. Support double sharps and double flats like `"C##"` and `"Abb"`.
3. Return `None` for invalid notes instead of raising.
