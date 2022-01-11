import mysql.connector
mydb = mysql.connector.connect(host = "localhost",user = "root", password ="my5641@sql",database = "mydatabase")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Members (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO Members (name,address),VALUES (%s,%s)"
val = ("kunal","SAI DHAM COLONY BINA")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")
