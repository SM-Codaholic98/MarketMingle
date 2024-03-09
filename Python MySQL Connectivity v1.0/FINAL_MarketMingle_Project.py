import mysql.connector, decimal

db = mysql.connector.connect(host="localhost", user="root", password="piku@2004", database="MARKET")

def CREATE_TABLE():
    sql01 = 'USE MARKET'
    sql02 = 'CREATE TABLE Shop(S_Id VARCHAR(10) NOT NULL PRIMARY KEY, SName VARCHAR(50), Contact_Number BIGINT(10), Area VARCHAR(30), Pincode INT, City VARCHAR(30), District VARCHAR(30), State CHAR(30), ESTD DATE)'
    sql03 = 'CREATE TABLE Accessories(A_Id VARCHAR(10) NOT NULL PRIMARY KEY, AName VARCHAR(50), MRP DECIMAL(60, 2), Quantity INT, Total_Price DECIMAL(60, 2), S_Id VARCHAR(10), FOREIGN KEY (S_Id) REFERENCES Shop(S_Id))'
    
    c = db.cursor()
    c.execute(sql01)
    c.execute(sql02)
    c.execute(sql03)
    db.commit()
    print("*** SHOP table and ACCESSORIES table has been successfully added in the MARKET database ***")
    
    
def INSERT_Shop_Records():
    ans = 'y'
    while ans.lower()=='y':
        S_Id = input("Enter the shop ID : ")
        SName = input("Enter the shop Name : ")
        Contact_Number =int(input("Enter the shop's Contact Number : "))
        Area = input("Enter the shop Area : ")
        Pincode = int(input("Enter the area Pincode : "))
        City = input("Enter the City : ")
        District = input("Enter the District : ")
        State = input("Enter the State : ")
        ESTD = input("Enter the shop Establishment Date : ")
        data = (S_Id, SName, Contact_Number, Area, Pincode, City, District, State, ESTD)
        sql = "INSERT INTO Shop VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c = db.cursor()
        c.execute(sql, data)
        db.commit()
        print("*** Shop details has been successfully added in the SHOP table ***")
        print()
        ans = input("Press 'y/Y' to add more SHOP record in the SHOP table : ")
        print()
    
    
def INSERT_Accessories_Records():
    ans = 'y'
    while ans.lower()=='y':
        A_Id = input("Enter the product ID : ")
        AName = input("Enter the product Name : ")
        MRP = input("Enter the MRP of a single product : ")
        Quantity = int(input("Enter the product Quantity : "))
        Total_Price = str(Quantity * float(decimal.Decimal(MRP)))
        S_Id = input("Enter the shop ID : ")
        data = (A_Id, AName, MRP, Quantity, Total_Price, S_Id)
        sql = "INSERT INTO Accessories(A_Id, AName, MRP, Quantity, Total_Price, S_Id) VALUES(%s,%s,%s,%s,%s,%s)"
        c = db.cursor()
        c.execute(sql, data)
        db.commit()
        print("*** Product details has been successfully added in the ACCESSORIES table ***")
        print()
        ans = input("Press 'y/Y' to add more Product record in the ACCESSORIES table : ")
        print()
    
    
def DISPLAY_Shop_Table():
    ans = 'y'
    while ans.lower()=='y':
        sql = "SELECT * FROM Shop"
        c = db.cursor()
        c.execute(sql)
        rows = c.fetchall()
        for i in rows:
            print("-----------------------------------")
            print("Shop ID = ", i[0])
            print("Shop Name = ", i[1])
            print("Shop's Contact Number = ", i[2])
            print("Shop Area = ", i[3])
            print("Shop Area Pincode = ", i[4])
            print("City = ", i[5])
            print("District = ", i[6])
            print("State = ", i[7])
            print("Shop Establishment Date = ", i[8])
            print("-----------------------------------")
            print()
        ans = input("Press 'y/Y' to display the SHOP records again : ")
        print()
        
def DISPLAY_Accessories_Table():
    ans = 'y'
    while ans.lower()=='y':
        sql = "SELECT * FROM Accessories"
        c = db.cursor()
        c.execute(sql)
        rows = c.fetchall()
        for i in rows:
            print("-----------------------------------")
            print("Product ID = ", i[0])
            print("Product Name = ", i[1])
            print("Product MRP = ", i[2])
            print("Product Quantity = ", i[3])
            print("Product Total Price = ", i[4])
            print("Shop ID = ", i[5])
            print("-----------------------------------")
            print()
        ans = input("Press 'y/Y' to display the ACCESSORIES records again : ")
        print()
        
            
