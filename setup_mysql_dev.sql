#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root', 
            password='your_root_password'  
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL server: {e}")
        return None

def create_database(cursor, database_name):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database {database_name} created successfully.")
    except Error as e:
        print(f"Error creating database {database_name}: {e}")

def create_user(cursor, username, password):
    try:
        cursor.execute(f"CREATE USER IF NOT EXISTS '{username}'@'localhost' IDENTIFIED BY '{password}'")
        print(f"User {username} created successfully.")
    except Error as e:
        print(f"Error creating user {username}: {e}")

def grant_privileges(cursor, username, database_name):
    try:
        cursor.execute(f"GRANT ALL PRIVILEGES ON {database_name}.* TO '{username}'@'localhost'")
        cursor.execute(f"GRANT SELECT ON performance_schema.* TO '{username}'@'localhost'")
        print(f"Privileges granted to user {username} on database {database_name}.")
    except Error as e:
        print(f"Error granting privileges to user {username}: {e}")

def main():
    database_name = 'hbnb_dev_db'
    username = 'hbnb_dev'
    password = 'hbnb_dev_pwd'

    connection = create_mysql_connection()
    if connection:
        cursor = connection.cursor()
        create_database(cursor, database_name)
        create_user(cursor, username, password)
        grant_privileges(cursor, username, database_name)

        # Commit the changes and close the connection
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL server preparation completed.")
    else:
        print("Failed to connect to MySQL server.")

if __name__ == "__main__":
    main()

