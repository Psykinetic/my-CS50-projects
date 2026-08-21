"""This program calculates the Energy present
in a system based on user-specified mass and
the speed of light"""

m = int(input("m (kg): "))
c = 3 * pow(10, 8)
print("E:", m * pow(c, 2), "J")
