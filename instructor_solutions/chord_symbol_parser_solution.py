def parse_note_token(s: str, i: int) -> tuple[str, int]:
    if i >= len(s) or s[i] not in "ABCDEFG":
        raise ValueError("Expected note")

    note = s[i]
    i += 1

    if i < len(s) and s[i] in "#b":
        note += s[i]
        i += 1
        if i < len(s) and s[i] in "#b":
            raise ValueError("Double accidentals are not supported")

    return note, i


def parse_chord(symbol: str) -> dict:
    qualities = ["maj9", "maj7", "m7b5", "dim7", "m7", "m", "7"]

    root, i = parse_note_token(symbol, 0)

    quality = "maj"
    for q in qualities:
        if symbol.startswith(q, i):
            quality = q
            i += len(q)
            break

    alterations = []
    while i < len(symbol) and symbol[i] != "/":
        if symbol[i] not in "#b":
            raise ValueError("Invalid alteration")

        j = i + 1
        while j < len(symbol) and symbol[j].isdigit():
            j += 1

        if j == i + 1:
            raise ValueError("Alteration must include a number")

        alterations.append(symbol[i:j])
        i = j

    bass = None
    if i < len(symbol) and symbol[i] == "/":
        bass, i = parse_note_token(symbol, i + 1)

    if i != len(symbol):
        raise ValueError("Invalid chord symbol")

    return {
        "root": root,
        "quality": quality,
        "alterations": alterations,
        "bass": bass,
    }
