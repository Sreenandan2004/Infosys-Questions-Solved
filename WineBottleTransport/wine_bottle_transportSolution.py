class Solution:
    def wineTrading(self, arr: list[int], n: int) -> int:
        """
        Calculates the minimum units of work required to fulfill all demands/supplies
        of wine bottles for N houses built along a straight line.
        
        Parameters:
        arr (list[int]): Supply (> 0) or demand (< 0) of wine at each house.
        n (int): Number of houses.
        
        Returns:
        int: Minimum work required to fulfill all demands.
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        work = 0
        imbalance = 0
        
        for bottles in arr:
            # Update the current net supply/demand imbalance
            imbalance += bottles
            # The absolute value of the imbalance must cross to the next house
            work += abs(imbalance)
            
        return work


if __name__ == "__main__":
    # Test cases
    sol = Solution()
    
    # Example 1
    arr1 = [5, -4, 1, -3, 1]
    n1 = len(arr1)
    ans1 = sol.wineTrading(arr1, n1)
    print(f"Test 1: Input={arr1}, Expected=9, Got={ans1}")
    assert ans1 == 9, f"Expected 9, but got {ans1}"
    
    # Example 2
    arr2 = [-1000, -1000, -1000, 1000, 1000, 1000]
    n2 = len(arr2)
    ans2 = sol.wineTrading(arr2, n2)
    print(f"Test 2: Input={arr2}, Expected=9000, Got={ans2}")
    assert ans2 == 9000, f"Expected 9000, but got {ans2}"
    
    print("All tests passed successfully!")
