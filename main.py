from db_setup import backend1
from customer import customer
from admin import backend2
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