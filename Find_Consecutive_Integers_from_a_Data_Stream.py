class DataStream:

    def __init__(self, value: int, k: int):
        self.q = deque()
        self.value = value
        self.k = k
      
        
    def consec(self, num: int) -> bool:
        self.q.append(num)

        while self.value != num and self.q:
            self.q.popleft()
        if len(self.q) >= self.k:
            return True
        else:
            return False

            
            
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
