# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        i = 0
        while True:
            x = x/10
            i += 1
            print(int(x))
            if int(x) == 0:
                print(f"Base: {x}, i: {i}")
                break
        
instance = Solution()
print(instance.isPalindrome(121))