#BMI Categories

# Your height in m: 1.75

height = float(input("What is your height? "))
weight = int(input("What is your weight? "))
print()

bmi = weight / (height*height)

print("YOUR BMI:", bmi)
print()


if bmi < 18.5:
    print("You are underweight")
elif bmi > 18.5 and bmi < 24.9:
    print("You are normal weight")
elif bmi > 24.9 and bmi < 29.9:
    print("You are overweight")
elif bmi > 30.0: 
    print("You are fat")
else: 
    print("Error")