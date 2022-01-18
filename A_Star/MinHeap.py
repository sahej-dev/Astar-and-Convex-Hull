from Square import Square

class MinHeap():
    def __init__(self, squares):
        self.squares = []
        for sq in squares:
            if sq.f != None:
                self.squares.append(sq)

        self.size = len(self.squares)


    def println(self):
        print(self.squares)


    def parent(self, i):
        return i >> 1


    def left(self, i):
        l = (i << 1) + 1

        if l < self.size:
            return l
        
        return -1


    def right(self, i):
        r = (i << 1) + 2

        if r < self.size:
            return r

        return -1


    def min_heapify(self, i):
        smallest = i
        l = self.left(i)
        r = self.right(i)

        if l != -1 and self.squares[l] <  self.squares[smallest]:
            smallest = l

        if r != -1 and self.squares[r] < self.squares[smallest]:
            smallest = r

        if smallest != i and i < self.size / 2:
            self.squares[i], self.squares[smallest] = self.squares[smallest], self.squares[i]
            self.min_heapify(smallest)


    def min_heapify_btm_up(self, i):
        largest = i
        parent = self.parent(i)
        if self.squares[largest] < self.squares[parent]:
            self.squares[largest], self.squares[parent] = self.squares[parent], self.squares[largest]
            if parent == 0:
                return
            self.min_heapify_btm_up(parent)
        

    
    def gen_min_heap(self):
        max = int((self.size - 1) / 2)
        for i in range(max, -1, -1):
            self.min_heapify(i)


    def extract_min(self):
        self.squares[0], self.squares[self.size - 1] = self.squares[self.size - 1], self.squares[0]
        x = self.squares.pop()
        self.size -= 1
        self.min_heapify(0)

        return x

    def insert(self, x):
        # self.squares.insert(0, x)
        self.squares.append(x)
        self.size += 1
        self.min_heapify_btm_up(self.size - 1)


    def close_init(self, squares):
        self.squares = []
        for sq in squares:
            if sq.explored and sq.f != None:
                self.squares.append(sq)

        self.size = len(self.squares)