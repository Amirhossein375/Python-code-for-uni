import cmath
a = int(input("Inter a :"))
b = int(input("Inter b :"))
c = int(input("Inter c :"))
if a == 0 :
	print("a should not be 0 ") 
else :
	delta = b**2 -4 * a * c
	x1 = -b + cmath.sqrt(delta) / 2*a
	x2 = -b - cmath.sqrt(delta) / 2*a
print(f"x1 is {x1} and x2 is {x2}")
