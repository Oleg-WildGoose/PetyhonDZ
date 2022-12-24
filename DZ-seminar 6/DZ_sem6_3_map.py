def times_10(num):
    return num * 10 
nums = [1, 2, 3, 4, 5]
nums = list(map(times_10, nums))
print(nums)
