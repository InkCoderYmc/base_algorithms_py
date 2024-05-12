def merge_sort(nums:list):
    """
    归并排序
    """
    # 确定返回条件
    if len(nums)<=1:
        return nums

    # 从中间将待排序数组拆分
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]

    return merge(merge_sort(left), merge_sort(right))

def merge(nums_1:list, nums_2:list):
    """合并两个有序数组,此处手动实现合并两个有序数组的功能,实际上可以使用Python heapq.merge()方法,后续会对此方法进行深入研究"""
    result = []
    while nums_1 and nums_2:
        # 比较两个数组的第一个元素,将较小的添加到结果数组中
        if nums_1[0] <= nums_2[0]:
            result.append(nums_1.pop(0))
        else:
            result.append(nums_2.pop(0))
    # 将剩余元素添加到结果数组中
    result += nums_1
    result += nums_2
    return result
