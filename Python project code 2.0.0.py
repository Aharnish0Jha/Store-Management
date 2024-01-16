import mysql.connector as c
con=c.connect(host="localhost",user="root",password="dps123")
mycur=con.cursor()
mycur.execute("create database if not exists term1_project")
mycur.execute("use term1_project")
mycur.execute("create table if not exists employee(emp_name varchar(25)not null,password varchar(25)not null)")
mycur.execute("create table if not exists cart(item_name varchar(35) not null,item_qty int not null,Total_price int not null)")
mycur.execute("create table if not exists customer(cust_name varchar(30) not null,cust_password int not null,cust_phoneNo char(10)not null)")
mycur.execute("create table if not exists supplier(supplier_name varchar(35) not null,item_supplying varchar(25) not null )")
mycur.execute("create table if not exists store(biscuits varchar(20) notnull ,chips varchar(20) not null, cold_drinks varchar(20) not null,chocolate varchar(20) not null, frozen_foods varchar(20) not null)")
con.commit()

z=0
mycur.execute("select * from employee")
for i in mycur:
    z+=1
if z==0:
    mycur.execute("insert into employee values('Akaash',101)")
    mycur.execute("insert into employee values('Akshay',102)")
    mycur.execute("insert into employee values('Saksham',103)")
    mycur.execute("insert into employee values('Rajveer',104)")
    con.commit()

a=0
mycur.execute("select * from customer")
for j in mycur:
    a+=1
if a==0:
    mycur.execute("insert into customer values('Sanjay',109,'8130112030')")
    mycur.execute("insert into customer values('Rohan',881,'8900128330')")
    mycur.execute("insert into customer values('Rahul',567,'9030314330')")
    mycur.execute("insert into customer values('Vishnu',678,'9930618830')")
    con.commit()

b=0
mycur.execute("select * from supplier")
for k in mycur:
    b+=1
if b==0:
    mycur.execute("insert into supplier values('AGA pvt lmt','bicuits')")
    mycur.execute("insert into supplier values('Chips Ahoy lmt','chips')") 
    mycur.execute("insert into supplier values('Shyam','cold drinks')")
    mycur.execute("insert into supplier values('Nestle Lmt.','chocolate')") 
    mycur.execute("insert into supplier values('Raju','frozen food')")
    con.commit()

c=0
mycur.execute("select * from store")
for h in mycur:
    c+=1
if c==0:
    mycur.execute("insert into store values('Good Day','Lays','Pepsi','Dairy Milk','Spring Rolls')")
    mycur.execute("insert into store values('Jim Jam','Uncle Chips','Coca Cola','Kit Kat','French Fries')")
    mycur.execute("insert into store values('Bourbon','Bingo!','Mountain Dew','Snickers','Chicken Nuggets')")
    mycur.execute("insert into store values('Marie Gold','Too Yumm!','Fanta','Toblerone','Microwave Dosa')")
    mycur.execute("insert into store values('Oreo','Haldiram','Sprite','Milky Way','Veg Patty')")
    con.commit()
    
