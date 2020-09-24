#!/usr/bin/env python3

num = int(input("How many asterisks do you want in the largest row: "))

for a in range(1,num+1):
	print("* "*a)
for b in range(num-1,0,-1):
	print("* "*b)
		
	
