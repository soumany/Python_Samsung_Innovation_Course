x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

if x > 0 and y > 0:
    quadrant = 1
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
elif x > 0 and y < 0:
    quadrant = 4
else:
    quadrant = "On the axis or origin"

print("The point is in quadrant", quadrant)