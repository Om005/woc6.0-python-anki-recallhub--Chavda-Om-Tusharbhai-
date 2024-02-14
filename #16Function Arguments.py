def avg(a=8, b=10):
    print("Average is", (a+b)/2)

def average(*nums):
    # nums is a tuple
    sum = 0
    for i in nums:
        sum += i
    return sum/len(nums)


avg(2, 3)
avg(b=3, a=2)
avg(4)
avg(b=8)

ok = average(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(ok)