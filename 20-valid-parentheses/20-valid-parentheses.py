from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opening = ['{', '[', '(']
        closing = ['}', ']', ')']
        hashMap = {']': '[', '}': '{', ')': '('}
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
                # print('added', s[i])
            elif s[i] in closing:
                if len(stack) != 0 and stack[-1] == hashMap.get(s[i]):
                    stack.pop()
                    # print('popped', s[i])
                else:
                    return False
        return len(stack) == 0