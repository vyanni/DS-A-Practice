class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List([int]]
        """
        totalCombinations = []
        
        def backtracking(targetDifference, currentCombination, currentIndex):
            if targetDifference == 0:
                totalCombinations.append(list(currentCombination))
                return 
            
            if targetDifference < 0:
                return
            
            for i in range(currentIndex, len(candidates)):
                currentCombination.append(candidates[i])
                backtracking(targetDifference - candidates[i], currentCombination, i)
                currentCombination.pop()
        
        backtracking(target, [], 0)
        return totalCombinations

