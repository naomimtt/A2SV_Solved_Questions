class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for arr in image:
            arr.reverse()
            for j in range(len(arr)):
                arr[j] = 1 - arr[j]
        return image


        
