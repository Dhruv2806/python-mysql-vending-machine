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

#Front-end (Customer)
def customer():
    import mysql.connector as sql
    dbconnect = sql.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'project')
    dbcursor = dbconnect.cursor()
    while True:
        dbcursor.execute("select *from products")
        data = dbcursor.fetchall()
        print(data)
        for i in data:
            print("Product ID:", i[0])
            print("Product:", i[1])
            print('Brand:', i[2])
            print("Price:", i[3])
            print("Quantity left:", i[4])
            print()
        num = int(input("How many types of products do you want:"))
        total = 0
        sub = 0
        cart = []
        check_1 = 0
        for j in range(num):
            try:
                id = int(input("Enter the ID of product type or press some other letter key to exit:"))
                for i in data:
                    i = list(i)
                    if id not in i:
                        continue
                    else:
                        check_1 += 1
                        subcart = []
                        sub += 1
                        index = i.index(id)
                        a = int(input(f"Enter the number of {i[index+2]} {i[index+1]} you want:"))
                        print()
                        i[4] = i[4] - a
                        if i[4] < 0:
                            print(f'We do not have {a} {i[index+1]}')
                            continue
                        else:
                            query1 = f"update products set quantity = quantity - %s where brand = %s"
                            subcart.append(i[index])
                            subcart.append(i[index+2])
                            subcart.append(a)
                            val = (a,i[index+2])
                            dbcursor.execute(query1, val)
                            dbconnect.commit()
                            m = ""
                            for l in i[3]:
                                if l.isdigit():
                                    m += l
                                else:
                                    continue
                            m = int(m)
                            subt = m * a
                            subcart.append(subt)
                            total = total + subt
                    cart.append(subcart)
                if check_1 == 0:
                    print("Product not found")
                else:
                    continue
            except:
                print("Thankyou for visiting")
                break
        if sub == 0:
            print("Thankyou")
        else:
            for bill in cart:
                print(bill[0], "Product:", bill[1], 'x', bill[2], '\t',"₹", bill[3])
            choice = input("Kindly go through your bill, press 1 to remove any item and press any other key to continue with payment:")
            print()
            if choice == '1':
                remove_n = int(input("Enter the number of types of products you want to remove:"))
                for eb in range(remove_n):
                    remove_t = 0
                    check = 0
                    remove_id = int(input("Enter the Product Id (FROM BILL ONLY) of product that you want to remove:"))
                    dbcursor.execute("select *from products")
                    remove_data = dbcursor.fetchall()
                    for x in remove_data:
                        if remove_id in x:
                            check += 1
                            remove_num = int(input(f"Enter the number of {x[2]} {x[1]} to be removed from your bill:"))
                            prod = ""
                            for k in x[3]:
                                if k.isdigit():
                                    prod += k
                                else:
                                    continue
                            prod = int(prod)
                            remove_t = prod * remove_num
                            total = total - remove_t
                            query2 = "update products set quantity = quantity + %s where pid = %s"
                            val1 = (remove_num, remove_id)
                            dbcursor.execute(query2,val1)
                            dbconnect.commit()
                        else:
                            continue
                    if check == 0:
                        print("Product not found")
                        print('Total bill amount:', '\t', "₹", total)
                    else:
                        print('New bill amount:', '\t', "₹", total)
            else:
                print('Total bill amount:', '\t', "₹", total)
            print('Thankyou for shopping')
            print()
        ch = input("Are there more customers:")
        if ch in 'Yy':
            continue
        elif ch in 'Nn':
            break
