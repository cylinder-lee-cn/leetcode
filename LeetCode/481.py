"""
481. 神奇字符串

神奇的字符串 S 只包含 '1' 和 '2'，并遵守以下规则：
字符串 S 是神奇的，因为串联字符 '1' 和 '2' 的连续出现次数会生成字符串 S 本身。
字符串 S 的前几个元素如下：S = “1221121221221121122 ......”

如果我们将 S 中连续的 1 和 2 进行分组，它将变成：
1 22 11 2 1 22 1 22 11 2 11 22 ......
并且每个组中 '1' 或 '2' 的出现次数分别是：
1 2 2 1 1 2 1 2 2 1 2 2 ......

你可以看到上面的出现次数就是 S 本身。
给定一个整数 N 作为输入，返回神奇字符串 S 中前 N 个数字中的 '1' 的数目。
注意：N 不会超过 100,000。

示例：
输入：6
输出：3
解释：神奇字符串 S 的前 6 个元素是 “122112”，它包含三个 1，因此返回 3。
"""


class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = '122'
        i = 2
        while i < n:
            num = '1'
            if m[-1] == '1':
                num = '2'
            m = m + num * int(m[i])
            i = i + 1
        return m[:n].count('1')


s = Solution()
print(s.magicalString(6))

"""
此题解法：
* 按照题意，先初始化一个字符串是神奇字符串的前3位。然后依据末尾可判断未来的要出现的字符是1还是2
* 初始化index为2，m的索引位，字符串未来长度就是m[i]
* 依次增加字符串，然后截取前n位，统计‘1’即可
"""
