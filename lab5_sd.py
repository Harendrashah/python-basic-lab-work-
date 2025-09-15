def cal_sum(nums):
    sum=0
    for num in nums:
        sum+=num
    return sum
def cal_sd(nums):
    mean = cal_sum(nums) /len(nums)
    square=[]
    for num in nums:
        square.append((num-mean)**2)
    sq_total = cal_sum(square)
    variance=sq_total/len(nums)
    sd= variance**0.5
    return sd

input_count = int(input("How many inputs do you wants:  "))
nums = []
for i in range(1, input_count+1):
    sample = int(input("Enter the number of population:  "))
    nums.append(sample)
print(nums)
shah=cal_sd(nums)
print(shah)
