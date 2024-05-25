# 最大子数组
"""
1.划分问题：将序列分成元素个数尽可能相等的两半。
2.递归求解：分别求出位于左半和右半的最佳序列。
3.合并问题：求出起点位于左半，终点位于右半的最大连续和序列，和子问题最优解比较。
"""
def find_max_crossing_subarray(nums, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    max_left = mid
    for i in range(mid, low-1, -1):
        sum += nums[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    max_right = mid
    for i in range(mid+1, high+1):
        sum += nums[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(nums, low, high):
    if high == low:
        return (low, high, nums[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(nums, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(nums, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(nums, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

import unittest
class TestMaximumSubarray(unittest.TestCase):
    def test_maximum_subarray(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(find_maximum_subarray(nums, 0, len(nums)-1), (3, 6, 6))

if __name__ == '__main__':
    unittest.main()