def bubble_sort(nums:list):
    for first_index in range(len(nums)-1):
        for second_index in range(len(nums)-1-first_index):
            if nums[first_index]>nums[second_index]:
                nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
    return nums