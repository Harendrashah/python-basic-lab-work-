def list_prime(num):
    prime=[]
    for i in range(2, num + 1):
        count=0
        for j in range (2, i):
            if (i % j==0):
                count += 1
        if count==0:
            prime.append(i)
    return prime
def main():
    num=int(input("enter a number:  "))
    list=list_prime(num)
    print( "the prime number are: ", list)
main()