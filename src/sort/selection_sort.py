def selection_sort(nums:list):
    """
    选择排序:每次找到一个最大或者最小的数,直到数组有序(较冒泡排序更好理解,每次循环只寻找一个数)
    """
    minIndex = None
    for first_index in range(len(nums)-1):
        minIndex = first_index
        for second_index in range(first_index+1, len(nums)):
            # 寻找遍历范围内的最小数,并记录其下标
            if nums[second_index] < nums[minIndex]:
                minIndex = second_index
        nums[first_index], nums[minIndex] = nums[minIndex], nums[first_index]
    return nums