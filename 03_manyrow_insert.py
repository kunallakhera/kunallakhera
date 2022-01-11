import mysql.connector
mydb = mysql.connector.connect(host = "localhost",user = "root", password ="my5641@sql",database = "mydatabase")
mycursor = mydb.cursor()
""" mycursor.execute("CREATE TABLE Members (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO Members (name,address),VALUES (%s,%s)"
val = [("kunal","SAI DHAM COLONY BINA"),("sarandeep vishwakarma","BHAGSEWANIYA BHAOPAL NEAR ASHIMA MALL"),('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')]
  mycursor.executemany(sql,val)
  mydb.commit()"""
  #print(mycursor.rowcount,"was inserted")
  print(mycursor.lastrowid)

