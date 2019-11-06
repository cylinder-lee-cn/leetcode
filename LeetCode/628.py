"""
628. 三个数的最大乘积

给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:
输入: [1,2,3]
输出: 6

示例 2:
输入: [1,2,3,4]
输出: 24

注意:
给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
"""


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]
        return max(a, b)


"""
此题解法：
如果能得到正数结果，那最大：
1、三个绝对值最大的整数相乘
2、两个绝对值最大负数和一个绝对值最大的整数相乘
如果结果只能是负数，那最大：
3、三个绝对值最小的负数相乘

所以：将数组升序排序后就只有两种取法，最右边的三个相乘；最左边2个和最右边1个相乘。
A、如果都是负数，那么最右边3个相乘符合前面推论‘3’
B、如果都是整数，那么最右边3个相乘符合前面推论‘1’
C、如果有整数，那么推论中‘1’或‘2’必定有一个是最大的
"""