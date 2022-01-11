import mysql.connector
mydb = mysql.connector.connect(host = "localhost",user = "root", password ="my5641@sql",database = "mydatabase")
mycursor = mydb.cursor()
sql = "INSERT INTO Members (name,address),VALUES (%s,%s)"
val = ("Nagendra sir","BHOPAL SAM COLLEGE")
mycursor.execute(sql,val)
mydb.commit()
print("1 record inserted, ID:",mycursor.lastrowid)