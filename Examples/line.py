import ASCII3D as a3d

screen = a3d.Screen(40,20)

screen.fill('.')
a3d.draw_line(2, 2, 5, 5, screen, '#')

screen.render()