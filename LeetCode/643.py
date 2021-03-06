"""
643. 子数组最大平均数 I

给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:
输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75

解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

注意:
1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
"""


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_nums_k = sum(nums[0:k])
        sum_nums_tmp = max_nums_k
        nums_len = len(nums)
        for i in range(k, nums_len):
            sum_nums_tmp = sum_nums_tmp + nums[i] - nums[i - k]
            max_nums_k = max(max_nums_k, sum_nums_tmp)
        return max_nums_k / k


s = Solution()
# print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
# print(s.findMaxAverage([-1], 1))
print(
    s.findMaxAverage([
        -6662, 5432, -8558, -8935, 8731, -3083, 4115, 9931, -4006, -3284,
        -3024, 1714, -2825, -2374, -2750, -959, 6516, 9356, 8040, -2169, -9490,
        -3068, 6299, 7823, -9767, 5751, -7897, 6680, -1293, -3486, -6785, 6337,
        -9158, -4183, 6240, -2846, -2588, -5458, -9576, -1501, -908, -5477,
        7596, -8863, -4088, 7922, 8231, -4928, 7636, -3994, -243, -1327, 8425,
        -3468, -4218, -364, 4257, 5690, 1035, 6217, 8880, 4127, -6299, -1831,
        2854, -4498, -6983, -677, 2216, -1938, 3348, 4099, 3591, 9076, 942,
        4571, -4200, 7271, -6920, -1886, 662, 7844, 3658, -6562, -2106, -296,
        -3280, 8909, -8352, -9413, 3513, 1352, -8825
    ], 90))
"""
此题解法：
# print([sum(nums[i:i + k]) for i in range(len(nums) - k + 1)])
* 按顺序截取长度为k的数组，sum后保留个最大值，然后除以k即可
* 用切片的方法很容易，但是效率比较低。
* 采用单循环的模式，计算初始k个元素的和，从i=k+1个元素开始，sum(k)+nums[i]-nums[i-k]就是下一组的和
  保留最大

sums = [0] + list(itertools.accumulate(nums))
return max(map(operator.sub, sums[k:], sums)) / k

上面代码中使用了Python的两个模块：itertools和operator。
itertools.accumulate可以对一个List的元素递进的进行操作，默认是‘加’。
nums=[1,2,3,4,5] index取值是0，0-1，0-1-2，0-1-2-3，0-1-2-3-4. 返回是[1, 3, 6, 10, 15]
s=[0]+[1, 3, 6, 10, 15]=[0, 1, 3, 6, 10, 15] 增加的0 表示没有元素的和。
用s.insert(0,0)会更好一些

operator是Python中内置操作符函数接口，定义了一些算术和比较内置操作的函数。
operator.sub就是‘减法’操作。
s[k:]截掉前面k个元素，这样s[k:]的第一个元素正好是nums第一组k个元素的和。假如k=2
s[k:]就是[3, 6, 10, 15]
s是[0, 1, 3, 6, 10, 15]
再使用operator.sub 将对应位置的元素相减
3-0（前2个元素的和-0个元素的和）
6-1（前3个元素的和-前1个元素的和）
10-3（前4个元素的和-前2个元素的和）
15-6 （前5个元素的和-前3个元素的和）
这样就获取了依次每2个元素的子数组的和。
"""
