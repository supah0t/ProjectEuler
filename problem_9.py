#Finds Pythagorean triplets

import math
from sys import exit

for x in range(1, 400):
	for y in range(1, 400):
		result = x*x + y*y
		z = math.sqrt(result)
		if z.is_integer():
			if (x + y + z == 1000):
				print(x * y * z)
				exit()