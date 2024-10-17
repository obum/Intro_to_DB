from getpass import getpass
# from mysql.connector import errorcode
import mysql.connector as db_connector


DB_NAME = 'alx_students'
create_database_query = 'CREATE DATABASE alx_students;'

try:
    with db_connector.connect(
        host= 'localhost', 
        user= 'root', 
        password=getpass('Enter password: ')) as connection:
        
        print(f'Connection successful : {connection._conn_attrs['_client_name']} conncected')
        with connection.cursor() as cursor:
            try:
                cursor.execute(create_database_query)
            except db_connector.Error as err:
                if err.errno == 1007:
                    print(f"Database '{DB_NAME}' already exists: {err.errno} error")
                else:   
                    print(f'connection error: {err}')
            else:
                print(f"Database '{DB_NAME}' created successfully!")
        
except db_connector.Error as err:
    print(f'connection error: {err}')
    




        

        