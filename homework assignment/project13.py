def combinationSum2(candidates, target):
    candidates.sort()  # Sort to handle duplicates
    result = []
    
    def backtrack(start, path, remaining):
        # If target becomes 0, we found a valid combination
        if remaining == 0:
            result.append(path[:])
            return
        
        # If remaining becomes negative, stop exploring
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            # If current number exceeds remaining target, stop
            if candidates[i] > remaining:
                break
            
            # Choose the number
            path.append(candidates[i])
            
            # Move to next index (i + 1) since we use each number once
            backtrack(i + 1, path, remaining - candidates[i])
            
            # Backtrack (remove last element)
            path.pop()
    
    backtrack(0, [], target)
    return result