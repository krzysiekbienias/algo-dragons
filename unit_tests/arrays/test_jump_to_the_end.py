import pytest
from arrays.jump_to_the_end import jump_to_the_end

@pytest.mark.parametrize(
    "arr, expected",
    [
        # --- Edge / minimal cases ---
        ([0], True),                 # already at the end
        ([1], True),                 # single element, any value works

        # --- Simple reachable / unreachable ---
        ([1, 0], True),              # can jump directly to last
        ([0, 1], False),             # stuck at start, cannot move
        ([1, 1, 1, 1], True),         # step-by-step
        ([1, 0, 0], False),           # can reach index 1 only, then stuck
        ([2, 0, 0], True),            # direct jump to end

        # --- Classic examples ---
        ([2, 3, 1, 1, 4], True),      # reachable
        ([3, 2, 1, 0, 4], False),     # blocked by zero

        # --- Zeros inside but still reachable ---
        ([2, 0, 2, 0, 1], True),      # can hop over zeros via index 2
        ([2, 0, 0, 0], False),        # can’t reach the last index

        # --- Larger jumps / tricky backtracking ---
        ([1, 2, 0, 1, 0], True),      # need to use index 1 jump
        ([1, 1, 0, 1], False),        # zero blocks before the end
        ([4, 0, 0, 0, 0], True),      # huge first jump
    ],
)
def test_jump_to_the_end(arr, expected):
    assert jump_to_the_end(arr) == expected


def test_jump_to_the_end_empty_raises():
    # Current implementation will IndexError on empty input; test documents that behavior.
    with pytest.raises(IndexError):
        jump_to_the_end([])