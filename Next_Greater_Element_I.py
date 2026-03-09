class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    break
            for k in range(j,len(nums2)):
                if nums2[k]> i:
                    stack.append(nums2[k])
                    found=True
                    break
                else:
                    found=False
            if not found:
                stack.append(-1)
        return stack
        
        
