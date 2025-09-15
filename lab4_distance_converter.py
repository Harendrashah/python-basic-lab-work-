def distance(dis):
    dis_miles=dis * 0.6214
    R_dis_miles=format(dis_miles,".2f")
    print("the distance in miles is {0} ".format(R_dis_miles))
def main():
    dis=int(input("the kilometers is:  "))
    distance(dis)
main()