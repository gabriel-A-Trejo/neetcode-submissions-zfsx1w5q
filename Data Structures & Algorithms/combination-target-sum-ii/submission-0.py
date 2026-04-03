class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()


        def dfs(index, current, total):
            if total == target:
                result.append(current.copy())
                return
            for j in range(index, len(candidates)):
                if j > index and candidates[j] == candidates[j - 1]:
                   continue
                if total + candidates[j] > target:
                   break
                current.append(candidates[j])
                dfs(j + 1, current, total + candidates[j])
                current.pop()
        dfs(0, [], 0)
        return result
        