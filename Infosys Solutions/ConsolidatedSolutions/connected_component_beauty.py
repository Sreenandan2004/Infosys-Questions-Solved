import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        # Each component has a set of its elements
        self.elements = [{i} for i in range(n + 1)]
        # Consecutive pairs in each component
        self.consecutive_pairs = [0] * (n + 1)

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by size: merge smaller into larger
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
                
            # Merge root_j into root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            
            # Check for new consecutive pairs when merging
            new_pairs = 0
            for x in self.elements[root_j]:
                if (x - 1) in self.elements[root_i]:
                    new_pairs += 1
                if (x + 1) in self.elements[root_i]:
                    new_pairs += 1
                    
            self.consecutive_pairs[root_i] += self.consecutive_pairs[root_j] + new_pairs
            self.elements[root_i].update(self.elements[root_j])
            self.elements[root_j] = set() # Free memory

    def get_beauty(self, i):
        root = self.find(i)
        # beauty(S) = |S| - consecutive_pairs
        return self.size[root] - self.consecutive_pairs[root]

def solve():
    """
    Connected Component Beauty using DSU with small-to-large merging.
    Time Complexity: O(N log^2 N) using Python sets.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q = int(input_data[1])
    t = int(input_data[2])
    
    dsu = DSU(n)
    ans_sum = 0
    idx = 3
    
    for _ in range(q):
        type_q = int(input_data[idx])
        u = int(input_data[idx+1])
        v = int(input_data[idx+2])
        idx += 3
        
        if type_q == 1:
            dsu.union(u, v)
        else:
            ans_sum += dsu.get_beauty(u)
            
    print(ans_sum)

if __name__ == '__main__':
    solve()
