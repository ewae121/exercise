from src.deduplicator import Deduplicator


def test_deduplicator():
    deduplicator = Deduplicator()
    assert deduplicator.deduplicate("aabbaa", 1) == "aba"

    assert deduplicator.deduplicate("aaaa", 2) == "aa"
    assert deduplicator.deduplicate("aaaabbbbbcccc", 2) == "aabbcc"


def test_validate():
    deduplicator = Deduplicator()
    assert deduplicator.deduplicate("abcdefg", 1) == "abcdefg"
    assert deduplicator.deduplicate("abcdefg", 0) == ""
    assert deduplicator.deduplicate("", 100) == ""


def _checkException(method, input_string, occurence):
    hasException = False
    try:
        method(input_string, occurence)
    except (TypeError, ValueError):
        hasException = True
    return hasException


def test_invalid_input():
    deduplicator = Deduplicator()
    assert not _checkException(
        deduplicator.deduplicate, 100, 1
    )  # Converted to str
    assert not _checkException(
        deduplicator.deduplicate, "azeabzr", "0"
    )  # Converted to int
    assert _checkException(deduplicator.deduplicate, 100, "a")
