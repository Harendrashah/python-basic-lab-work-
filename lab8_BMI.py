class BMI:
    def __init__(self, weight,height):
        self.wei=weight
        self.hei=height
    def cal_bmi(self):
       return self.wei/self.hei**2
    def display_bmi(self):
        return "the BMI calculation is {:.2f}.".format(self.cal_bmi())

if __name__=='__main__':
        name=input("enter your name: ")
        wei=float(input("enter your weight: "))
        hei=float(input("enter your height: "))
        a= BMI(wei,hei)
        #print('The BMI calculation=',a.cal_bmi())
        print(a.display_bmi())
