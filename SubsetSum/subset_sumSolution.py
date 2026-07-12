def is_subset_sum(arr: list[int], target_sum: int) -> bool:
    """
    Checks if there is a subset of the given set whose sum is equal to target_sum.
    """
    # Create a 1D DP array of size target_sum + 1, initialized to False.
    # dp[j] will store whether a sum of j is possible.
    dp = [False] * (target_sum + 1)
    
    # Base case: A sum of 0 is always possible (empty subset)
    dp[0] = True
    
    # Process each element in the input list
    for num in arr:
        # Loop backwards from target_sum down to num.
        # Iterating backwards ensures we use each element at most once.
        # If we went forwards, dp[j-num] would represent the current row's update,
        # which would allow multiple uses of the same element.
        for j in range(target_sum, num - 1, -1):
            # Recurrence relation:
            # The sum j is possible if it was already possible (dp[j])
            # OR if the sum (j - num) was possible using previous elements.
            dp[j] = dp[j] or dp[j - num]
            
    return dp[target_sum]

if __name__ == "__main__":
    # Test cases
    set1 = [3, 34, 4, 12, 5, 2]
    sum1 = 9
    print(f"Set: {set1}, Target Sum: {sum1} -> {is_subset_sum(set1, sum1)}")
    
    set2 = [3, 34, 4, 12, 5, 2]
    sum2 = 30
    print(f"Set: {set2}, Target Sum: {sum2} -> {is_subset_sum(set2, sum2)}")
