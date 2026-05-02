# Problem 3: Chord Symbol Parser

## Difficulty

Medium

## Pattern

String parsing, left-to-right scanning, validation

## Prompt

Parse a chord symbol into structured parts:

```python
{
    "root": str,
    "quality": str,
    "alterations": list[str],
    "bass": str | None,
}
```

A chord symbol may contain:

1. a required root note
2. an optional quality
3. zero or more alterations
4. an optional slash-bass note

Implement:

```python
def parse_chord(symbol: str) -> dict:
    pass
```

## Supported Root and Bass Notes

A note token is:

```text
A, B, C, D, E, F, or G
```

with an optional accidental:

```text
# or b
```

Examples:

```text
C, Bb, F#, A, Db
```

Do not support double sharps or double flats for this problem.

## Supported Qualities

Use the following valid qualities:

```python
["maj9", "maj7", "m7b5", "dim7", "m7", "m", "7"]
```

If no quality is present, use:

```python
"maj"
```

Important: match the longest valid quality first.

For example, `"maj7"` should parse as `"maj7"`, not `"m"` plus invalid trailing text.

## Supported Alterations

An alteration starts with `#` or `b`, followed by one or more digits.

Examples:

```text
#11
b9
#5
b13
```

Multiple alterations may appear in sequence:

```text
G7#9b13
```

## Slash Bass

A slash-bass note starts with `/`, followed by a valid note token.

Example:

```text
Bb7#11/E
```

has bass note `"E"`.

## Examples

### Example 1

```python
Input: "Bb7#11/E"

Output: {
    "root": "Bb",
    "quality": "7",
    "alterations": ["#11"],
    "bass": "E",
}
```

### Example 2

```python
Input: "F#m7b5"

Output: {
    "root": "F#",
    "quality": "m7b5",
    "alterations": [],
    "bass": None,
}
```

### Example 3

```python
Input: "Dbmaj9/F"

Output: {
    "root": "Db",
    "quality": "maj9",
    "alterations": [],
    "bass": "F",
}
```

### Example 4

```python
Input: "C"

Output: {
    "root": "C",
    "quality": "maj",
    "alterations": [],
    "bass": None,
}
```

## Invalid Input Rule

Raise `ValueError` if the chord symbol cannot be fully parsed.

Examples that should raise:

```python
"H7"        # invalid root
"Cmaj7xyz"  # invalid trailing text
"G7#"       # alteration has no number
"/C"        # missing root
"C/"        # missing bass note
```

## Clarifying Questions to Ask

- Which chord qualities are in scope?
- Can alterations appear in any order?
- Do we support slash chords?
- How should invalid symbols be handled?
- Should lowercase chord symbols be accepted?

## Expected Approach

Use a left-to-right parser:

1. Parse the root note.
2. Match the longest valid quality.
3. Parse zero or more alterations.
4. Parse optional slash bass.
5. Confirm that the entire string was consumed.

## Target Complexity

```text
Time:  O(n)
Space: O(n) in the worst case for output strings / alterations
```

## Follow-ups

1. Support more qualities like `sus4`, `add9`, `6`, `13`.
2. Normalize enharmonic spellings.
3. Return a dataclass instead of a dictionary.
4. Parse a full lead-sheet line like `| Dm7 G7 | Cmaj7 A7b9 |`.
