Name = input("what is your name: ")
print(Name)
weight = float(input("what is your weight in your kilo: "))
print(weight)
height = float(input("what is your height in meter: "))
print(height)
BMI = round(weight/(height*height), 2)
# print(Name + "BMI is" + str(BMI))
if (BMI<18.5):
    print(Name+" underweight "+ str(BMI))
elif (18.5<=BMI) and (BMI<=24.9):
    print(Name+" healthy "+ str(BMI))
elif (25.0<=BMI) and (BMI<=29.9):
    print(Name+" overheight "+ str(BMI))
else:
    print(Name+" obese "+ str(BMI))      
