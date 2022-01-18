class Square():
    def __init__(self, x, y, size, idx, obstacle = False, color = None):
        self.x = x
        self.y = y
        self.size = size

        self.isA = False
        self.isB = False
        self.obstacle = obstacle
        self.explored = False
        self.parent = None

        self.text_size = size / 3

        self.color = color

        self.idx = idx
        self.g = None
        self.h = None
        if self.g is not None and self.h is not None:
            self.f = self.g + self.h
        else:
            self.f = None
    
        # Opmimizations
        self._text_x = self.x + self.size / 2
        self._text_y = self.y + self.size / 2

        self._text_left_x = self.x + self.size / 10
        self._text_rght_x = self.x + 0.9 * self.size

        self._btm_rght_x = self.x + self.size
        self._btm_rght_y = self.y + self.size


    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


    def __lt__(self, other):
        if self.f != other.f:
            return self.f < other.f
        
        return self.h < other.h


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def draw(self, i = None):
        if self.isA or self.isB:
            textSize(self.text_size)
            textAlign(CENTER, CENTER)
            fill(0, 0, 240, 170)
            rect(self.x, self.y, self.size, self.size)
            fill(255)
            text('A' if self.isA else 'B', self._text_x, self._text_y)
            return
        elif self.obstacle:
            fill(20)
            rect(self.x, self.y, self.size, self.size)
            return
        elif self.color is None:
                noFill()
        else:
            r, g, b, a = self.color
            fill(r, g, b, a)  

        rect(self.x, self.y, self.size, self.size)

        if i is not None:
            fill(0)
            text(i, self._text_x, self._text_y)

        if self.f != None:
            fill(0)
            textSize(self.text_size)
            textAlign(CENTER, CENTER)
            text(str(self.f), self._text_x, self._text_y)

            textSize(self.text_size / 2)
            textAlign(LEFT, TOP)
            text(str(self.g), self._text_left_x , self.y)

            textAlign(LEFT, TOP)
            h = str(self.h)
            text(h, self._text_rght_x - textWidth(h), self.y)

            """
            if self.parent != None:
                textAlign(LEFT, TOP)
                h = str(self.h)
                text(str(self.parent.f), self._text_rght_x - textWidth(str(self.parent.f)), 0.9*self._btm_rght_y)
            """

    
    def on_click(self, setA = False, setB = False, erase = False):
        if self.x < mouseX and \
        mouseX < self._btm_rght_x and \
        self.y < mouseY and \
        mouseY < self._btm_rght_y:
            if erase:
                self.clear()
            elif setA:
                self.isA = True
                self.g = 0
            elif setB:
                self.isB = True
                self.h = 0
            else:
                self.obstacle = not self.obstacle

            return False, False

        return setA, setB


    def clear(self):
        self.obstacle = False
        self.isA = False
        self.isB = False
        self.color = None
        self.f = None
        self.g = None
        self.h = None
        self.explored = False
        self.parent = None


    def calculate(self, A, B, open, x):

        g = int(round(sqrt((x.x - self.x)**2 + (x.y - self.y)**2) / self.size, 1) * 10)
        g += x.g
        h = int(round(sqrt((B.x - self.x)**2 + (B.y - self.y)**2) / self.size, 1) * 10)

        f = g + h

        if self.f != None and f < self.f:
            self.parent = x
        elif self.f == None:
            self.parent = x

        if self.explored:
            if f < self.f:
                self.f = f
                self.g = g
        else:
            g = int(round(sqrt((A.x - self.x)**2 + (A.y - self.y)**2) / self.size, 1) * 10)

            f = g + h
            self.f = f
            self.g = g
            self.h = h
            self.color = (0, 240, 0, 150)
            open.insert(self)
        

        return open