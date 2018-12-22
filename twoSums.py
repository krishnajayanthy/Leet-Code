def twoSum(nums,target):
    a ={}
    for i, num in enumerate(nums):
        if target-num in a:
            return [a[target - num], i]
        else:
            a[num] = i

print(twoSum([0,4,3,0],0))