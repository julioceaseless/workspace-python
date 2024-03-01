#!/usr/bin/env python3
import sys
sys.path.append('/home/julio/Workspace-Python/init_play')

from add import add

def mul (a, b):
	return a * b

if __name__ == "__main__":
	my_sum = add(3, 4)
	print(f"sum is: {my_sum}")
	product = mul(3, 4)
	print(f"Product of 3 by 4 is {product}");
