#!/usr/bin/python

# hydration percent for bakers. totalWater/totalFlour * 100%.
# sourdough starter is usually a 50/50 mix.

# todo, could make hydration target calculator

totalWater = 0
totalFlour = 0

sourdoughFlag = input("Is this a sourdough recipe? Y/n: ")
if ( sourdoughFlag.upper() == "Y"):
    totalWater += float(input("Input water amount in starter in grams: "))
    # totalWater += sourdoughWater
    totalFlour += float(input("Input flour amount in starter in grams: "))
    # totalFlour += sourdoughFlour
totalWater += float(input("Input water amount in grams: "))
totalFlour += float(input("Input flour amount in grams: "))

hydrationPercent = ((totalWater/totalFlour)*100)

print(f"total water is: {totalWater}")
print(f"total flour is: {totalFlour}")

print(f"hydration percent: {hydrationPercent}%")
