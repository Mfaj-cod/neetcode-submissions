import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        if x < 0:
            return False

        original = x
        new = 0
        while x > 0:
            new_digit = x % 10
            new = (new * 10) + new_digit
            x = x // 10
        
        return new == original