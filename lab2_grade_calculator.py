Name = input("enter your name: " )
A = float(input("The obtained of marks english is: "))
B = float(input("The obtained marks of maths is: "))
C = float(input("The obtained marks of science is: "))
if ((100>A>0) and (100>B>0) and (100>C>0)):
    total= A+B+C
print(total)
full_mark = 300
percentage = total/full_mark*100
print(percentage)
if percentage>80 and percentage<=100:
    print("The distinction")
elif percentage>70 and percentage<=80:
    print("The First Division")
elif percentage>60 and percentage<=70:
    print("The second division")
elif percentage>50 and percentage<=60:
    print("The Third division")
elif percentage<50 and percentage>40:
        print("fail")
else:
    print("please check the entered grades again")
    title="----------THANK you--------"
    print(title)