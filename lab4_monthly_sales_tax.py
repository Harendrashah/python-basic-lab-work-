def local(l1):
    total=l1/20
    return total
def state(s1):
    total=s1/40
    return total
def total(l1,s1):
    total=l1+s1
    return total
def main():
    sales= int(input("enter the sale of 2 months "))
    local_tax= local(sales)
    state_tax=state(sales)
    final=total( local_tax,state_tax)
    print("the total local tax= ", local_tax)
    print("the total state tax= ",state_tax)
    print("the total final tax= ",state_tax)
main()



