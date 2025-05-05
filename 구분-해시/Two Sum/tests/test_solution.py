import pytest
from src.solution1 import Solution


@pytest.mark.parametrize("nums, target, result", [
    (
        [2,7,11,15],
        9,
        [0, 1]
    ),
    (
        [3,2,4],
        6,
        [1, 2]
    ),
    (
        [3,3],
        6,
        [0, 1]
    ),
])
def test_solution(nums, target, result):
    assert Solution().twoSum(nums, target) == result