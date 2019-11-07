import pyodbc

# Variables to connect to DB

server = 'local,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

docker_northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

# what is a cursor?

cursor = docker_northwind.cursor()
cursor.excute("SELECT @@version;")
row = cursor.fetchone()
print(row)



# all_customers = cursor.excute("SELECT * FROM Customers;").fetchall()
# Fetch