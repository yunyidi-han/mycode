#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

print("Easy:")
for farm in farms:
	if farm['name'] == "NE Farm":
		for animal in farm['agriculture']:
			print(animal)

print("Medium:")
#could make easy a method with variable and call it here but meeeeeeeeeh
choice = input("Please pick a farm from ['NE Farm', 'W Farm', 'SE Farm']: ") 
for farm in farms:
	if farm['name'] == choice: #no input validation here...
		for animal in farm['agriculture']:
			print(animal)

print("Hard:")
notAnimals = ["carrots","celery"]
choice = input("Please pick a farm from ['NE Farm', 'W Farm', 'SE Farm']: ") 
for farm in farms:
	if farm['name'] == choice: #no input validation here...
		for animal in farm['agriculture']:
			if animal not in notAnimals:
				print(animal)
