import ASCII3D as a3d

screen = a3d.Screen(40,20)

screen.fill('.')

triangle_1 = a3d.Triangle((1,1), (4,4), (1,4))
triangle_1.draw(screen, 3)

screen.render()