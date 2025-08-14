from ..config import BRIGHTNESS

class Triangle:
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
    def draw(self, screen, brightness:int):
        screen.draw_char(self.point_1[0], self.point_1[1], BRIGHTNESS[brightness])
        screen.draw_char(self.point_2[0], self.point_2[1], BRIGHTNESS[brightness])
        screen.draw_char(self.point_3[0], self.point_3[1], BRIGHTNESS[brightness])
