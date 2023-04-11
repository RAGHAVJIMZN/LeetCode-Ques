# class Solution:
#     def removeStars(self, s: str) -> str:
#         n = s.count('*')
#         for i in range(n):
#             ind = s.find('*')
#             s = s[0:ind-1] + s[ind+1:]
#         return s 