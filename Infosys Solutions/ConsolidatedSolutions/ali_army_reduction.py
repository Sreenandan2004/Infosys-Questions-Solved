import sys
from collections import deque

def get_min_moves_bfs(n):
    """
    Naive BFS solution to find the shortest path from n to 1.
    Time Complexity: O(N) in the worst case, but visits very few states because of division options.
    """
    if n == 1:
        return 0
        
    q = deque([(n, 0)])
    visited = {n}
    
    while q:
        curr, moves = q.popleft()
        
        # We try all 3 operational options:
        # Option 1: curr - 1
        # Option 2: ceil(curr / 2) = (curr + 1) // 2
        # Option 3: ceil(curr / 3) = (curr + 2) // 3
        options = [curr - 1, (curr + 1) // 2, (curr + 2) // 3]
        
        for next_val in options:
            if next_val == 1:
                return moves + 1
            if next_val >= 1 and next_val not in visited:
                visited.add(next_val)
                q.append((next_val, moves + 1))
                
    return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    print(get_min_moves_bfs(n))

if __name__ == '__main__':
    solve()
