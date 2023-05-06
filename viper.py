import mysql.connector
import random

conn = mysql.connector.connect(host="localhost", user="root", database="vv", password="root")
cursor = conn.cursor()
print("                                  WELCOME TO VACCINE SLOT BOOKING                                 ")
while True:

    print("1) REGISTER A NEW USER")
    print("2) REGISTERED USER")
    print("3) quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = input("Enter your Name= ")
        l = input("Enter your Aadhaar Number= ")
        c = input("Enter your Mobile Number= ")

        cursor.execute("INSERT INTO registrationss(NAME,AADHAAR_NO,Mobile_no)VALUES(%s,%s,%s)", (a, l, c))
        print("your registration is done successfully")
        conn.commit()
    elif choice == 2:
        f = input("enter your aadhaar number= ")
        cursor.execute("select * from registrationss where aadhaar_no= {}".format(f))
        print("                              THESE ARE YOUR DETAILS                        ")
        print("+--------+--------------+-----------+")
        print("| Name   | Aadhaar_no   | Mobile_no |")
        print("+--------+--------------+-----------+")
        for i in cursor:
            print("|", i[0], "|", i[1], "|", i[2], "|")
            print("+--------+--------------+-----------+")

        conn.commit()
        cursor.execute("select * from registrationss where aadhaar_no= {}".format(f))
        print("+--------+--------------+---------+")

        print("| slot1 | slot2 | slot3  | slot4 |")
        print("| 10 Am | 11Am  | 12Noon | 1 Pm  |")
        print("+--------+--------------+---------+")
        result = cursor.fetchall()

        p = input("PLEASE SELECT YOUR SLOT BY TIME= ")
        for i in result:
            a = random.randint(0000, 9999)
            print("NAME= ", i[0])
            print("Aadhaar Number= ", i[1])
            print("Slot= ", p)
            print("Mobile Number= ", i[2])
            print("Secret Code= ", a)

        conn.commit()




        print("Slot booking has been done successfully")
    elif choice == 3:
        break

