def find_greater_number(x_list, x_num):
    list=[]
    for i in x_list:
        if i > x_num:
            list.append(i)
    return list
def main():
    list=[5,7,9,35,78]
    num=9
    print(find_greater_number(list,num))
main()
