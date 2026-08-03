class Solution:
    def longestPalindrome(self, s: str) -> str:
        # take 2 pointers at 0 and 1
        # if palindrome and longer than already palindrome, replace the already with curr one, move pointer right
        # if not palindrome, move both
        res = ""

        for l in range(len(s)):
            r = l

            while r < len(s):
                curr = s[l:r+1]

                if curr == curr[::-1]:
                    if len(curr) > len(res):
                        res = curr

                r += 1
        
        return res