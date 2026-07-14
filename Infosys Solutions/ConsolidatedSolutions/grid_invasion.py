import sys

def solve():
    """
    Naive solution for Grid Invasion.
    Simulates the invasion process second by second.
    Time Complexity: O((N * M)^2)
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    grid_rows = input_data[2:n+2]
    
    # Convert grid to a 2D list for mutability
    grid = [list(row) for row in grid_rows]
    
    enemy_count = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'E':
                enemy_count += 1
                
    if enemy_count == 0:
        print(0)
        return
        
    seconds = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while True:
        invaded_this_second = []
        
        # Check all cells to find E cells adjacent to an A cell
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 'E':
                    is_adjacent_to_A = False
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if 0 <= nr < n and 0 <= nc < m:
                            if grid[nr][nc] == 'A':
                                is_adjacent_to_A = True
                                break
                    if is_adjacent_to_A:
                        invaded_this_second.append((r, c))
                        
        # If no new cells were invaded, simulation is finished
        if not invaded_this_second:
            break
            
        # Perform the invasion
        for r, c in invaded_this_second:
            grid[r][c] = 'A'
            enemy_count -= 1
            
        seconds += 1
        
    # If there are remaining uninvaded enemy cells, it is impossible
    if enemy_count > 0:
        print(-1)
    else:
        print(seconds)

if __name__ == '__main__':
    solve()
