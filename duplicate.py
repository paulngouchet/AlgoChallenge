'''Remove duplicate


Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

method

loop through the array

i need to keep track of the ocurrence.

First solution  -  have dictionary to keep track of the occurence by looping

loop through the array and populate the dictionary

the number is the key and the value will the number of occurence

at the end just delete the occurences see'''


def duplicate(nums):

    dict_duplicate = {}

    for num in nums:

        if num in dict_duplicate:
            dict_duplicate[num] += 1   # the dictionary was populated
        else:
            dict_duplicate[num] = 1

    # Now i am going to remove all the duplicate keys


    for key, value in dict_duplicate.items():

        if value > 1:
            for i in range(value-1):
                nums.remove(key)

    return len(nums)


print(duplicate([1,1,3,4,5,5])) # should print 4
