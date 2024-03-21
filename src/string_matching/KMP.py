class KMP:
    def __init__(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle

    def search_pattern(self):
        m, n = len(self.haystack), len(self.needle)
        # step1: compute next array
        i, j = 0, 1
        next = [0] * n
        while j < n:
            if self.needle[i] == self.needle[j]:  #如果相等比较好理解，直接更新next数组
                next[j] = i+1
                i += 1
                j += 1
            elif i > 0:  #如果不相等的话，需要将i跳转到next[i-1]，但是如果i=0的话，则不存在next[i-1]，需要另外判断
                i = next[i-1]
            else:  #如果i=0，needle[i]!=needle[j]，说明只有j需要一直往后+1
                j += 1
        # step2: kmp search
        i, j = 0, 0
        while i < m and j < n:
            if self.haystack[i] == self.needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = next[j-1]
            else:
                i += 1
        if j == n: return i-j
        return -1