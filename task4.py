from typing import List

def numIslands(grid: List[List[str]]) -> int:
    r = len(grid)                 
    if r == 0:                    
        return 0 
    c = len(grid[0])              
        
    def DFS(i, j):                
        if grid[i][j] == '1':     
            grid[i][j] = '0'      
            if i > 0:             
                DFS(i-1, j)
            if i < r - 1:         
                DFS(i+1, j)   
            if j > 0:             
                DFS(i, j-1)   
            if j < c-1:  
                DFS(i, j+1)        
                
    count = 0                     
    for i in range(r):            
        for j in range(c):        
            if grid[i][j] == '1': 
                count += 1        
                DFS(i, j)         
    return count 