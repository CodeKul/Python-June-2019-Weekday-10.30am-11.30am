import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="root",
    passwd="root@123",
    database="StudentDB"
)
mycursor = mydb.cursor()


# # create table
# mycursor.execute("CREATE TABLE Student (name VARCHAR(255), marks VARCHAR(255))")
# print("Table is created...")


# # Insert into table
# sql = "INSERT INTO Student (name, marks) VALUES (%s, %s)"
# val = ("PQR", "90")
# mycursor.execute(sql, val)
# mydb.commit()
# print("data inserted...")


# # Select from table
# mycursor.execute("SELECT * FROM Student")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# Where clause
sql = "SELECT * FROM Student WHERE marks ='90'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)