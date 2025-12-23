import mysql.connector as sql
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