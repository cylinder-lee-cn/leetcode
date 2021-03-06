"""
747. 至少是其他数字两倍的最大数

在一个给定的数组nums中，总是存在一个最大元素 。
查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
如果是，则返回最大元素的索引，否则返回-1。

示例 1:
输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.

示例 2:
输入: nums = [1, 2, 3, 4]
输出: -1
解释: 4没有超过3的两倍大, 所以我们返回 -1.

提示:
nums 的长度范围在[1, 50].
每个 nums[i] 的整数范围在 [0, 99].
"""


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_n = max(nums)
        max_n_index = nums.index(max_n)

        max_n_half = max_n / 2
        nums[max_n_index] = max_n_half
        if (max(nums) == max_n_half):
            return max_n_index
        else:
            return -1


s = Solution()
print(s.dominantIndex([1, 2, 3, 4]))
print(s.dominantIndex([3, 6, 1, 0]))
"""
此题解法：已知，最大元素是否至少是数组中每个其他数字的两倍。
也就是说 将最大元素/2 依旧还是这数组里最大。

"""
