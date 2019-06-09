
''' Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21

to reverse


do abs to find abs value

convert integer to string

loop through list of characters backward - append in new string

convert to number


do number * initial_number/abs_number'''


def reverse(initial):

    if initial == 0 or  (initial < -2**31) or initial > (2**31 - 1) :
            return 0
    abs_initial = abs(initial)

    str_initial = list(str(abs_initial))



    str_final = ""

    #print(len(str_initial)-1)
    size = len(str_initial)-1

    for i in range(size, -1, -1):



        str_final += str_initial[i]



    abs_final = int(str_final)

    if abs_final < -2**31 or abs_final > (2**31 - 1):
            return 0

    return int(abs_final * (1.0 * initial / abs_initial))


print(reverse(120))
