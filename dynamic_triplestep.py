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


def ways(n, way_table):

    if n in way_table:
        return way_table[n]

    way_table[n] = ways(n-1, way_table) + ways(n-2, way_table) + ways(n-3, way_table)

    return way_table[n]

way_table = {1:1, 2:2, 3:4}

print(ways(5, way_table))
