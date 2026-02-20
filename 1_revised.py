
1
list1 = [1,2,3,4]
2
list2 = list1
3
​
list1
1
list1
[1, 2, 3, 4]
list2
1
list2
[1, 2, 3, 4]
list1, list2
1
list1, list2
([1, 2, 3, 4], [1, 2, 3, 4])
1
list1[1] = 1000
1
list2
[1, 1000, 3, 4]
1
list1
1
a = [1,2,3,4]
2
​
1
a
[1, 2, 3, 4]
#
1
#a.append([4,5])
1
a
[1, 2, 3, 4]
1
a.extend([4,5])
1
a
[1, 2, 3, 4, 4, 5]
lis = [1,2,34,45,5]

sqr_list = list(map(lambda x: x*2, lis))

print(sqr_list)
1
lis = [1,2,34,45,5]
2
​
3
sqr_list = list(map(lambda x: x*2, lis))
4
​
5
print(sqr_list)
[2, 4, 68, 90, 10]
1
lis = [1,2,34,45,5]
2
​
3
sqr_list = list(filter(lambda x: x*2, lis))
4
​
5
print(sqr_list)
[1, 2, 34, 45, 5]
1
from functools import reduce
/
1
num = [1,2,3,5,5,6]
2
result = reduce(lambda x,y: x/y,num)
3
print(result)
0.0011111111111111111
1
a = [1,2,3,4,5,5,6,7,8,9,9,0,0,6,5,44]
2
​
3
even = []
4
odd= []
5
for i in a:
6
    if i%2==0:
7
        even.append(i)
8
    else:
9
        odd.append(i)
10
        
11
print(even, odd)
[2, 4, 6, 8, 0, 0, 6, 44] [1, 3, 5, 5, 7, 9, 9, 5]
def even_odd(a):
    even = []
    odd = []
    for i in a:
        if i %2==0:
            even.append(i)
        else:
            odd.append(i)
            
    return even, odd

a = [1,3,4,5,7,8,9,9,5,8,9,0,2030030,24]
my_even = even_odd(a)
print(my_even)
            
1
def even_odd(a):
2
    even = []
3
    odd = []
4
    for i in a:
5
        if i %2==0:
6
            even.append(i)
7
        else:
8
            odd.append(i)
9
            
10
    return even, odd
11
​
12
a = [1,3,4,5,7,8,9,9,5,8,9,0,2030030,24]
13
my_even = even_odd(a)
14
print(my_even)
15
            
([4, 8, 8, 0, 2030030, 24], [1, 3, 5, 7, 9, 9, 5, 9])
1
even = [i for i in range(0,11) if i%2==0]
2
odd = [i for i in range(0,11) if i%2!=0]
3
print(even)
4
print(odd)
[0, 2, 4, 6, 8, 10]
[1, 3, 5, 7, 9]
1
even = list(filter(lambda i:i%2==0, range(0,11)))
2
print(even)
3
odd = list(filter(lambda i:i%2!=0, range(0,11)))
4
print(odd)
[0, 2, 4, 6, 8, 10]
[1, 3, 5, 7, 9]
1
​
