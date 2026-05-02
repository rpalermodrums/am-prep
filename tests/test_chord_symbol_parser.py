import pytest

from src.chord_symbol_parser import parse_chord


def test_altered_slash_chord():
    assert parse_chord("Bb7#11/E") == {
        "root": "Bb",
        "quality": "7",
        "alterations": ["#11"],
        "bass": "E",
    }


def test_minor_seven_flat_five_is_longest_quality():
    assert parse_chord("F#m7b5") == {
        "root": "F#",
        "quality": "m7b5",
        "alterations": [],
        "bass": None,
    }


def test_major_nine_slash_chord():
    assert parse_chord("Dbmaj9/F") == {
        "root": "Db",
        "quality": "maj9",
        "alterations": [],
        "bass": "F",
    }


def test_root_only_defaults_to_major():
    assert parse_chord("C") == {
        "root": "C",
        "quality": "maj",
        "alterations": [],
        "bass": None,
    }


def test_supported_qualities():
    assert parse_chord("Cmaj7")["quality"] == "maj7"
    assert parse_chord("Cm7")["quality"] == "m7"
    assert parse_chord("Cm")["quality"] == "m"
    assert parse_chord("Cdim7")["quality"] == "dim7"
    assert parse_chord("C7")["quality"] == "7"


def test_multiple_alterations():
    assert parse_chord("G7#9b13") == {
        "root": "G",
        "quality": "7",
        "alterations": ["#9", "b13"],
        "bass": None,
    }


def test_accidental_roots_and_basses():
    assert parse_chord("C#/Gb") == {
        "root": "C#",
        "quality": "maj",
        "alterations": [],
        "bass": "Gb",
    }


@pytest.mark.parametrize("symbol", [
    "",
    "H7",
    "/C",
    "C/",
    "Cmaj7xyz",
    "G7#",
    "G7b",
    "C##7",
    "Cbmaj7/",
    "Cm7/H",
])
def test_invalid_symbols_raise_value_error(symbol):
    with pytest.raises(ValueError):
        parse_chord(symbol)
