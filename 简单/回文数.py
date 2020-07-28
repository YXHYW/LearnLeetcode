"""
问题描述：
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

思路1：转换为字符串
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            # 如果是复数，倒转过后肯定不是回文数
            return False
        else:
            list_x = list(str(x))
            if list_x == list_x[::-1]:
                return True
            else:
                return False