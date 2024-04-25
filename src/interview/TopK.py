# 题目描述
# 从arr[1, n]这n个数中，找出最大的k个数，这就是经典的TopK问题。

#! 例：从arr[1, 12]={5,3,7,1,8,2,9,4,7,2,6,6} 这n=12个数中，找出最大的k=5个。

# partition函数模板
def partition(nums, left, right):
    pivot = nums[left]#初始化一个待比较数据
    i,j = left, right
    while(i < j):
        while(i<j and nums[j]>=pivot): #从后往前查找，直到找到一个比pivot更小的数
            j-=1
        nums[i] = nums[j] #将更小的数放入左边
        while(i<j and nums[i]<=pivot): #从前往后找，直到找到一个比pivot更大的数
            i+=1
        nums[j] = nums[i] #将更大的数放入右边
    #循环结束，i与j相等
    nums[i] = pivot #待比较数据放入最终位置
    return i #返回待比较数据最终位置

# 很自然的引出快排的实现
def quicksort(nums, left, right):
    if left < right:
        index = partition(nums, left, right)
        quicksort(nums, left, index-1)
        quicksort(nums, index+1, right)

# 例子
nums = [1,3,2,2,0]
quicksort(nums, 0, len(nums)-1)

# 转变一下思路，topk是希望找到一个位置，这个位置一边是k个比这个位置上数更小的数，另一半是更大的数
def topk_split(nums, k, left, right):
    #寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
    if (left<right):
        index = partition(nums, left, right)
        if index==k:
            return
        elif index < k:
            topk_split(nums, k, index+1, right)
        else:
            topk_split(nums, k, left, index-1)

# 有了切分函数之后，很自然的就能对最小的k个数，最大的k个数，第k大的数之类的问题进行转换了，此处就不赘述了