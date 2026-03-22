x =input()

type(x)

int(x)

x= int(input())

type(x)

a = input()

b = input()

c = a+b
print(c)

#String datatype

#Indexing in Strings.

s = "Gurmukh"

s[0]

s[5]

s[3]

s[-3]

s[+2]

s[-1]

s[1]

s[-0]

print(s)

type(s)

### Slicing in Python

s = 'gurmukh is learning' 

s[7]

val = 'I am a learner'

val[2:10:2]

val[1:5:2]

val[2:6:2]

val[3:9:3]

val[4:7:2]

val[5:6:4]

val[2:1:3]

val[:3:1]

val[4:12:3]

val[4:12]

val[:12]

#val = 'I am a learner'
val[4::2]

val[:4:3]

val[::4]

### + operator in Strings

x= 'my name is sandeep '

x =  x +'mittal'

print(x)

print(x[0:2])

z= 'ab'+ x[2:]

print(z)

### strings are immutable

s = 'abcd'
s[0]= 'c'
print(s)

### Fuctions for Stings

len(x)

y=  x.lower()

print(y)

y= x.upper()
print(y)

### concatenation in strings

'red'+ '3'

### split in strings

x= 'I am smart'

x = x.split(',')
print(x)

x = x.split(' ')
print(x)

x = x.split('m')
print(x)

x = x.split('smart')
print(x)

x = x.split('I')
print(x)

###  list

l = [1,2,3,4.5,'Tanisha']

l

type(l)

#empty list

l = []
l

#accessing and creating elements from list

name1= ['nisha', 'Priya', 'Ganesh', 'Anuj']

print(name1)

name1[4]

name1[-3]

name1[1:2:1]

name1[1:5:2]

s='abcd'
s[0]='c'
print(s) # Showing error becuase we can not make any changes in String.



### Negative indexing

l = 'i am a learner'

l[10:1]

### class 5

name1 = ['nisha', 'Priya', 'Ganesh', 'Anuj']

name1

l[10:1:-1]

name1[-3:-1:2]

name1[-3:-1:1]

name1[-2:-1:2]

name1[-3:-2:-1]

name1[-4:-2:1]

name1[-2:-1:-2]

name1[2:5:1]



l=['sun', 'mon', 'tue', 'Wed', 'thur', 'fri', 'Sat']

l

l[-3:-5:-2]

l[-3:-5:2]

l.append(1,2,3)
l

l.append([1,2,3])
l

list1 = ['physics', 'chemistry', 1997, 2000]

list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]:", list1[0])

print("list2[1:5]:", list2[1:5])


#Lists are mutable

list1[0] = 'Hindi'

print(list1)

list1[3] = 'english'
print(list1)

# difference between append and extend, and +.

#### append= we can only add 1(one) element at the end.

#### append means = to add something at the end.

list1.append('abc')
list1

list1.append(1,2,3)
list1#we can not append the list with more than one elements.
#in this list we provided 3 numbers.

list1.append([1,2,3])
list1

### Extend function

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = ['a' ,'b']
list1.extend(list2)
list1

list1 = ['physics' , 'chemistry', 1997, 2000]
list2 = ['a', 'b']
list1.extend(list2) # extend the operation would not be permanent It just shows you the demo that how it will look like
list1

list1 = ['physics' , 'chemistry', 1997, 2000]
list3 = ['c', 'd']
list1+list3 #addition


ml1 = ['john', 'id_231393', 'status_active']
ml1.append(['a','b'])
ml1  #append

ml1 = ['john', 'id_231393', 'status_active']
ml1.extend(['a','b'])
ml1 #extend

ml1 = ['john', 'id_231393', 'status_active']
ml2 = ['order_id', 'csd2334']
ml1+ml2


#### Pop function

list.pop() # pop function is used to remove the last element from the lista and return it what element it has removed.


list1 = ['physics', 'chemistry', 1997, 2000]

list1.pop(1)
list1

list1.pop() # if we does not provide the element index then it will remove the last element

#### Repeating the same elements in the list,  we will use (*) symbol to repeat the same elements

x = [1,2,3,4,5]*2
print(x)

#difference between pop and remove functions\.
x

### to remove a particular element

x.remove(2)

x

x.remove(5)
x

y = ['a', 'b', 'g']
y.remove('b')
y

### Class 6 Loops

## In operator 
#it return the value in Boolean form.
x= [1,2,3,4]
1 in [1,2,3,4]

4 in x

3 in x

6 in x

x = 'Gurmukh'

'z' in x

'u' in x

### insert() function



animal = ['camel' , 'elephant', 'cat', 'dog']
animal

animal.insert( 1,'cow')
animal # 1 is the position on which you want to insert the element
#keep in mind always insertion always follows the indexing

type(animal)

### Sorting

animal = ['camel' , 'elephant', 'cat', 'dog']
animal

animal.sort()
animal.sort(reverse = True)
animal #it reversed in decending order alphabetically.

animal = ['zebra' , 'snake', 'penther', 'dog', 'horse', 'panda', 'monkey']
animal

animal.sort()
animal.sort(reverse = True)
animal ## see the below list is in decending order by alphabetically.

animal.sort()
animal ## if we put only sort() then it will give us in ascending order.

Number = [1,2,3,5,6,7,8,9,0,0,]
Number

Number.sort()
Number

Number.sort(reverse = True)
Number

s = 'hello hello how are you'
s

list('hello')

#FAQS


li= [[1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]]
li

li[0][3]

## Bonus


# re function

import re

# initializing string
string = "how are you doing! I am doing very well. how you're doing"
#using re.split()
#spliting characters in string


re.split("|-|",string)
re



