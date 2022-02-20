"""
  Test for deduplicator module.
"""

from src.deduplicator.deduplicator import Deduplicator
from src.deduplicator import constants


def test_deduplicator():
    """Test deduplicate method"""
    deduplicator = Deduplicator()
    assert deduplicator.deduplicate("aabbaa", 1) == "aba"

    assert deduplicator.deduplicate("aaaa", 2) == "aa"
    assert deduplicator.deduplicate("aaaabbbbbcccc", 2) == "aabbcc"


def test_validate():
    """Test deduplicate method as requested"""
    deduplicator = Deduplicator()
    assert deduplicator.deduplicate("abcdefg", 1) == "abcdefg"
    assert deduplicator.deduplicate("abcdefg", 0) == ""
    assert deduplicator.deduplicate("", 100) == ""


def _check_exception(method, input_string, occurence):
    has_exception = False
    try:
        method(input_string, occurence)
    except (TypeError, ValueError):
        has_exception = True
    return has_exception


def test_invalid_input():
    """Test exception for invalid input"""
    deduplicator = Deduplicator()
    assert not _check_exception(
        deduplicator.deduplicate, 100, 1
    )  # Converted to str
    assert not _check_exception(
        deduplicator.deduplicate, "azeabzr", "0"
    )  # Converted to int
    assert _check_exception(deduplicator.deduplicate, 100, "a")


def test_processing_state_changed():
    """Test on_processing_state_changed callback"""
    start = 0
    stop = 0

    def my_cb(new_state):
        nonlocal start
        nonlocal stop

        if new_state == constants.START_PROCESSING:
            start += 1
        elif new_state == constants.STOP_PROCESSING:
            stop += 1

    deduplicator = Deduplicator()
    deduplicator.add_state_changed_cb(my_cb)
    new_str = deduplicator.deduplicate("aaazzzddddee", 2)

    assert new_str == "aazzddee"
    assert start == 1
    assert stop == 1
