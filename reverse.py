class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        string = "".join(s)
        reverse = string[::-1]
        s[:] = list(reverse)
        