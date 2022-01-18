import time

class Button():
    def __init__(self, x, y, toggle = False, size = 10, name = None):
        self.x = x
        self.y = y
        self.w = size * 3
        self.h = size
        self.name = name
        self.text_size = size / 2
        self.toggle = toggle

        # Optimizations
        self._text_x = self.x + self.w / 2
        self._text_y = self.y + self.h / 2

        self._btm_rght_x = self.x + self.w
        self._btm_rght_y = self.y + self.h

    def draw(self):
        if self.toggle:
            fill(0, 200, 40, 150)
        else:
            fill(240, 0, 0, 150)

        rect(self.x, self.y, self.w, self.h)
        if self.name != None:
            # strokeWeight(5)
            fill(255)
            textSize(self.text_size)
            textAlign(CENTER, CENTER)
            text(self.name, self._text_x, self._text_y)

    def on_click(self, grid):
        if self.x < mouseX and \
        mouseX < self._btm_rght_x and \
        self.y < mouseY and \
        mouseY < self._btm_rght_y:
            self.toggle = not self.toggle

            if self.name == 'RESET':
                grid.clear()
                grid.just_reset = True
                self.toggle = not self.toggle
            elif self.name == 'PPT':
                grid.run = not self.toggle
