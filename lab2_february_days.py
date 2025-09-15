feb=int(input("enter the year: "))
if(feb%400==0):
    print("This year is leap year")
else:
    if(feb%100==0):
        print("This year is not leap year")
    else:
        if(feb%4==0):
            print("This year is leap year")
        else:
            print("This year is not leap year")

