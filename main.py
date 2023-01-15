import random

def calculate_bac():
    # Constants for alcohol density and metabolism rate
    # metabolism rate for men: 0.015; for women: 0.01
    # using 0.01 for simplicity
    m = 0.01
    weight = float(input("What is your weight in kg? "))
    gender = input("What is your gender (m/f)? ")
    if gender == "m":
        r = 0.68
    elif gender == "f":
        r = 0.55
    else:
        print("Invalid input. Using default value for 'm'")
        r = 0.68
    bac = 0
    beer = float(input("How many liters of beer have you consumed? "))
    wine = float(input("How many liters of wine have you consumed? "))
    cocktail = float(input("How many liters of cocktail have you consumed? "))
    schnaps = float(input("How many liters of schnaps have you consumed? "))
    bac += (beer * 00.514) / (weight * r)
    bac += (wine * 00.1269) / (weight * r)
    bac += (cocktail * 00.1800) / (weight * r)
    bac += (schnaps * 00.4000) / (weight * r)
    time_elapsed = int(input("How much time has passed since your first drink in minutes? "))
    bac = bac * 100 - (m * (time_elapsed / 60))
    bac = round(bac, 2)
    if bac <= 0:
        print("You are sober.")
    else:
        sober_time = bac / m
        print(f"Your blood alcohol content is: {bac}%")
        if beer > 0 and wine > 0 and cocktail > 0 and schnaps > 0:
            print("Your upcoming hangover will be severe due to mixing multiple types of alcohol.")
        elif bac < 0.2:
            print("Your upcoming hangover will be light.")
        elif bac < 0.5:
            print("Your upcoming hangover will be moderate.")
        else:
            print("Your upcoming hangover will be severe.")
        print(f"You will be sober in approximately {sober_time:.2f} hours.")
        hangover_cures = ["drink water", "sleep", "take painkillers", "eat a healthy meal", "exercise", "take a shower", "drink sports drink", "drink coconut water", "drink tea", "take a nap", "avoid alcohol", "avoid caffeine", "avoid cigarettes", "avoid greasy foods", "avoid bright lights", "avoid loud noises", "avoid stress", "avoid spicy food", "avoid any other alcohol"]
        print("A recommended hangover cure is to: " + random.choice(hangover_cures))
        if bac >= 0.5:
            print("It is illegal to operate a vehicle in this state.")
        elif bac >= 0.2:
            print("It is not recommended to operate a vehicle in this state.")
calculate_bac()