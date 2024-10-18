from getpass import getpass
# from mysql.connector import errorcode
import mysql.connector as db_connector


DB_NAME = 'alx_book_store'
create_database_query = 'CREATE DATABASE IF NOT EXISTS alx_book_store;'

try:
    with db_connector.connect(
        host= 'localhost', 
        user= 'root',
        password=getpass('Enter password: ')
        ) as connection:
        
               
        print(f'Connection successful : {connection._conn_attrs['_client_name']} conncected')
        with connection.cursor() as cursor:
                cursor.execute(create_database_query)
                print(f"Database '{DB_NAME}' created successfully!")           
        
except db_connector.Error as err:
    print(f'connection error: {err.msg}')
    

                

    




        

        