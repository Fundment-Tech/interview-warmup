from warmup import most_common, running_total


def test_running_total():
    assert running_total([1, 2, 3]) == [1, 3, 6]


def test_running_total_empty():
    assert running_total([]) == []


def test_most_common():
    assert most_common(["a", "b", "b"]) == "b"


def test_most_common_empty():
    assert most_common([]) is None


def test_most_common_tie_returns_first():
    assert most_common(["x", "y", "y", "x"]) == "x"
