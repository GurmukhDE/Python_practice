# Python_practice
Daily Python practice with a focus on data engineering concepts and interview preparation.
from loguru import logger

l = [2,4,5,6,8,9]

l2  = ['a', 'b']

list_inside_list_append = (logger.info(l.append(l2)))
logger.info(f'list_inside_list_appended {l}')

logger.info(l.append(3))
logger.info(l)

l2 = [1,3,7]
logger.info(l.extend(l2))
logger.info(l)
 
logger.info(l.insert(4,2))
logger.info(l)

md_list = [['gurmukh', "data_engineer"],['company', 'EPAM']] #multidimensional List

print(md_list[0][0])


lis = [1,2,3,4,5,6,7,8,'kaalia', 'Shehensha', 'coolie', 'mard', 'Namak Haram', 'Sholey', 'Sharaabi'] 

#lis(start:end:step) default step size is 1
logger.info(lis[1::8]) #this is slicing method

result = [lis[1] , lis[8]] # this is indexing method
logger.info(result)

#if I want to filter only String values
logger.info(lis[8:15])

#reverse a list

lis = [1,2,3,4,5,'kaalia', 'Shehensha', 'coolie', 'mard'] 

logger.info(lis[::-1]) #reverse a list

result = [x for x in lis if isinstance(x, str)] # just to fetch only string from a list
logger.info(result)

result = [x for x in lis if isinstance(x, int)] # just to fetch only int from a list
logger.info(result)

#--------------------------------------------------------
#methods

logger.info(len(lis))

logger.info(lis.insert(3,'Majboor'))
logger.info(lis)

# I want all int should come first and string come later

int_ = [x for x in lis if isinstance (x, int)]

string_ = [x for x in lis if isinstance(x, str)]

final_lis = int_ + string_
logger.info(final_lis)  # Yeah ho gya....!!!!!hurrahhha

#.pop() method

l = [1,2,4,5,'y6',7, 'p95' ,9]
# as we can see in the above list l there a two values are anomaly in the list i.e  = 'y6' and 'p95' so:
# so let's delete them from the data using .pop() method

r1 = l.pop(4)
logger.info(l)

r2 = l.pop(5)
logger.info(l)

# sometimes we need to fix some values in a list then how to do that we use change the value method.

g = ['gurumukh singhh', 'Pallavi singh', 'India']

g[0] = 'gurmukh singh'

logger.info(g)
#----------------------------------------------------------

#.split() method

api_url = 'https://chatgpt.com/c/694b0d1d-1e30-8320-9ad4-8d53731af91b'

formatted_url = api_url.split("/")

logger.info(formatted_url)
# from the above API URL we have converted it to a list 
# ['https:', '', 'chatgpt.com', 'c', '694b0d1d-1e30-8320-9ad4-8d53731af91b']
#now we can fetch or do transformation or many operation on it.

#for example let's find that the given URL is for which API let's find it

logger.info(formatted_url[2])# here we get this url for Chatgpt.com

logger.info(formatted_url)
