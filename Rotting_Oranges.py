class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])
        direction = [(-1,0),(0,1),(1,0),(0,-1)]
        fresh=set()
        rotten = collections.deque()
        step = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j]==1:
                    fresh.add((i,j))
                elif grid[i][j]==2:
                    rotten.append([i,j,step])
        while rotten:
            i,j,step = rotten.popleft()
            for di, dj in direction:
                if 0<=i+di<row and 0<=j+dj<column and grid[i+di][j+dj] == 1:
                    grid[i+di][j+dj]=2
                    fresh.remove((i+di,j+dj))
                    rotten.append([i+di,j+dj,step+1])
        return step if not fresh else -1
        