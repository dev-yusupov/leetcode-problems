"""

Write a function that takes a list of strings and returns a list of lists, 
where each inner list contains words from the original list that are anagrams of each other. 
Words are considered anagrams if they contain the exact same characters in any order.

"""

from typing import List

def sort_letters_of_word(word: str) -> str:
    return "".join(sorted(word))

def sort_anagrams(words: List[str]) -> List[List[str]]:
    hashed_map = {}

    for word in words:
        sorted_word = sort_letters_of_word(word)
        if sorted_word in hashed_map:
            hashed_map[sorted_word].append(word)

        else:
            hashed_map[sorted_word] = [word]

    return list(hashed_map.values())


print(sort_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))