class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subseq_list = []

        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                subseq_list.append(s[i])
                i+=1
            
            j+=1

        
        if "".join(subseq_list) == s:
            return True
        
        else:
            return False
        

class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = 0

        for c in t:
            if s[i] == c:
                i+=1

                if i == len(s):
                    return True

        return False