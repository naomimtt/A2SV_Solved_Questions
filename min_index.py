class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count = {}
        count1 = {}
        for i in range(len(list1)):
            count[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in count:
                count1[list2[j]] = j + count[list2[j]]
        return [string for string in count1 if count1[string] == min(count1.values())]

        


        
