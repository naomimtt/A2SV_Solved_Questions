class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def dominant(lst):
            if len(lst) == 0:
                return None
                
            count = Counter(lst)
            for i in count:
                if 2 * count[i] > len(lst):
                    return i, count[i]
            return None
        
        gd = dominant(nums)
        if gd is None:
            return -1
        
        gd, tc = gd
        
        left_count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] == gd:
                left_count += 1
            
            right_count = tc - left_count
            
            left_size = i + 1
            right_size = n - i - 1
            
            if (2 * left_count > left_size and 
                2 * right_count > right_size):
                return i
        
        return -1
