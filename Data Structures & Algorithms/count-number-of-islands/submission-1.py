class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        breadth first search solution
        '''

        #if grid is empty, return 0 islands
        if not grid:
            return 0

        #intialize vars
        #rows = len(grid) aka num of arrays in 2d arr
        #cols = len(grid[0]) aka num of elements in arr
        rows, cols = len(grid), len(grid[0])

        #set of visited points:
        #takes in tuples of (rowNum, colNum)
        #could also use a 2d array, filled w/ false and set to true when visited
        visit = set()

        #num of islands
        islands = 0

        #breadth first search algo
        def bfs(r, c):

            #init a de queue
            q = collections.deque()

            #add curr to set, and append to queue
            visit.add((r, c))
            q.append((r, c))

            #while queue is not empty
            while q:

                #pop element from left od queue
                row, col = q.popleft()

                #one to the right, one to the left, one below, and one above
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                
                for dr, dc in directions:
                    #r is new row coord, c is new col coord
                    r, c = row + dr, col + dc

                    if ((r) in range(rows) and #if r is in the matrix
                    (c) in range(cols) and # if c is in the matrix
                    grid[r][c] == "1" and #must be on land
                    (r, c) not in visit): # must not already be visited
                        q.append((r, c)) # add to the end of the queue
                        visit.add((r, c)) # add to visited

        #iterate through entire matrix
        for r in range(rows):
            for c in range(cols):
                #if element is an island, and has not been visited
                #run bfs and add to the island
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        #return num of islands
        return islands