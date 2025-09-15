H= int(input("Enter the any 1stnumber:  "))
A=int(input("Enter the 2nd any number:  "))
print("The prime number betwwen ",H,"or",A,"are:")
for i in range (H,A+1):
    if i>1:
        for j in range (2,i):
            if (i % j) == 0:
                break
        else:
            print(i)