"""
229. 求众数 II

给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:
输入: [3,2,3]
输出: [3]

示例 2:
输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        m1, c1, m2, c2 = 0, 0, 0, 0

        result = []

        for v in nums:
            if (c1 == 0 or m1 == v) and m2 != v:
                m1 = v
                c1 = c1 + 1
            elif (c2 == 0 or m2 == v):
                m2 = v
                c2 = c2 + 1
            else:
                c1 = c1 - 1
                c2 = c2 - 1

        c1, c2 = 0, 0

        for v in nums:
            if m1 == v:
                c1 = c1 + 1
            elif m2 == v:
                c2 = c2 + 1

        nl = int(len(nums) / 3)

        if c1 > nl:
            result.append(m1)

        if c2 > nl:
            result.append(m2)

        return result


"""
此题解法：
* 此题与169类似，还是摩尔投票法
"""

s = Solution()
print(s.majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
