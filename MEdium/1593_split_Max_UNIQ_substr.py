class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, stn):
            if start >= len(s):
                return 0
            
            max_splits = 0
            for i in range(start + 1, len(s) + 1):
                curr = s[start:i]
                if curr not in stn:
                    stn.append(curr)  
                    max_splits = max(max_splits, 1 + backtrack(i, stn))
                    stn.pop()
                    
            return max_splits
        
        return backtrack(0, [])