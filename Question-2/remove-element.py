def removeElement(nums: list[int], val: int) -> int:
    i = 0
    while i < len(nums):
        print(nums[i]);
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)
    


print(removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val= 2))