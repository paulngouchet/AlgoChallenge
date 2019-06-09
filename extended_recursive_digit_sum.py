import math
import os
import random
import re
import sys
import copy

# Complete the superDigit function below.

def generate(n,k):
    str_number = list(n)
    initial = copy.deepcopy(str_number)
    for i in range(k - 1):
        str_number.extend(initial)

    #print(str_number)
    return str_number

def generate2(n,k):

    str_number = n
    for i in range(k - 1):
        str_number += n

    return str_number, len(str_number)



def summation(str_number):
    sum = 0
    for num in str_number:
        sum += int(num)

    return list(str(sum))

def summation2(str_number, size):
    number = int(str_number)
    print(number)
    print(size)
    sum = 0
    for i in range(size-1, -1, -1):
        digit = number / (10**i)
        sum += digit
        number -= digit*(10**i)

    return str(sum), len(str(sum))



def recursion2(str_number, size):

    if size == 1:
        return int(str_number)
    else:
        new_number, new_size = summation2(str_number, size)
        return recursion2(new_number, new_size)

def recursion(str_number):

    if len(str_number) == 1:
        return int(str_number[0])
    else:
        new_number = summation(str_number)
        return recursion(new_number)

def superDigit2(n, k):

    str_number, size = generate2(n,k)

    if size == 1:
        return int(str_number)

    return recursion2(str_number, size)

def superDigit(n, k):

    str_number = generate(n,k)

    if len(str_number) == 1:
        return int(str_number)

    return recursion(str_number)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
