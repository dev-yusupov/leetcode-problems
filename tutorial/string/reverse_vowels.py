def reverseVowels(word: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    word_list = list(word)
    
    left = 0
    right = len(word) - 1

    while left < right:
        if word_list[left] not in vowels:
            left += 1
            continue
        if word_list[right] not in vowels:
            right -= 1
            continue

        word_list[left], word_list[right] = word_list[right], word_list[left]

        left += 1
        right -= 1

    return "".join(word_list)


print(reverseVowels("IceCreAm"))