def backend2():
    import mysql.connector as sql
    dbconnect = sql.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'project')
    dbcursor = dbconnect.cursor()
    dbcursor.execute("select *from products")
    data1 = dbcursor.fetchall()
    print("Welcome ADMIN")
    print()
    print("Press 1 to add more stock")
    print("Press 2 to update cost of any product")
    print("Press 3 to remove any product")
    print("Press 4 to search for any product")
    print("Press 5 to sort the products by desired order")
    print()
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_id = int(input("Enter the PID of the product:"))
        check = 0
        for abc in data1:
            if add_id in abc:
                check += 1
                print("Product:", abc[1], abc[2])
                print("Cost:", abc[3])
                new_num = int(input("Enter amount of new stock:"))
                print()
                query1 = "update products set quantity = quantity + %s where pid = %s"
                val1 = (new_num, add_id)
                dbcursor.execute(query1,val1)
                dbconnect.commit()
                print("New Quantity:", abc[4]+new_num)
                print("Stock added")
                print()
            else:
                continue
        if check == 0:
            print("Product not found")
            print()
    elif choice == 2:
        new_id = int(input("Enter PID of the product:"))
        check1 = 0
        for klm in data1:
            if new_id in klm:
                check1 += 1
                print("Product:", klm[1], klm[2])
                print("Cost:", klm[3])
                print()
                new_cost = input("Enter the new cost of the product:")
                print()
                pcost = "Rs." + new_cost
                val2 = (pcost, new_id)
                query2 = "update products set cost = %s where pid = %s"
                dbcursor.execute(query2, val2)
                dbconnect.commit()
                print('Cost updated successfully')
            else:
                continue
        if check1 == 0:
            print("Product not found")
    elif choice == 3:
        del_id = int(input("Enter PID of the product you want to remove:"))
        check2 = 0
        for pqr in data1:
            if del_id in pqr:
                check2 += 1
                dbcursor.execute(f"delete from products where PID = {del_id}")
                dbconnect.commit()
                print("Product deleted successfully")
            else:
                continue
        if check2 == 0:
            print("Product not found")
    elif choice == 4:
        search_id = int(input("Enter PID of the product you want to search for:"))
        check3 = 0
        for abc in data1:
            if search_id in abc:
                check3 += 1
                print("Product ID:", abc[0])
                print("Product:", abc[1])
                print('Brand:', abc[2])
                print("Price:", abc[3])
                print("Quantity left:", abc[4])
                print()
        if check3 == 0:
            print("Invalid PID")
    elif choice == 5:
        sort_field = input("Enter the field by which you want to sort the products (P- PID, B- Brand, C- Cost, Q- quantity:").lower()
        if sort_field == 'p':
            dbcursor.execute("select *from products order by PID")
            data2 = dbcursor.fetchall()
            for p in data2:
                print("Product ID:", p[0])
                print("Product:", p[1])
                print('Brand:', p[2])
                print("Price:", p[3])
                print("Quantity left:", p[4])
                print()
        elif sort_field == 'b':
            dbcursor.execute("select *from products order by brand")
            data3 = dbcursor.fetchall()
            for q in data3:
                print("Product ID:", q[0])
                print("Product:", q[1])
                print('Brand:', q[2])
                print("Price:", q[3])
                print("Quantity left:", q[4])
                print()
        elif sort_field == 'c':
            order = input("Enter the order in which you want to sort (A- Asc; D- Dsc):").lower()
            if order == 'a':
                dbcursor.execute("select *from products order by cost")
                data4 = dbcursor.fetchall()
                for r in data4:
                    print("Product ID:", r[0])
                    print("Product:", r[1])
                    print('Brand:', r[2])
                    print("Price:", r[3])
                    print("Quantity left:", r[4])
                    print()
            elif order == 'd':
                dbcursor.execute("select *from products order by cost desc")
                data5 = dbcursor.fetchall()
                for s in data5:
                    print("Product ID:", s[0])
                    print("Product:", s[1])
                    print('Brand:', s[2])
                    print("Price:", s[3])
                    print("Quantity left:", s[4])
                    print()
        elif sort_field == 'q':
            order = input("Enter the order in which you want to sort (A- Asc; D- Dsc):").lower()
            if order == 'a':
                dbcursor.execute("select *from products order by quantity")
                data6 = dbcursor.fetchall()
                for t in data6:
                    print("Product ID:", t[0])
                    print("Product:", t[1])
                    print('Brand:', t[2])
                    print("Price:", t[3])
                    print("Quantity left:", t[4])
                    print()
            elif order == 'd':
                dbcursor.execute("select *from products order by quantity desc")
                data7 = dbcursor.fetchall()
                for u in data7:
                    print("Product ID:", u[0])
                    print("Product:", u[1])
                    print('Brand:', u[2])
                    print("Price:", u[3])
                    print("Quantity left:", u[4])
                    print()
# backend1()
backend1()
while True:
    ch = input("Who is this- ADMIN (A) or CUSTOMER (C): ").lower()
    if ch == 'a':
        passwd = input('Enter your password:')
        if passwd == "28113":
            backend2()
            continue
        else:
            print("Invalid Password")
            continue
    elif ch == 'c':
        customer()
        continue
    else:
        break