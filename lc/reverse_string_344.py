class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)
        for i in range(len(s)):
            t = s[i]
            s[i]=s[n-i-1]
            s[n-i-1]=t