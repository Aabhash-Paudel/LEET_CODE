class Solution:
    def isPalindrome(self, x: int) -> bool:
        # original = x
        # reversed_num = 0
        # while x > 0:
        #     digit = x % 10
        #     reversed_num = reversed_num * 10 + digit
        #     x //= 10

        # return original == reversed_num
        return str(x)==str(x)[::-1]