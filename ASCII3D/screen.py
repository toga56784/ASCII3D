class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = []
        self.fill(' ')
    def fill(self, char):
        self.canvas = [char] * self.width * self.height
    def draw_char(self,x,y,char):
        i = 0
        i += y * self.width
        i += x
        self.canvas[i] = char
    def render(self):
        pass