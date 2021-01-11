"""
1287. 有序数组中出现次数超过25%的元素
给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，
它的出现次数超过数组元素总数的 25%。

请你找到并返回这个整数

示例：
输入：arr = [1,2,2,6,6,6,6,7,10]
输出：6

提示：
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""

from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arr_dict = Counter(arr)
        arr_len = len(arr)
        for k, v in arr_dict.items():
            if v > arr_len/4:
                return k


s = Solution()
print(s.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
