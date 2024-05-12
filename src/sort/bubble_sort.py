def bubble_sort(nums:list):
    """
    冒泡排序:每次找到一个最大或者最小的数,直到数组有序
    1.比较相邻元素,如果第一个比第二个大,交换两者
    2.对每对相邻元素进行处理,此时最后的元素即为最大的数
    3.对除最后一个元素外的其他元素重复,得到第二大的数
    4.重复上述操作,直到排序完成
    """
    # 确定双重循环的范围
    for first_index in range(len(nums)-1):
        for second_index in range(len(nums)-1-first_index):
            # 比较两个相邻值并交换
            if nums[first_index]>nums[second_index]:
                nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
    return nums