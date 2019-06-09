'''ways(1) -> 1

ways(2) -> 1 1,  2

ways(3) - 1 1 1 , 1 2 , 2 1, 3

ways(4) - 1 1 1 1 , 1 2 1 ,  1 1 2 , 2 1 1, 2 2,  1 3,  3 1



I would say that the formula will look in the following way:

K(1) = 1
K(2) = 2
k(3) = 4
K(n) = K(n-3) + K(n-2) + K(n - 1)

'''


def ways(n):

    if n == 1 :
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    number_ways = ways(n-1) + ways(n-2) + ways(n-3)

    return number_ways


print(ways(5))
