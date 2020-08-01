'''super_digit(P) = super_digit(148148148)
               = super_digit(1+4+8+1+4+8+1+4+8)
               = super_digit(39)
               = super_digit(3+9)
               = super_digit(12)
               = super_digit(1+2)
               = super_digit(3)
               = 3.
sample case:
1st step is build the super digit
generate_number()
string_number
for i in range(k - 1):
  string_number += string_number
  return list(string_number)

14 = 1+4 = 5
148 = 1 + 4 + 8 = 13 = 1 + 3 = 3
1 = 1
base case if len(string_number) == 1:
return int(string_number[0])

else i need to return the sum
 sum(string_number)
 recursion(string_number)

        1 4 8
          /
        13
        /
        4


function to sum ():
list(148) = [1, 4, 8]
sum = 0
number in list:
sum += int(number)
return sum
''''


def generate(n,k):
    str_number = list(n)
    initial = copy.deepcopy(str_number)
    for i in range(k - 1):
        str_number.extend(initial)
    #print(str_number)
    return str_number

def summation(str_number):
    sum = 0
    for num in str_number:
        sum += int(num)

    return list(str(sum))

def recursion(str_number):
    if len(str_number) == 1:
        return int(str_number[0])
    else:
        new_number = summation(str_number)
        return recursion(new_number)

def superDigit(n, k):
    str_number = generate(n,k)

    if len(str_number) == 1:
        return int(str_number[0])

    return recursion(str_number)
