"""
168. Excel表列名称

给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

示例 1:
输入: 1
输出: "A"

示例 2:
输入: 28
输出: "AB"

示例 3:
输入: 701
输出: "ZY"

"""


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        d = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F',
             7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
             13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q',
             18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V',
             23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
             }

        if (n <= 16):
            return d[n]

        sum = ''

        while (n > 26):
            n, y = divmod(n, 26)
            if (y == 0):
                y = 26
                n = n - 1
            sum = d[y] + sum
        sum = d[n] + sum
        return sum


s = Solution()
print(s.convertToTitle(52))

"""
此题解法: 与171题是姊妹题, 需要将n÷26 获得商和余数, 如果商大于26 那就继续除.....
"""
