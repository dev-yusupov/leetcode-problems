from typing import List

def compress(chars: List[str]) -> int:
        s_list = []

        count = {}
        
        for char in chars:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for key, value in count.items():
            s_list.append(key)
            
            if value == 1:
                s_list.append("")
            else:
                s_list.append(str(value))

        return count
    
print(compress(chars=["a", "a", "a"]))