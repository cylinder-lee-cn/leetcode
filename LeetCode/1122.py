"""
1122. 数组的相对排序

给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

提示：
arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中
"""
from typing import List
# import collections


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_dict = {}
        arr2_set = set(arr2)

        result = []
        tail = []

        for a in arr1:
            if a in arr2_set:
                arr1_dict[a] = arr1_dict.get(a, 0) + 1
            else:
                tail.append(a)

        for a in arr2:
            tmp = [a] * arr1_dict[a]
            result.extend(tmp)

        result.extend(sorted(tail))
        return result


s = Solution()
print(
    s.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
                        [2, 1, 4, 3, 9, 6]))
"""
此题解法：
* 首先遍历arr1，将存在与arr2的数字，存入dict并统计出现次数，反之放入tail的list
* 再遍历arr2，将数字按照次数重复成list，添加到result
* 最后将tail排序后拼接在result后面即可
"""
