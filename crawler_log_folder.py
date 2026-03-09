class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        for i in logs:
            if i!='./' and i != "../":
                counter += 1
            elif i=='../':
                if counter != 0:
                    counter -= 1
        return counter
                    
           
