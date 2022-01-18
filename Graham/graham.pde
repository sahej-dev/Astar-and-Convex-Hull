import math

def sort_by_y(point):
    return -point.y

def sort_by_theta(point):
    return point.theta

class Point():
    def __init__(self, x, y, size = 10):
        self.x = x
        self.y = y
        self.size = size
        self.theta = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(round(self.theta, 2)) + ')'


    def draw(self, i, label = False):
        #text('p' + str(i), self.x + 10, self.y + 10)
        fill(255)
        noStroke()
        ellipse(self.x, self.y, self.size, self.size)

        if label:
            stroke(255, 0, 0)
            #text('p' + str(i) + ' ' + str(self), self.x + 10, self.y + 10)
            text('p' + str(i), self.x + 10, self.y + 10)

    def to_vec(self):
        return PVector(self.x, self.y)


class Stack():
    def __init__(self):
        self.l = []

    def push(self, x):
        self.l.append(x)

    def pop(self):
        self.l.pop()

    def top(self):
        return self.l[-1]

    def next_to_top(self):
        return self.l[-2]

    def draw(self, last_line = False):
        n = len(self.l)
        stroke(255)
        for i in range(n - 1):
            line(self.l[i].x, self.l[i].y, self.l[i + 1].x, self.l[i + 1].y)

        if last_line:
            line(self.l[-1].x, self.l[-1].y, self.l[0].x, self.l[0].y)

points = []
p0 = None
MAX_POINTS = 500

def setup():
    randomSeed(123)
    global points, p0

    size(800, 800)
    w2, h2 = width / 3, height / 3
    for i in range(MAX_POINTS):
        points.append(Point(int(random(-w2, w2) + 0.5), int(random(-h2, h2) + 0.5)))

    points = sorted(points, key=sort_by_y)
    p0 = points[0]
    points = points[1:]

    for point in points:
        #point.theta = (PI + atan2((-point.y + p0.y), (point.x - p0.x)) ) % (2 * PI)
        point.theta = atan2((-point.y + p0.y), (point.x - p0.x)) 

    points = sorted(points, key=sort_by_theta)


j = 1
S = Stack()

def draw():
    global S, p0, points, j

    #frameRate(3)
    background(0)
    translate(400, 400)

    fill(255, 0, 0)
    ellipse(0, 0, 10, 10)

    p0.draw(0, label = True)
    for i in range(MAX_POINTS - 1):
        points[i].draw(i + 1)

    if j == 1:
        S.push(p0)
        S.push(points[0])
        S.push(points[1])

    if j > 1 and j < MAX_POINTS - 1:
        while len(S.l) > 2:
            p1 = S.next_to_top().to_vec()
            p2 = S.top().to_vec()
            p3 = points[j].to_vec()

            A = PVector.sub(p2, p1)
            B = PVector.sub(p1, p3)

            c = (A.cross(B)).z
            if c <= 0:
                S.pop()
            else:
                break
        
        S.push(points[j])

    j += 1

    if j == MAX_POINTS - 1:
        S.draw(last_line = True)
        noLoop()
    else:
        S.draw()

        