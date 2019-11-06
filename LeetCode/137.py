"""
137. 只出现一次的数字 II
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,3,2]
输出: 3

示例 2:
输入: [0,1,0,1,0,1,99]
输出: 99
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d = {}
        # for n in nums:
        #     d[n] = d.get(n, 0) + 1

        # for k, v in d.items():
        #     if (v == 1):
        #         return k

        ones, twos = 0, 0
        for n in nums:
            ones = (ones ^ n) & (~twos)
            twos = (twos ^ n) & (~ones)

        return ones


s = Solution()
print(s.singleNumber([2, 2, 3, 2]))
print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))
"""
此题解法：
* 最简单的就是使用数字的统计法，将数字以及对应个数放入字典，然后看看字典内value为1的是哪个数字
* 还有位运算法
利用状态机表示：我们用下面的三种状态来表示对于某个数字出现了多少次：00、01、10、00，也就是我们累加的过程0——>1——>2——>0，当满3个数字时则记为0次。
所以，我们可以用两个整数（32位）来表示所有数中每一位上出现1的次数。例子：ones的第3位为1，twos的第3位为0，则表示当前累计的所有元素中，各个元素的第3位上出现1的个数为2个。
写出对应关系：
00 (+) 1 = 01
01 (+) 1 = 10
10 (+) 1 = 00 ( mod 3)
那么我们用ab来表示开始的状态，对于加1操作后，得到的新状态的ba（其中a表示倒数第一位，b表示倒数第2位）的算法如下：
a = a xor r & ~b;
b = b xor r & ~a;
因为我们最后要求的是只出现1次的元素，所以通过对所有元素的位运算后，32个位上出现1只有一次的元素就是我们要返回的元素，也就是ones当前保存的元素。
"""