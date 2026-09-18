import mysql.connector as sql

mydb = sql.connect(
    host='localhost',
    user='root',
    password='9048',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("CREATE TABLE temp_codes (id INT AUTO_INCREMENT PRIMARY KEY,code VARCHAR(10) NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
mycursor.execute("INSERT INTO temp_codes (code)VALUES (LPAD(FLOOR(RAND() * 1000000), 6, '0'));")
mycursor.execute("COMMIT")
