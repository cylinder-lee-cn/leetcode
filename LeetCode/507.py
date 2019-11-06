"""
507. 完美数

对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False

示例：
输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14

注意:
输入的数字 n 不会超过 100,000,000. (1e8)
"""


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        perfect = {6, 28, 496, 8128, 33550336, 8589869056, 137438691328}

        if (num in perfect):
            return True
        else:
            return False


"""
此题解法：
* 传统解法，将num进行因数分解，然后将因数相加和num进行比较
* 取巧的做法，数学家已经计算出现在能找到的前十个完美数，查表既可

首十个完全数是（OEIS A000396）：
6（1位）
28（2位）
496（3位）
8128（4位）
33550336（8位）
8589869056（10位）
137438691328（12位）
2305843008139952128（19位）
2658455991569831744654692615953842176（37位）
191561942608236107294793378084303638130997321548169216（54位）

"""