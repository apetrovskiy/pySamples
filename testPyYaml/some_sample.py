# Input: "aaaabbbcca"
# Output: [("a", 4), ("b", 3), ("c", 2), ("a", 1)]
from typing import List, Tuple


def char_grouper(input:str)->List[Tuple[str,int]]:
    result=[]
    index = 0
    previous_char=''
    current_char=input[index]
    number_of_items = 0
    while index < len(input)-1:
        index +=1
        previous_char = current_char
        current_char = input[index]
        if current_char != previous_char:
            result.append((previous_char,number_of_items))
            number_of_items = 1
        else:
            number_of_items += 1
    return result


print(char_grouper("aaaabbbcca"))
