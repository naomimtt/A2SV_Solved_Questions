#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        appears = {}
        for i in a:
            appears[i]= appears.get(i, 0)+1
            
        for num in b:
            if appears.get(num, 0) == 0:
                return False
            appears[num] -= 1
        
        return True
    
    
    