def emp_login():
    print("--------LOGIN--------")
    name=input("Enter user name:")
    passwd=input("Enter password:")
    query="Select password from employee;"
    mycur.execute(query)
    data=mycur.fetchall()
    res = " ".join(map(str,data))
    if passwd in res:
        print("="*80)
        print(" "*30,"LOGIN SUCCESSFUL!!"," "*25)
        print(" "*30,"WELCOME",name.capitalize()," "*25)
        print("="*80)
        while True:
            print("------TASKS-----")
            print("1. Add new items")
            print("2. View all items")
            print("3. Delete a record")
            print("4. Update")
            print("5. Supplier details")
            print("6. New employee")
            print("7. View employee details")
            print("8.Log Out")
            ch9=int(input("What would you like to do ?"))
            if ch9==1:
                while True:
                    print(" "*80)
                    print("-------ADD NEW ITEMS-------")
                    item_name=input("ENTER NEW BISCUITS ITEM NAME:") 
                    item_name1=input("ENTER NEW CHIPS ITEM NAME:")
                    item_name2=input("ENTER NEW COLD DRINKS ITEM NAME:") 
                    item_name3=input("ENTER NEW CHOCOLATE ITEM NAME:")
                    item_name4=input("ENTER NEW FROZEN FOOD ITEM NAME:")
                    query="insert into store values('%s','%s','%s','%s','%s')"%(item_name,item_name1,item_name2,item_name3,item_name4)
                    mycur.execute(query)
                    con.commit()
                    print("Record Successfully Inserted.......")
                    x=input("Do you want to enter more items(y/n):")
                    if x=='n':
                        print(" "*80)
                        break

            elif ch9==2:
                print(" "*80)
                print("------------------------------------------------------------")
                print("('BISCUITS','CHIPS','COLD DRINKS','CHOCOLATE','FROZEN FOOD')")
                print("------------------------------------------------------------")
                mycur.execute("select * from store")
                data=mycur.fetchall()
                for i in data:
                    print(i)
                    print(" "*80)

            elif ch9==3:
                print(" " *80)
                print("--COLUMNS IN STORE--")
                print("1:Biscuits")
                print("2:Chips")
                print("3:Cold_Drinks")
                print("4:Chocolate")
                print("5:Frozen_Foods")
                h=input("ENTER COLUMN NAME:") 
                item_to_be_deleted=input("ENTER ANY ITEM NAME FROMABOVE COLUMN:")
                quer="delete from store where{}='{}'".format(h,item_to_be_deleted)
                mycur.execute(quer)
                con.commit()
                print("::::::::::::::")
                print("ITEM DELETED:)")
                print("::::::::::::::")
                print(" "*80)

            elif ch9==4:
                print(" " *80)
                print("--COLUMNS IN STORE--")
                print("1:Biscuits")
                print("2:Chips") 
                print("3:Cold_Drinks")
                print("4:Chocolate")
                print("5:Frozen_Foods")
                c=input("TO WHIH COLUMN DO U WANT UPDATE ITEM NAME:")
                old_name=input("ENTER OLD_NAME:")
                new_name=input("ENTER NEW_ITEM_NAME: ")
                query="update store set {}='{}' where {}='{}'".format(c,new_name,c,old_name)
                mycur.execute(query)
                con.commit()
                print(":::::::::::::::")
                print("STORE UPDATED:)")
                print(":::::::::::::::")
                print(" "*80)

            elif ch9==5:
                print(" "*80)
                print("----------------------------------")
                print("('SUPPLIER NAME','ITEM SUPPLYING')")
                print("----------------------------------")
                mycur.execute("select * from supplier")
                data=mycur.fetchall()
                for i in data:
                    print(i)
                    print(" "*80)

            elif ch9==6:
                print(" "*80)
                print("------NEW RECORD------")
                emp_name=input("Enter name:")
                emp_password=input("Enter password:")
                query="Select password from employee;"
                mycur.execute(query)
                data=mycur.fetchall()
                res = " ".join(map(str,data))
                if emp_password in res:
                    print("==PASSWORD ALREADY EXITS==")
                    z=int(input("ENTER PASSWORD:"))
                    query="insert into employee values('{}',{})".format(emp_name,z)
                    mycur.execute(query)
                    con.commit()
                    print("Record Successfully Inserted...")
                    print(" "*80)
                else:
                    query1="insert into employe values('{}',{})".format(emp_name,emp_password) 
                    mycur.execute(query1) 
                    con.commit()
                    print("Record Successfully Inserted...")
                    print(" "*80)

            elif ch9==7:
                print(" "*80)
                print("----------------------------------")
                print("('EMPLOYEE NAME','PASSWORD')")
                print("----------------------------------")
                mycur.execute("select * from employee")
                data=mycur.fetchall()
                for i in data:print(i)
                print(" "*80)
                
            elif ch9==8:
                break
    else:
        print("---------------")
        print("WRONG PASSWORD")
        print("---------------")

def place_order(a):
    for j in range(a):
        item_name=input("enter the item name you want to order:")
        item_quantity=int(input("enter how much quantity of the item selected do you want to buy :")) 
        total_price=1*item_quantity
        query="insert into cart values(('%s'),('%s'),('%s'))"%(item_name,item_quantity,total_price) 
        mycur.execute(query) 
        con.commit() 
        n=input("DO YOU WANT ORDER MORE ITEMS:y/n")
        if n=='y':
           menu()
        else:
           print_bill()
           empty_cart()

def empty_cart():
   mycur.execute("use term1_project")
   mycur.execute("delete from cart")
   con.commit()

def cust_login():
   print(" "*80)
   print("******LOGIN******")
   name=input("Enter name")
   passwd=input("Enter password")
   query1="Select cust_password from customer;"
   mycur.execute(query1)
   data1=mycur.fetchall()
   res1= " ".join(map(str,data1))
   if passwd in res1:
       print("="*80)
       print(" "*30,"LOGIN SUCCESSFUL!!"," "*25)
       print(" "*30,"WELCOME",name.capitalize()," "*25)
       print("="*80)
       menu()
   else:
       print("==============")
       print("WRONG PASSWORD")
       print("==============")

