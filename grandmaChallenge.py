#!/usr/bin/env python3

plate = ["steak","brocolli","beans","carrots","brocolli"]
count = 0
for food in plate:
	if food.lower() == "brocolli":
		count += 1
		print(f"I found {count} brocolli on your plate... *SLAP*")
		
bank = 25
room = ["light","dark","light","dark","light"]
print(f"You start with {bank} dollars")
countL = 0
for light in room:
	if light.lower() == "light":
		bank -= 1
		countL += 1
		print(f"Grandma found {countL} light(s) on... she took a dollar... you have {bank} dollars left")		

piggyBank = 0
print(f"Your piggy bank starts with {piggyBank} cents")
ground = ["penny","penny","penny","dime","penny","quarter","penny","dollar"]
for money in ground:
	if money.lower() == "penny":
		piggyBank += 1
		print(f"Grandma found a penny on the ground! She gave it to you and now you have {piggyBank} cents in your piggy bank!")
