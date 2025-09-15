import re
count = 0  
with open("D:\\download disk c\\what_is_python.txt","r") as f:
   for line in f:
        line = re.sub("[^A-Za-z0-9+]"," ",line)
        words = line.split(" ")
        for word in words:
            if word.lower()=="python":
                count +=1
print(count)
