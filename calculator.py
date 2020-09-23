#!/usr/bin/env python3

def add(a,b):
	result = a + b
	print(result)
	
def subtract(a,b):
	result = a - b
	print(result)
	
def divide(a,b):
	result = a / b
	print(result)
	
def multiply(a,b):
	result = a * b
	print(result)
	
def validate(a):
	try: 
		float(a)
		return True
	except ValueError:
		return False
	
def main():
	a = ''
	while not isinstance(a,float):
		num1 = input("Please input the first number: ")
		if validate(num1):
			a = float(num1)
	b = ''
	while not isinstance(b,float):
		num2 = input("Please input the second number: ")
		if validate(num2):
			b = float(num2)
	operations = ["+","-","/","*","add","subtract","divide","multiply"]
	operator = ''
	while operator not in operations:
		operator = input(f"Please choose {operations}: ").lower()
	a = float(a)
	b = float(b)
	if operator == "add" or operator == "+":
		add(a,b)
	elif operator == "subtract" or operator == "-":
		subtract(a,b)
	elif operator == "divide" or operator == "/":
		divide(a,b)
	elif operator == "multiply" or operator == "*":
		multiply(a,b)
		
main()
	
