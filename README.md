# Navttc-Task-09-BMI-Calculator

# BMI Calculator

## Description

This Python script calculates the Body Mass Index (BMI) based on a user's height in centimeters and weight in kilograms. It also categorizes the BMI result into one of the following categories: Severely underweight, Underweight, Normal weight, Overweight, or Obese.

## Code

```python
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
```

## Steps

1. **Input Height and Weight:**
   - Prompt the user to input their height in centimeters and weight in kilograms.

2. **Convert Height to Meters:**
   - Convert the height from centimeters to meters by dividing by 100.

3. **Calculate BMI:**
   - Calculate the BMI using the formula:
     ```python
     BMI = weight / (Height * Height)
     ```

4. **Print the BMI:**
   - Output the calculated BMI to the user.

5. **Determine the BMI Category:**
   - Based on the BMI value, the script categorizes the result into one of the following:
     - Severely underweight (BMI ≤ 16)
     - Underweight (BMI ≤ 18.5)
     - Normal weight (BMI ≤ 25)
     - Overweight (BMI ≤ 30)
     - Obese (BMI > 30)

## How to Run

1. **Ensure Python is Installed:**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Save the Script:**
   - Save the provided Python code into a file named `09 - BMI Calculator(Nasir Sharif).py`.

3. **Execute the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `09 - BMI Calculator(Nasir Sharif).py` is saved.
   - Run the script using the following command:
     ```bash
     python 09 - BMI Calculator(Nasir Sharif).py
     ```

4. **Enter Height and Weight:**
   - Input your height in centimeters and weight in kilograms as prompted.

5. **View Output:**
   - The script will display your BMI and the corresponding category.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact Nasir Sharif at nasirsharifqasoori786@gmail.com
