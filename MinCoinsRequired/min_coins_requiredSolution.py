def min_coins(coins: list[int], V: int) -> int:
    """
    Finds the minimum number of coins required to make a given value V.
    If it is not possible to make the change, returns -1.
    """
    # Initialize DP array of size V + 1 with infinity representing unreachable states
    # We use V + 1 because the maximum number of coins of denomination >= 1 is V.
    # Therefore, V + 1 is effectively infinity.
    dp = [float('inf')] * (V + 1)
    
    # Base case: 0 coins are needed to make a value of 0
    dp[0] = 0
    
    # Iterate through all values from 1 to V
    for i in range(1, V + 1):
        # Check every coin denomination
        for coin in coins:
            # If the current coin is smaller than or equal to the amount i
            if i - coin >= 0:
                # Update the DP state using the recurrence relation:
                # dp[i] = min(dp[i], dp[i - coin] + 1)
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    # If the target value is still unreachable, return -1
    return dp[V] if dp[V] != float('inf') else -1

if __name__ == "__main__":
    # Test cases
    coins1 = [25, 10, 5]
    V1 = 30
    print(f"Coins: {coins1}, V: {V1} -> Minimum coins: {min_coins(coins1, V1)}")
    
    coins2 = [9, 6, 5, 1]
    V2 = 11
    print(f"Coins: {coins2}, V: {V2} -> Minimum coins: {min_coins(coins2, V2)}")
