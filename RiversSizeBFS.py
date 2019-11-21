def riversize(matrix):
    res = []    #   collecting all river sizes to an array
    visited = {}    #   tracking visited nodes (indexes)
    q = []  #   nodes queue for BFS
    
    #   traversal and BFS in single flow
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            #   skip 0 elements at current idx, and visited idxs
            if matrix[i][j] != 0 and (i,j) not in visited:
                q.append((i,j)) #   appending idx of next appeared 1          
                counter = 0 #   reseting river size counter to 0 to start count for next river
            #   while q is not empty, keep checking all river branches
            while len(q) > 0:
                current = q.pop()   #   dequeuing last river branch
                #   checking if branch has been visited or not                 
                if current not in visited:
                    counter += 1    #   inrementing length of the current river
                    visited[current] = True #   marking brancg as visited
                    ii = current[0] # tuple's 1st ids
                    jj = current[1] # tuple's 2nd ids
                    #   if current branch connected has 1 as its neighbor, appending neighbor to the queue
                    if ii-1 >= 0 and matrix[ii-1][jj] == 1 and (ii-1, jj) not in visited:
                        q.append((ii-1, jj))
                        
                    if ii+1 < len(matrix) and matrix[ii+1][jj] == 1 and (ii+1, jj) not in visited:
                        q.append((ii+1, jj))

                    if jj-1 >= 0 and matrix[ii][jj-1] == 1 and (ii, jj-1) not in visited: 
                        q.append((ii, jj-1))
        
                    if jj+1 < len(matrix[0]) and matrix[ii][jj+1] == 1 and (ii, jj+1) not in visited:
                        q.append((ii, jj+1))
                if len(q) == 0:
                    res.append(counter)
    return res

# test case
river = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ]
river2 = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]


print(riversize(river))

print(riversize(river2))