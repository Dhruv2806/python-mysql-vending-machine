import mysql.connector as sql
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