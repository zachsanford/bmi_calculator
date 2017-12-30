#!/usr/bin/env python3

# Author: Zachary Sanford (@zachsanford)
# Published Dec 20th, 2017

print("**************** BMI Calculator ****************\n")
print("Hello, let's figure out your Body Mass Index!\n")
lbs = int(input("Please enter your weight in pounds (lbs) >> "))
inches = int(input("\nPlease enter your height in inches >> "))

def poundsToKilos(var):
	kilos = var * 0.45359237
	return kilos

kg = poundsToKilos(lbs)

def inchesToMeters(x):
	meters = x * 0.0254
	return meters

m = inchesToMeters(inches)

def bodyMassIndex(weight,height):
	y = weight / (height ** 2)
	return y

bmi = bodyMassIndex(kg,m)

print("\nYour BMI is",bmi)
if bmi >= 30:
	print("\nYour BMI Category is OBESITY.")
elif bmi >= 25:
	print("\nYour BMI Category is OVERWEIGHT.")
elif bmi >= 18.5:
	print("\nYour BMI Category is NORMAL WEIGHT.")
else:
	print("\nYour BMI Category is UNDERWEIGHT.")
