from typing import List

def hash_func(value: int, arr_length: int):
    return value % arr_length

def first_repeat_element(arr: List[int]) -> int:
    hash_arr = {}

    for num in arr:
        if num in hash_arr:
            return num
        
        hash_arr[num] = True

        print(hash_arr)

    return -1

arr = [10, 5, 3, 4, 3, 5, 6]
result = first_repeat_element(arr)
print(result)  # Output: 5