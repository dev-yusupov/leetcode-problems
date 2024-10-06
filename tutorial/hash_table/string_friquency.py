"""

Write a function that takes in a list of strings and 
returns a dictionary (hash table) where each key is a string from the list 
and the value is the count of how many times that string appears in the list.

"""

from typing import List, Dict

def string_freq(elements: List[str]) -> Dict[str, int]:
    hashed_map: Dict[str, int] = {}

    for element in elements:
        if element in hashed_map:
            hashed_map[element] += 1
        else:
            hashed_map[element] = 1

    return hashed_map

print(string_freq(["apple", "banana", "apple", "orange", "banana", "apple"]))