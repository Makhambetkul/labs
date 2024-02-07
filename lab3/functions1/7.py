def has_33(nums):
    t=False
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            t= True
            break
        else:
            continue
    print(t)
    
has_33([1, 3, 3])
has_33([1, 3, 2, 3])
has_33([3, 1, 3])