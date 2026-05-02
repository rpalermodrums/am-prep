import pytest

from src.normalize_note_names import normalize_notes


def test_normalize_sample():
    assert normalize_notes(["C", "Db", "F#", "Cb", "B#"]) == [0, 1, 6, 11, 0]


def test_empty_list():
    assert normalize_notes([]) == []


def test_naturals():
    assert normalize_notes(["C", "D", "E", "F", "G", "A", "B"]) == [0, 2, 4, 5, 7, 9, 11]


def test_sharps():
    assert normalize_notes(["C#", "D#", "F#", "G#", "A#"]) == [1, 3, 6, 8, 10]


def test_flats():
    assert normalize_notes(["Db", "Eb", "Gb", "Ab", "Bb"]) == [1, 3, 6, 8, 10]


def test_boundary_enharmonics():
    assert normalize_notes(["B#", "Cb", "E#", "Fb"]) == [0, 11, 5, 4]


def test_repeated_notes_count_repeated_occurrences():
    assert normalize_notes(["A", "A", "A"]) == [9, 9, 9]


def test_invalid_note_raises_value_error():
    with pytest.raises(ValueError):
        normalize_notes(["C", "H"])


def test_double_accidentals_not_supported():
    with pytest.raises(ValueError):
        normalize_notes(["C##"])
