import mysql.connector
from mysql.connector import Error
from sqlalchemy.engine import create_engine
 
def create_server_connection(host_name, user_name, user_psswd, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_psswd,
            database = db_name
        )
        print("Connection Established")
    except Error as err:
        print(f"something went wrong")

    return connection

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"something went wrong")

connection = create_server_connection("localhost", "root", "slqalchemy@mysql", "organization")

# SQLAlchemy1 : where 
sql1 = db.select([employees]).where(employees.columns.salary < 25000) 
print(execute_query(connection, sql1))

# SQLAlchemy : in
sql2 = db.select([employees]).where(employees.columns.salary.in_([20000, 30000]))
print(execute_query(connection, sql2))

# SQLAlchemy : order by
sql3 = db.select(employees]).order_by(db.desc(employees.columns.id), employees.columns.name)
print(execute_query(connection, sql3))
