import mysql.connector
from tkinter import messagebox
import json


with open('config.json') as config:
    db_items = json.load(config)

host = db_items.get("host")
user = db_items.get("db_user")
password = db_items.get("db_password")
schema = db_items.get("schema")
database = db_items.get("database")

def ConnectDatabase():
    # Load the configuration

    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def CreateDatabase():

    mysqldb = ConnectDatabase()
    
    if mysqldb:
        try:
            with mysqldb.cursor() as mycursor:
                mycursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
                mycursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS {schema}.{database} (
                    Id INT AUTO_INCREMENT PRIMARY KEY,
                    Username VARCHAR(255),
                    Password VARCHAR(255),
                    Category VARCHAR(255),
                    Comments VARCHAR(255))""")
            mysqldb.commit()
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            mysqldb.close()
    else:
        print("Failed to connect to the database.")
        
def Add(username, password, category, comments):
    CreateDatabase()
    mysqldb = ConnectDatabase()
    
    if mysqldb:
        try:
            with mysqldb.cursor() as mycursor:
                mycursor.execute(f"INSERT INTO {schema}.{database} (Username, Password, Category, Comments) VALUES (%s, %s, %s, %s)", (username, password, category, comments))
            mysqldb.commit()
            messagebox.showinfo("Information", "Employee inserted successfully...")
            
        except mysql.connector.Error as err:
            messagebox.showerror("Error", "An error occurred while inserting the record")
            print(f"Error: {err}")
            
        finally:
            mysqldb.close()
    else:
        print("Failed to connect to the database.")
        
def Delete(username, password, category, comments):
    mysqldb = ConnectDatabase()
    with mysqldb.cursor() as mycursor:
        mycursor.execute(f"DELETE FROM {schema}.{database} WHERE Username = %s AND Password = %s AND Category = %s AND Comments = %s", (username, password, category, comments))
    mysqldb.commit()
    mysqldb.close()
    messagebox.showinfo("Information", "Employee deleted successfully...")
    
def Update(id, username, password, category, comments):
    mysqldb = ConnectDatabase()
    
    try:
        with mysqldb.cursor() as mycursor:
            mycursor.execute(f"UPDATE {schema}.{database} SET Username = %s, Password = %s, Category = %s, Comments = %s WHERE Id = %s", (username, password, category, comments, id))
        mysqldb.commit()
        mysqldb.close()
        messagebox.showinfo("Information", "Employee updated successfully...")
    
    except Exception as e:
        print(e)
        mysqldb.rollback()
        messagebox.showerror("Error", "An error occurred while updating the record")
    

def Show():
    CreateDatabase()
    mysqldb = ConnectDatabase()
    if mysqldb:
        try:
            with mysqldb.cursor() as mycursor:
                mycursor.execute(f"SELECT * FROM {schema}.{database}")
                result = mycursor.fetchall()
                return result
        except mysql.connector.Error as err:
            messagebox.showerror("Error", "An error occurred while displaying the record")
            print(f"Error: {err}")
        finally:
            mysqldb.close()
    else:
        messagebox.showerror("Error", "An error occured while connecting to the database")