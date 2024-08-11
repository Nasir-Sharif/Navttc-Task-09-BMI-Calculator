height = float(input("Enter the Height in CM: "))
weight = float(input("Enter the Weight in Kilograms: "))

# Convert height from cm to meters
Height = height / 100

# Calculate BMI
BMI = weight / (Height * Height)

print("Your Body Mass Index (BMI):", BMI)

# Determine the BMI category
if BMI <= 16:
    print("Severely underweight")
elif BMI <= 18.5:
    print("Underweight")
elif BMI <= 25:
    print("Normal weight")
elif BMI <= 30:
    print("Overweight")
else:
    print("Obese")
