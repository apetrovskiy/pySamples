from typing import List, Optional


def filter_array(input_data: Optional[List[int]]) -> List[int]:
    if input_data is None:
        return []
    if (
        len(input_data) == 0
        or all([0 == item for item in input_data])
        or all([input_data[0] == item for item in input_data])
    ):
        return input_data
    zeroes_counter = 0

    def distribute_input_elements(element: int):
        if 0 == element:
            zeroes_counter += 1
        else:
            return element

    result = [(item, None) if 0 != item else (None, 0) for item in input_data]
    return [item[0] for item in result if item[0] is not None] + [
        item[1] for item in result if item[1] is not None
    ]
    return input_data
