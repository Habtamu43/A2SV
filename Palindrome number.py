class Solution():
    def isPalindrome(self, x):
         x_str=str(x)
         x_str_reversed=(str(x)[::-1]) 
         if x_str==x_str_reversed :
            return True 
         else :
            return False
