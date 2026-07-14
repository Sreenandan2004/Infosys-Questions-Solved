import sys

def solve():
    """
    Naive solution for Food Stamps.
    Greedily selects the food type with the maximum current taste value in each step.
    Time Complexity: O(M * N)
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    v = [int(x) for x in input_data[2:n+2]]
    d = [int(x) for x in input_data[n+2:2*n+2]]
    
    total_taste = 0
    
    for _ in range(m):
        # Find the food type with the maximum current taste value
        max_val = -1
        best_idx = -1
        for i in range(n):
            if v[i] > max_val:
                max_val = v[i]
                best_idx = i
                
        # If no food type has positive taste points, we stop
        if max_val <= 0 or best_idx == -1:
            break
            
        # Add to total taste points and decrement the taste of this food type
        total_taste += max_val
        v[best_idx] -= d[best_idx]
        
    print(total_taste)

if __name__ == '__main__':
    solve()
