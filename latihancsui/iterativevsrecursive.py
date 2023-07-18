def maximum_iter(lst):

  max_temp = lst[0]

  for i in range(1,len(lst)):
    if lst[i] > max_temp:
      max_temp = lst[i]

  return max_temp

a = maximum_iter([1,3,2,4,5,7])
print(a)

#ATAU

def maximum_rec(lst):
# base case
    if len(lst) == 1:
        return lst[0]

# recursion case
    max_rest = maximum_rec(lst[1:])
    if max_rest > lst[0]:
        return max_rest
    else:
        return lst[0]