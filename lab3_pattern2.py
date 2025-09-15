rws = 6
col = 21
for i in range(rws):
    for j in range(col):
        if(i == 0 or i == rws - 1 or j == 0 or j ==col-1):
            print("*",end ="")
        else:
            print(" ",end="")
    print()

