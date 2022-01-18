from Square import Square

class Grid():
    def __init__(self, endX, endY, nx=None, startX = 0, startY = 0):
        self.path_found = False
        self.flag = True
        self.just_reset = False
        self.run = True
        self.take_step = False

        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        if nx is None:
            self.nx = 18
        else:
            self.nx = nx

        self.sq_size = (self.endX - self.startX) / self.nx
        self.ny = (self.endY - self.startY) / self.sq_size

        self.squares = []
        for i in range(0, self.endX, self.sq_size):
            for j in range(0, self.endY, self.sq_size):
                self.squares.append(Square(i, j, self.sq_size, j / self.sq_size + (i / self.sq_size) * self.ny))

    
    def draw(self):
        stroke(0)
        strokeWeight(1)
        for i in range(len(self.squares)):
            self.squares[i].draw()


    def clear(self):
        self.path_found = False
        self.flag = True
        for sq in self.squares:
            sq.clear()


    def neighbours(self, idx, Aidx = None):
        nx, ny = self.nx, self.ny
        l = [idx - ny - 1, idx - 1, idx + ny - 1,
             idx - ny    ,          idx + ny    ,
             idx - ny + 1, idx + 1, idx + ny + 1]

        max = nx * ny
        if idx % ny == 0:
            l = l[3:]
        elif (idx + 1) % ny == 0:
            l = l[:-3]

        res = [i for i in l if 0 <= i < max]
        
        obstacles = []
        for i in res:
            if self.squares[i].obstacle or self.squares[i].explored:
                obstacles.append(i)

        for i in obstacles:
            res.remove(i)

        if Aidx in res:
            self.backtrack = True

        return [self.squares[i] for i in res]

    
    def getAB(self):
        A, B = None, None
        for sq in self.squares:
            if sq.isA:
                A = sq
            elif sq.isB:
                B = sq
            
            if A != None and B != None:
                break
        
        return A, B
