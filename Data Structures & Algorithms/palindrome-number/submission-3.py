import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        digit = 0
        length = 1
        tmp = x
        while tmp > 10:
            tmp = tmp % 10
            length += 1

        i, temp = 0, x
        while i < length:
            new_digit = temp % 10
            digit = new_digit + (digit * 10)
            temp = temp // 10

            i += 1
        
        return x == digit