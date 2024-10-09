"""

Given a string of characters (including zeros), 
move all zeros to the end while keeping the relative order of other characters the same. 
Use two pointers to shift non-zero characters to the front.

"""

def moveZeros(word: str) -> str:
    word_list = list(word)
    non_zero_index = 0

    for char in word_list:
        if char != "0":
            word_list[non_zero_index] = char
            non_zero_index += 1  # O(1)

    for i in range(non_zero_index, len(word)):
        word_list[i] = "0" #  O(1)

    return "".join(word_list)


print(moveZeros("0fd03dda"))