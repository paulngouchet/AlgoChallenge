'''Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
size 3 means 100
number * 10
2 4 3
5 6 4
to go steps by steps
1st function - takes as input the linked list and returns an array with the number
extracted from the list
2nd function takes as input the array and return the integer
3rd function takes as input 2 integers, calculate the sum 807, produces array which will loop through in reverse order
4th function takes as input an array and returns a linked list
main function combines everything '''


def extract(l1):
    head = l1
    extracted = []
    
    while head.next != None:
        extracted.append(head.val)
        head = head.next
    extracted.append(head.val)
    return extracted

def combine(array_list):
    size = len(array_list)
    sum = 0
    # 4
    for i in range(size - 1, -1):
        step = (i * 10) * array_list[i]
        sum += step

    return sum


def sum(integer1, integer2):
    final_sum = integer1 + integer2
    return [int(i) for i in str(final_sum)]

def sum2list():
