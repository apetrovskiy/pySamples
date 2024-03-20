from typing import List
import pytest

from src.core.solution_array_filter import filter_array


TEST_DATA = [
    (None, []),
    ([], []),
    ([0], [0]),
    ([1], [1]),
    ([0, 1], [1, 0]),
    ([0, 1, 0, 2, 0, 5, 0, 4, 3], [1, 2, 5, 4, 3, 0, 0, 0, 0]),
]


@pytest.mark.parametrize("input_data,expected_result", TEST_DATA)
def test_array_filtering(input_data: List[int], expected_result: List[int]):
    actual_result = filter_array(input_data)
    #
    print(actual_result)
    #
    assert actual_result == expected_result
