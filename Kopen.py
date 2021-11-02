from math import sqrt, acos, degrees

# координаты A - центр робота
Ax = 30
Ay = 10

# координаты B - перед робота
Bx = 35
By = 20

# координаты C - куда надо повернуться
Cx = 10
Cy = 10

c = sqrt((Ax-Bx)*(Ax-Bx) + (Ay-By)*(Ay-By))
b = sqrt((Ax-Cx)*(Ax-Cx) + (Ay-Cy)*(Ay-Cy))
a = sqrt((Cx-Bx)*(Cx-Bx) + (Cy-By)*(Cy-By))

print(a, b, c)

a2 = a*a
b2 = b*b
c2 = c*c

angle_alpha = degrees(acos((b2+c2-a2)/(2*b*c)))
print(angle_alpha)