def DELETE_Shop_Records():
    ans = 'y'
    while ans.lower()=='y':
        id = input("Enter the shop ID : ")
        if CHECK_Shop_Record(id)==False:
            print("--> Shop ID ",id,"does not exist in the SHOP table !!!")
        else:
            sql = "DELETE FROM Shop WHERE S_Id=%s"
            data = (id,)
            c = db.cursor()
            c.execute(sql, data)
            db.commit()
            print("*** Record of the shop ID ",id,"has been successfully deleted from the SHOP table ***")
        print()
        ans = input("Press 'y/Y' to delete more shop record from the SHOP table")
        print()


def CHECK_Shop_Record(shop_ID):
    sql = "SELECT * FROM Shop WHERE S_Id=%s"
    c = db.cursor(buffered=True)
    data = (shop_ID,)
    c.execute(sql, data)
    no_of_rows = c.rowcount
    if no_of_rows==1:
        return True
    else:
        return False
    
    
def DELETE_Accessories_Records():
    ans = 'y'
    while ans.lower()=='y':
        id = input("Enter the product ID : ")
        if CHECK_Shop_Record(id)==False:
            print("--> Product ID ",id,"does not exist in the ACCESSORIES table !!!")
        else:
            sql = "DELETE FROM Accessories WHERE A_Id=%s"
            data = (id,)
            c = db.cursor()
            c.execute(sql, data)
            db.commit()
            print("*** Record of the product ID ",id,"has been successfully deleted from the ACCESSORIES table ***")
        print()
        ans = input("Press 'y/Y' to delete more product record from the ACCESSORIES table")
        print()


       
def CHECK_Accessories_Record(product_ID):
    sql = "SELECT * FROM Accessories WHERE A_Id=%s"
    c = db.cursor(buffered=True)
    data = (product_ID,)
    c.execute(sql, data)
    no_of_rows = c.rowcount
    if no_of_rows==1:
        return True
    else:
        return False
    
    
def UPDATE_Accessories_Price():
    ans = 'y'
    while ans.lower()=='y':
        id = input("Enter the product ID : ")
        if CHECK_Accessories_Record(id)==False:
            print("--> Product ID ",id,"does not exist in the ACCESSORIES table !!!")
        else:
            p = input("Enter the increased Price of the product : ")
            p = float(decimal.Decimal(p))
            qty = int(input("Enter the updated Quantity of the product : "))
            
            sql = "SELECT MRP, Quantity, Total_Price FROM ACCESSORIES WHERE A_Id=%s"
            data = (id,)
            c = db.cursor()
            c.execute(sql, data)
            
            mrp = c.fetchone()
            MRP = float(decimal.Decimal(mrp[0]))
            new_mrp = MRP + p
            tp = qty * new_mrp
            new_mrp = str(new_mrp)
            tp = str(tp)
            sql = "UPDATE Accessories SET MRP=%s, Quantity=%s, Total_Price=%s WHERE A_Id=%s"
            data = (new_mrp, qty, tp, id)
            c.execute(sql, data)
            db.commit()
            print("*** Product's MRP, Quantity and Total Price has been successfully updated in the ACCESSORIES table ***")
        print()
        ans = input("Press 'y/Y' to update more product's price in the ACCESSORIES table : ")
        
        
ans = 'y'
while ans.lower()=='y':
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MENU %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("--> Press 1 to insert shop records in the SHOP table")
    print("--> Press 2 to insert product records in the ACCESSORIES table")
    print("--> Press 3 to display the SHOP table")
    print("--> Press 4 to display the ACCESSORIES table")
    print("--> Press 5 to delete records from the SHOP table")
    print("--> Press 6 to delete records from the ACCESSORIES table")
    print("--> Press 7 to update the MRP, Quantity and Total Price of a product in the ACCESSORIES table")
    print("--> Press 8 to open the MARKET database & to create SHOP table and ACCESSORIES table")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    ch = int(input("Enter your choice : "))
    if ch==1:
        print()
        INSERT_Shop_Records()
        print()
    elif ch==2:
        print()
        INSERT_Accessories_Records()
        print()
    elif ch==3:
        print()
        DISPLAY_Shop_Table()
        print()
    elif ch==4:
        print()
        DISPLAY_Accessories_Table()
        print()
    elif ch==5:
        print()
        DELETE_Shop_Records()
        print()
    elif ch==6:
        print()
        DELETE_Accessories_Records()
        print()
    elif ch==7:
        print()
        UPDATE_Accessories_Price()
        print()
    elif ch==8:
        print()
        CREATE_TABLE()
        print()
    else:
        print()
        print("--> YOU HAVE ENTERED WRONG CHOICE !!!, please enter the correct option from the MENU __/\__")
        print()
    ans=input("Press 'y/Y' to go to the MENU : ")
    print()