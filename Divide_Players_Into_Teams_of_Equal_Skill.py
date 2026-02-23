class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        skill.sort()
        total_skills = sum(skill)
        num_player=n//2
        if total_skills%num_player !=0:
            return -1
        target= total_skills//num_player
        chemistry=0
        i=0
        j=n-1
        while i<j:
            if skill[i]+skill[j]!= target:
                return -1
            chemistry+=skill[i]*skill[j]
            i+=1
            j-=1
        return chemistry
        

        
