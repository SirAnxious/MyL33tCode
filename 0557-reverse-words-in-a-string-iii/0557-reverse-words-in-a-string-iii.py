class Solution:
    def reverseWords(self, s: str) -> str:
        newS = []
        lst = s.split(" ")
        res = ''
        for i in range(len(lst)):
            # newS.append()
            res += lst[i][::-1]
            # res += i[::-1]
            if(i != len(lst)-1):
                res += " "
#         for i in range(len(newS)):
#             res += newS[i]
#             if(i != len(newS)-1):
#                 res += " "
        return res