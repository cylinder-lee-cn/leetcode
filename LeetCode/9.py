"""
9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False

        while x > rev:
            y = divmod(x, 10)
            x = y[0]
            pop = y[1]
            rev = rev * 10 + pop

        if x == rev or x == rev // 10:
            return True
        else:
            return False


S = Solution()
print(S.isPalindrome(123321))

"""
回文数解法,参考官网. 还是利用数学方法进行数字的反转.但是有几个注意事项:
* 负数都不是回文数
* 0是回文数,但是个位数是0的其它数字均不是回文数
* 使用商和余数的方法进行数字反转的时候,如果发现已经反转的数字和剩余的数字相同,即可判断此数为回文数
    (这个回文数一定是偶数位,恰好反转到了一半)
* 同上,如果发现已经反转的数字与剩余的数字÷10的商相同,也可以判断此数为回文数
    (这个回文数一定是奇数位,中间位的数字必定与自己相同,反转后位置不变)
"""