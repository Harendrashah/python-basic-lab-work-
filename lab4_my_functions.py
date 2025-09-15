def greeting():
    print("we are doing lab 2 this week.")
def greeting2(name):
    print("I hope you are doing fine,{0}".format(name))
def add(num1,num2):
    s= num1+num2
    return s
def cal_division(num1,num2):
    division=num1/num2
    result_division=format(division,".2f")
    print("the division of %d and %d is %f"%(num1,num2,division))
    
def main():
    greeting()
    greeting2("mate")
    print(add(2,4))
    cal_division(5,2)
main()