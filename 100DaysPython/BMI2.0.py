# Enter your height in meters e.g., 1.55
height = float(input("height: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("weight: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight /( height**2)

if bmi < 18.5:
    print (f"You BMI is {bmi}. You are underweight")
elif  18.5 < bmi < 25:
    print (f"You BMI is {bmi}. You have a normal weight")
elif 25 <= bmi < 30:
    print (f"You BMI is {bmi}. You  are slightly overweight")
elif 30 <= bmi < 35:
    print (f"You BMI is {bmi}. You  are obese")
elif bmi >= 35:
    print (f"You BMI is {bmi}. You are clinically obese")