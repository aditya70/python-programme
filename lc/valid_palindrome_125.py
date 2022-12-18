class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=''
        for c in s:
            if c.isalnum():
                t+=c.lower()

        n=len(t)
        if n%2 == 1: t=t[:n//2]+t[n//2 + 1:]
        return t[:n//2]==t[n//2:][::-1]        