def sign_up():
   print(" "*80)
   print("******SIGN-UP******")
   cust_name=input("ENTER YOUR NAME:")
   cust_phoneNo=int(input("ENTER YOUR POHONE NUMBER:"))
   cust_password=input("ENTER PASSWORD:")
   query2="Select cust_password from customer;"
   mycur.execute(query2)
   data2=mycur.fetchall()
   res2= " ".join(map(str,data2))
   if cust_password in res2:
       print("==PASSWORD ALREADY EXISTS==")
       cust_password1=input("ENTER NEW PASSWORD->")
       query="insert into customer values(('%s'),('%s'),('%s'))"%(cust_name,cust_password1,cust_phoneNo)
       mycur.execute(query)
       con.commit()
       print("Record Successfully Inserted.......")
   else:
       query="insert into customer values(('%s'),('%s'),('%s'))"%(cust_name,cust_password,cust_phoneNo)
       mycur.execute(query)
       con.commit()
       print("Record Successfully Inserted.......")
   a=input("DO YOU WANT TO CONTINUE SHOPPING?y/n")
   if a=='y':
       print("--------WELCOME",cust_name.capitalize(),"--------")
       menu()
       
   
       
    

def print_bill():
    print(" "*80)
    print("------------BILL------------")
    print('ITEM NAME','QUANTITY','PRICE')
    query3="select *from cart"
    mycur.execute(query3)
    data2=mycur.fetchall()
    for l in data2:
        print (l)
        print('--------TOTAL PRICE---------')
        query4="select sum(Total_price) from cart"
        mycur.execute(query4)
        dat=mycur.fetchall()
        for k in dat:
            print(k)
            print(" "*80)

def menu():
    print("-----MENU-----")
    print("1:Biscuits")
    print("2:Chips")
    print("3:Cold_Drinks")
    print("4:Chocolate")
    print("5:Frozen_Foods")
    print("--------------")
    ch3=input("WHAT DO YOU WANT TO BUY:")
    if ch3=='1' or ch3=='biscuits':
        mycur.execute("select biscuits from store")
        data=mycur.fetchall()
        print("=================")
        print(" ")
        for i in data:
            print(i)
            print(" ")
            print("=================")
        a=int(input("HOW MANY BISCUITS DO YOU WANT TO BUY:"))
        place_order(a)

    elif ch3=='2' or ch3=='chips':
        mycur.execute("select chips from store")
        data=mycur.fetchall()
        print("=================")
        print(" ")
        for i in data:
            print(i)
            print(" ")
            print("=================")
        b=int(input("HOW MANY CHIPS DO YOU WANT TO BUY:"))
        place_order(b)

    elif ch3=='3' or ch3=='cold drinks':
        mycur.execute("select cold_drinks from store")
        data=mycur.fetchall()
        print("=================")
        print(" ")
        for i in data:
            print(i)
            print(" ")
            print("=================")
        c=int(input("HOW MANY COLD-DRINK DO YOU WANT TO BUY:"))
        place_order(c)

    elif ch3=='4' or ch3=='chocolate':
        mycur.execute("select chocolate from store")
        data=mycur.fetchall()
        print("=================")
        print(" ")
        for i in data:
            print(i)
            print(" ")
            print("=================")
        d=int(input("HOW MANY CHOCOLATE DO YOU WANT TO BUY:"))
        place_order(d)

    elif ch3=='5' or ch3=='frozen food':
        mycur.execute("select frozen_foods from store")
        data=mycur.fetchall()
        print("=================")
        print(" ")
        for i in data:
            print(i)
            print(" ")
            print("=================")
        e=int(input("HOW MANY Frozen Food DO YOU WANT TO BUY:"))
        place_order(e)

    else:
        print("-----WRONG CHOICE----")

while True:
    print("*"*80)
    print(" "*80)
    print(" "*30," $$$ ONE DOLLAR STORE $$$ "," "*25)
    print(" "*80)
    print("*"*80)
    print("1->Employee Login")
    print("2->Customer")
    print("3->Exit")
    ch1=int(input("ENTER CHOICE:"))
    if ch1==1:
        emp_login()
    elif ch1==2:
        print("------------------")
        print(" WELCOME CUSTOMER ")
        print("------------------")
        print("1.Order As Guest")
        print("2.Log In")
        print("3.Sign Up")
        print("------------------")
        ch2=int(input("ENTER CHOICE:"))
        if ch2==1:
            print(" "*80)
            x=input("ENTER YOUR NAME:")
            print("----WELCOME",x.capitalize(),"----")
            menu()
        elif ch2==2:
            cust_login()
        elif ch2==3:
            sign_up()
        else:
            print("----WRONG CHOICE----")
    elif ch1==3:
        break
    else:
        print("----WRONG CHOICE----")
