from Button import Button
from Grid import Grid
from MinHeap import MinHeap
import math

SCR_W = 1000
SCR_H = 700

GRID_WIDTH = 800

BTN_X = 825
BTN_H = 50
BTN_MARGIN = 20


# Button Setup
names = ['SET A', 'SET B', 'ERASER', 'PPT', 'RESET']
buttons = {}

for i in range(len(names)):
    buttons[names[i]] = Button(BTN_X, BTN_H + i * (BTN_H + BTN_MARGIN), size = BTN_H, name = names[i])


# Grid Setup
grid = Grid(endX = GRID_WIDTH, endY = SCR_H, nx = 8)
open = MinHeap([])

def setup():
    size(SCR_W, SCR_H)

def draw():
    global open, closed
    #frameRate(0.5)
    background(255)

    stroke(255)
    line(GRID_WIDTH, 0, GRID_WIDTH, height)
    
    for name in names:
        buttons[name].draw()

    if grid.just_reset:
        open = MinHeap([])
        grid.just_reset = False

    A, B = grid.getAB()
    #print('A:', A, 'B:', B)
    if A != None and B != None and grid.flag:
        open.insert(A)
        grid.flag = False

    if grid.run:
        if grid.flag == False and grid.path_found == False:
            try:
                x = open.extract_min()
                x.explored = True

                if x == B:
                    grid.path_found = True

                for sq in grid.neighbours(x.idx):
                    open = sq.calculate(A, B, open, x)
                
            except IndexError:
                grid.path_found = True
        
    elif grid.take_step:
        if grid.flag == False and grid.path_found == False:
            try:
                x = open.extract_min()
                x.explored = True

                if x == B:
                    grid.path_found = True

                for sq in grid.neighbours(x.idx):
                    open = sq.calculate(A, B, open, x)
            except IndexError:
                grid.path_found = True

        grid.take_step = False
    
    for sq in grid.squares:
        if sq.explored:
            sq.color = (255, 0, 0, 255)

    if grid.path_found:
        x = B
        while x != None:
            x.color = (0, 0, 240, 170)
            x = x.parent


    grid.draw()


def mouseClicked():
    grid.take_step = True
    for name in names:
        buttons[name].on_click(grid)

    for sq in grid.squares:
        buttons['SET A'].toggle, buttons['SET B'].toggle = sq.on_click(buttons['SET A'].toggle, buttons['SET B'].toggle, buttons['ERASER'].toggle)
