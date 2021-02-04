# Input: "aaaabbbcca"
# Output: [("a", 4), ("b", 3), ("c", 2), ("a", 1)]
from collections import Counter
from typing import List, Tuple


def grouper(input:str)->List[Tuple[str,int]]:
    number_of_items = 1
    def calc(index:int):
        nonlocal number_of_items
        if index+1 < len(input):
            if input[index] != input[index+1]:
                result = (input[index],number_of_items)
                number_of_items = 1
                return result
            else:
                number_of_items += 1
        else:
           return (input[index],number_of_items)
    return [x for x in [calc(index) for index in range(len(input))] if x is not None]


print(grouper("aaaabbbcca"))
print(grouper("aaaabbbccca"))
