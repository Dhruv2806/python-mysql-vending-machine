import mysql.connector as sql
#Back-end
def backend1():
    import mysql.connector as sql
    dbconnect = sql.connect(host = 'localhost', user = 'root', passwd = 'root')
    dbcursor = dbconnect.cursor()
    try:
        dbcursor.execute("create database project")
        dbconnect.commit()
    except:
        dbcursor.execute("use project")
    try:
        dbcursor.execute("create table products(PID int primary key, Product varchar(100) not null, Brand varchar(25) not null, Cost varchar(40) not null, Quantity int)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(101, 'Soda bottles (500ml)', 'Sprite', 'Rs. 20 ', 10)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(102, 'Soda bottles (250ml)', 'Fanta', 'Rs. 15', 15)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(110, 'Milk packets (1L)', 'Amul', 'Rs. 52', 25)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(115, 'Eggs', 'Dairy', 'Rs. 02 (each)', 30)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(111, 'Milk packets (1L)', 'Delight', 'Rs. 51', 20)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(106, 'Brown Bread packs', 'Modern', 'Rs. 30', 8)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(107, 'White Bread packs', 'Everfresh', 'Rs. 25', 11)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(151, 'Candies', 'Cadbury', 'Rs. 05', 26)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(134, 'Mineral Water Bottles (1L)', 'Bisleri', 'Rs. 30 ', 20)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(129, 'Biscuit packets (1 pack)', 'Hide n Seek', 'Rs. 17 ', 22)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(145, 'Noodle packets', 'Yippee', 'Rs. 25', 30)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(137, 'Chewing Gums', 'Boomer', 'Rs. 01', 40)")
        dbconnect.commit()
    except:
        pass
    try:
        dbcursor.execute("insert into products values(192, 'Chewing Gums', 'Centerfresh', 'Rs. 01', 25)")
        dbconnect.commit()
    except:
        pass

