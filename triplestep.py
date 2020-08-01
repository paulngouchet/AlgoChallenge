'''triple step
How many possible ways to run up the n stairs
1 2 3
Example
n = 7
1 + 2 + 3 + 1
let's say 3
1 + 1 + 1 or 1 + 2
for solving 4
example 1 + (n - 1)
1 + 2 = 1 + 1 + (n - 1 -1 )
combination for 1 - base case n = 1 - recursion the base case is'''

recursive(list, n)

if n == 1:
  list.append(1) # if n = 1 then answer 1 # base case

# i need to keep track of multiple versions of the list
if n == 2: #if n = 2 then answer 2 or 1 + 1 - append ->
  list.append(2) or list.append(1) , list.append(1)
if n == 3
  list.append(3) or list.append(1) list.append(1), list.append(1)   or list.append(2) list.append(1)     # function for all the possible combination of 3 - 2 - 1

# what is the main case

recursive(list, n)
ways(3)
ways(2) + ways(1)
ways(1) = 1  A - AB - AC CB
ways(2) = 1,1 - 2 - B C
ways(3) = 1, 1, 1 or 1, 2 or 2, 1
