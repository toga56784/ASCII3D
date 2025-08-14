import os

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw_line(x0, y0, x1, y1, screen, char):
    dx = x1-x0
    dy = y1-y0
    if dx != 0:
        gradient = dy/dx
        for i in range(dx+1):
            screen.draw_char(x0+i, round(y0+i * gradient), char)
