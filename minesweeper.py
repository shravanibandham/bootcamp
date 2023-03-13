grid=[["-","-","-","#","#"],
["-","#","-","-","-"],
["-","-","#","-","-"],
["-","#","#","-","-"],
["-","-","-","-","-"]]
for row_index in range(len(grid)):
    #print(f"row index: {row_index}")
    count=0
    #print(len(grid[row_index]))
    for col_index in range(len(grid[row_index])):
        #print(f"value at column index {col_index} is: {grid[row_index][col_index]}")
         
        if grid[row_index][col_index] == "-":

            if grid[row_index-1][col_index-1] == '#':
                count += 1
            if grid[row_index-1][col_index+1] == '#':
                count += 1
            if grid[row_index][col_index-1] == '#':
                count += 1
            if grid[row_index][col_index+1] == '#':
                count += 1
            if grid[row_index+1][col_index-1] == '#':
                count += 1
            if grid[row_index+1][col_index] == '#':
                count += 1
            if grid[row_index+1][col_index+1] == '#':
                count += 1
    grid[row_index][col_index] = count                                 
