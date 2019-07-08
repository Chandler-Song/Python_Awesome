li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)

print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li)

li.sort()

print('Original Variable:\t', li)

t_li = li.sort()
print('Sorted Variable:\t', t_li)

s_li = sorted(li, reverse=True)

li.sort(reverse=True)

tup = (9,1,8,2,7,3,6,4,5)
tup.sort()
s_tup = sorted(tup)
print('Tuple\t', s_tup)