from math import radians as rad
from math import tan as tg 
from math import pi 

#the first task
degree = int(input("Input degree:"))
radian = rad(degree) 
print("Output radian:", radian)

#the second task
height = int(input("Height: "))
base_1 = int(input("Base, first value: "))
base_2 = int(input("Base, second value: "))
area_trap = height * (base_1 + base_2)/2
print("Expected Output:", int(area_trap))

#the third task
n = int(input("Input number of sides: "))
a = float(input("Input the length of a side: "))
area = (n * a * a) / (4 * tg(pi / n))
print("The area of the polygon is: ", area)
#the last task
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print("Expected Output: ", area)

