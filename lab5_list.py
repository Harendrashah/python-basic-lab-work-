def create_list():
    list=['playStation','Xbox','Steam','iOS','Google Play']
    return list
def get_info(list):
    h=(list[0])
    a=(list[-2])
    r=(len(list))
    info=(h,a,r)
    return info
def get_practical(list):
    new_list=[]
    new_list=list[1:4]
    return(new_list)
def get_last_three(list):
    new_list=[]
    new_list.append(list[-1])
    new_list.append(list[-2])
    new_list.append(list[-3])
    return(new_list)
def double_list(list):
    new_list=(list)*2
    return(new_list)
def Amend(list):
    new_list=list
    new_list[1]="None"
    new_list.append("Bye")
    return(new_list)
def main():
    test_list=create_list()
    print(test_list)
    print(get_info(test_list))
    print(get_practical(test_list))
    print(get_last_three(test_list))
    print(double_list(test_list))
    print(Amend(test_list))
main()
