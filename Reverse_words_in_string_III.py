class Solution:
    def reverseWords(self, s: str) -> str:
        st =("")
        x = s.split()
        for i in range(len(x)):
            j = x[i]
            j = j[::-1]
            st = st +(" ")+ j
        st = st[1:]
        return st
        