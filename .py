import configparser
from loguru import logger
from day_13_AES_encyption_decyption import decrypt
from src.main.databases.code_cleaning_part_2 import MySqlConnection, MySqlCrudOperation

class Labour:
    def __init__(self, first_name, last_name, wages, role):
        self.first_name = first_name
        self.last_name = last_name
        self.wages = wages
        self.role =role


    def save_to_database(self, crud):
        query = "SELECT id FROM labours WHERE lower(fist_name) = %s AND lower(last_name) = %s"
        result = self.crud.read_from_mysql(query, (self.first_name, self.last_name))

        if result:
            logger.info(f"Labour already exists with ID : {result[0][0]}")
            return result[0][0]
        
        insert_query  = """
            INSERT INTO labours (first_name, last_name, wages, role, email)
            VALUES (%s, %s, %s, %s,%s)"""
        email = self.first_name + "." + self.last_name + "@gmail.com"  
        
    def login(self):
        pass


config = configparser.ConfigParser()
config.read(r"C:\Users\manish\Documents\python_programming\src\resources\config_file.ini")
config.set("mysql_database","password", 
           decrypt(config["mysql_database"]["password"])
)

mysql_db_conn_obj = MySqlConnection(config)
mysql_db_conn_obj.connect()

crud = MySqlCrudOperation(mysql_db_conn_obj.connection) # type: ignore

manish_obj = Labour("manish", "kumar", 500)
manish_obj.save_to_database(crud)

print(manish_obj._Labour__wage)

# print(manish_obj._last)

ramesh_obj = Labour("Rajesh", "Singh", 400)

# print(Labour.total_count)
# first_name, last_name, wage



