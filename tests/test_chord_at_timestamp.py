from src.chord_at_timestamp import chord_at


CHANGES = [(0, "Dm7"), (4, "G7"), (8, "Cmaj7")]


def test_sample_between_boundaries():
    assert chord_at(CHANGES, 7) == "G7"


def test_exact_boundary_returns_new_chord():
    assert chord_at(CHANGES, 4) == "G7"
    assert chord_at(CHANGES, 8) == "Cmaj7"


def test_first_chord_region():
    assert chord_at(CHANGES, 0) == "Dm7"
    assert chord_at(CHANGES, 3) == "Dm7"


def test_after_last_chord_returns_last_chord():
    assert chord_at(CHANGES, 100) == "Cmaj7"


def test_before_first_chord_returns_none():
    assert chord_at([(4, "G7"), (8, "Cmaj7")], 2) is None


def test_empty_changes_returns_none():
    assert chord_at([], 10) is None


def test_single_change():
    assert chord_at([(12, "Fmaj7")], 11) is None
    assert chord_at([(12, "Fmaj7")], 12) == "Fmaj7"
    assert chord_at([(12, "Fmaj7")], 20) == "Fmaj7"


def test_negative_times():
    changes = [(-4, "Am7"), (0, "D7"), (4, "Gmaj7")]
    assert chord_at(changes, -5) is None
    assert chord_at(changes, -4) == "Am7"
    assert chord_at(changes, -1) == "Am7"
    assert chord_at(changes, 0) == "D7"
