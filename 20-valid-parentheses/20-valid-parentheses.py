class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        opening = ['{', '[', '(']
        closing = ['}', ']', ')']
        hashMap = {']': '[', '}': '{', ')': '('}
        for i in range(len(s)):
            if s[i] in opening:
                arr.append(s[i])
                # print('added', s[i])
            elif s[i] in closing:
                if len(arr) != 0 and arr[-1] == hashMap.get(s[i]):
                    arr.pop()
                    # print('popped', s[i])
                else:
                    return False
        return len(arr) == 0