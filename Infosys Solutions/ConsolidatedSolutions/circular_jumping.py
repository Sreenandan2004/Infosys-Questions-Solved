import sys
from collections import deque

def solve():
    """
    Circular jumping shortest path using BFS.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    x = int(input_data[1])
    y = int(input_data[2])
    a = [0] + [int(val) for val in input_data[3:n+3]]
    
    if x == y:
        print(0)
        return
        
    dist = [-1] * (n + 1)
    dist[x] = 0
    q = deque([x])
    
    while q:
        curr = q.popleft()
        step = a[curr]
        
        # Option 1: Jump right
        right = (curr + step - 1) % n + 1
        # Option 2: Jump left
        left = (curr - step - 1) % n + 1
        
        for neighbor in (right, left):
            if dist[neighbor] == -1:
                dist[neighbor] = dist[curr] + 1
                if neighbor == y:
                    print(dist[neighbor])
                    return
                q.append(neighbor)
                
    print(-1)

if __name__ == '__main__':
    solve()
