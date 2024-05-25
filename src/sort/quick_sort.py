def quick_sort(nums):
    """
    快速排序
    """
    # 确定返回条件
    if len(nums) <= 1:
        return nums

    # 找到一个锚点
    pivot = nums[len(nums) // 2]
    # 将数组分为小于锚点的左边和大于锚点的右边
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    # 递归调用排序后的结果再合并
    return quick_sort(left) + middle + quick_sort(right)