class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""
        
        for c in s:
            if c == "[":
                stack.append(curr_str)
                stack.append(curr_num)
                curr_num = 0
                curr_str = ""
            elif c == "]":
                prev_num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + prev_num * curr_str
            elif c.isdigit():
                curr_num = curr_num*10 + int(c)
            else:
                curr_str += c
        return curr_str