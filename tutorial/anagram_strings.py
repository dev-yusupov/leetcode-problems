def check_anagrams(string1: str, string2: str) -> bool:

    if len(string1) != len(string2):
        return False

    hash_counts = {}

    for char in string1:
        hash_counts[char] = hash_counts.get(char, 0) + 1

    for char in string2:
        if char not in hash_counts:
            return False
        
        hash_counts[char] -= 1

        if hash_counts[char] < 0:
            return False
        
    return True


print(check_anagrams("listen", 'silent'))