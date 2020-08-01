# Bubble sort implementation

def bubble_sort(nums):
    num_swap = 0
    for a in range(len(nums) - 1):
        num_swap = 0
        for i in range(0, len(nums) - 1 - a): # You can do some optimization , not check the last element at the second turn etc
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                num_swap += 1

        if num_swap == 0: # Checking if no swap was done
            break
    return nums

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
