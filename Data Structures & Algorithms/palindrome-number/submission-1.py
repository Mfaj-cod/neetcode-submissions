import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        digit = 0
        length = math.floor(math.log10(abs(x))) + 1
        i = 0
        while i < length:
            new_digit = x % 10
            digit = new_digit + digit * 10

            i += 1
        
        return x == digit