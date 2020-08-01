# Insertion sort

def insertion(nums):
    for i in range(1, len(nums)):
        unsorted_element = nums[i]
        j = i
        while (j > 0 and nums[j-1] > unsorted_element):
            # If the loop exit then that means that nums[j-1] < unsorted_element so we can stop
            nums[j] = nums[j-1]
            j = j - 1

        nums[j] = unsorted_element
    return nums

print(insertion([64, 25, 12, 22, 11]))
