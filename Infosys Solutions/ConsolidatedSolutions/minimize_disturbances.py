import sys

def get_disturbances(x, n, c, A):
    level = x
    dist = 0
    for i in range(n):
        if A[i] == 1:
            if level == c:
                dist += 1
            else:
                level += 1
        else: # A[i] == -1
            if level == 0:
                dist += 1
            else:
                level -= 1
    return dist

def solve():
    """
    Naive solution for Oil Tank Disturbances.
    Directly tests all possible initial oil values X in [0, C] and takes the minimum.
    Time Complexity: O(C * N)
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    c = int(input_data[1])
    A = [int(x) for x in input_data[2:n+2]]
    
    min_dist = float('inf')
    best_x = -1
    
    # Try all possible initial oil levels X
    for x in range(c + 1):
        dist = get_disturbances(x, n, c, A)
        if dist < min_dist:
            min_dist = dist
            best_x = x
            
    print(best_x)

if __name__ == '__main__':
    solve()
