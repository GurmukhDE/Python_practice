from loguru import logger

#1Q1 - You receive daily row counts from multiple files. you need to sum of the counts

counts = [1200, 3400, 5600]

v = sum(counts)
logger.info(v)

#q2- Filter Invalid Records

#Negative values indicate corrupt records.

data = [10, -3, 25, -1, 40]

#Using a for loop, create a list of only valid records.

invalid_record = []

for i in data:
    if i < 0:
        invalid_record.append(i)
logger.info(invalid_record)

#INTERMEDIATE (Real ETL Logic)

#3️ Dictionary Iteration (Very Common)

#You get record counts per table:

tables = {
    "customers": 10000,
    "orders": 50000,
    "payments": 2000
}

customers = {}

orders = {}

payment = {}

for table in tables:
    logger.info(customers.append(table))
    logger.info(orders.append(table))
    logger.info(payment.append(table))

#-----------------------------------------

#list_comprehension











    
