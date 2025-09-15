def Add(num1, num2):
    sum = (num1)+(num2)
    return sum
def subtract(num1, num2):
    diff = (num1) - (num2)
    return diff
def multiply(num1 , num2 ):
    multiply = (num1)*(num2)
    return multiply
def division(num1, num2):
     div = (num1)/(num2)
     return div
def  run_calculator():
    display_menu()
    choice = input("Enter your choice (1/2/3/4/q):")
    print("You selected",(choice),".")
    if choice == "q":
         print("Bye!")   
    elif choice != "1"and choice !="2" and choice !="3"and choice !="4" and choice !="q":
         print("Error!: invalid choice.")
         run_calculator()
    else :
         num1 = int(input("Enter the first number:   "))
         num2 = int(input("Enter the second number:   "))
         if choice == "1":
             print("Result : "+ str(num1)+" + "+str(num2)+" = " , Add(num1,num2))
         elif choice == "2":
             print("Result : "+ str(num1)+" - "+str(num2)+" = ", subtract(num1,num2))
         elif choice == "3":
             print("Result : "+ str(num1)+" * "+str(num2)+" = ", multiply(num1,num2))
         elif choice == "4":
             if num2 > num1 or num1 == 0 or num2 == 0 :
                 print("data error")
             else:
                 div_1 = "{:.2f}".format(division(num1,num2))
                 print("Result : "+ str(num1)+" / "+str(num2)+" = ", div_1)
         run_calculator()
def display_menu():
    print("Select an option:   ")
    print("1.Add")
    print("2.Subtraction")
    print("3.Multiply")
    print("4.Division")
    print("q.Quit")
def main():
    run_calculator()
if __name__ == "__main__":
    main()