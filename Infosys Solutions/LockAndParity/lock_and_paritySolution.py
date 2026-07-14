import sys

def solve():
    """
    Finds the minimum cost of a valid lock and key assignment.
    As proven, the minimum cost is always the minimum cost of a single even edge.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    L = [int(x) for x in input_data[1:n+1]]
    
    min_cost = float('inf')
    
    # Check all pairs (j, i) with j < i
    for i in range(n):
        for j in range(i):
            # Assignment key j to lock i is valid if L[j] != L[i]
            # and the effective value is even.
            if L[j] != L[i] and (L[j] - L[i]) % 2 == 0:
                cost = abs(L[j] - L[i])
                if cost < min_cost:
                    min_cost = cost
                    
    if min_cost == float('inf'):
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    solve()
