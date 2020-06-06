# Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.
#
# Note:
#
#
# 	1 <= w.length <= 10000
# 	1 <= w[i] <= 10^5
# 	pickIndex will be called at most 10000 times.
#
#
# Example 1:
#
#
# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
#
#
#
# Example 2:
#
#
# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
#
#
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
#


class Solution:
    def __init__(self, w):
        ep = 10e-5
        self.N, summ = len(w), sum(w)
        weights = [elem/summ for elem in w]
        Dic_More, Dic_Less, self.Boxes = {}, {}, []
        
        for i in range(self.N):
            if weights[i] >= 1/self.N:
                Dic_More[i] = weights[i]
            else:
                Dic_Less[i] = weights[i]
                
        while Dic_More and Dic_Less:
            t_1 = next(iter(Dic_More))
            t_2 = next(iter(Dic_Less))
            self.Boxes.append([t_2,t_1,Dic_Less[t_2]*self.N])
            
            Dic_More[t_1] -= (1/self.N - Dic_Less[t_2])
            if Dic_More[t_1] < 1/self.N - ep:
                Dic_Less[t_1] = Dic_More[t_1]
                Dic_More.pop(t_1)
            Dic_Less.pop(t_2)
            
        for key in Dic_More: self.Boxes.append([key])

    def pickIndex(self):
        r = random.uniform(0, 1)
        Box_num = int(r*self.N)
        if len(self.Boxes[Box_num]) == 1:
            return self.Boxes[Box_num][0]
        else:
            q = random.uniform(0, 1)
        if q < self.Boxes[Box_num][2]:
            return self.Boxes[Box_num][0]
        else:
            return self.Boxes[Box_num][1]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
