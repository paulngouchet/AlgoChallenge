# Example of dynamic programming



def fibonacci(n, fib_table):

    if n == 1 or n == 2:
        return 1

    if n in fib_table:
        return fib_table[n]

    else:
        fib_table[n] = fibonacci(n-1, fib_table) + fibonacci(n-2, fib_table)

    return fib_table[n]


fib_table ={1:1, 2:1}

print(fibonacci(4, fib_table))
