from tkinter import *
from tkinter import messagebox
import os
import tkinter as tk
import mysql.connector
from tkinter import ttk
from tkinter import messagebox as tkMessageBox
from tkinter.font import Font

import math

password = input("Enter password for root user:")
#=================DATABASE SETUP==========================


mydb=mysql.connector.connect(host="localhost",user="root",passwd=password)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Stationary_Management;")
mycursor.execute("USE Stationary_Management;")
mycursor.execute("CREATE TABLE IF NOT EXISTS stock_management(item_name CHAR(30),item_code VARCHAR(10), CP FLOAT(10,2), SP FLOAT(10,2), quantity INT(5), manufacturer VARCHAR(30), total_cost FLOAT(10,2), category VARCHAR(30), supply_d DATE );")
mycursor.execute("CREATE TABLE IF NOT EXISTS sell_item( customer_name VARCHAR(30), phone_no INT(10), selling_d DATE ,item_n VARCHAR(30),price FLOAT(10,2),quantity INT(10) ,discount FLOAT(10,2), total_price FLOAT(10,2) );" )
mycursor.close()
mydb.close()

#================MAIN WINOW=================================

def mainwindow():
    global mw
    mw = Tk()
    mw.title('Stationary Management')
    mw.configure(bg='#D8BFD8',)
    Label (mw, text= '               ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=0, column=0,)       #TOP  SPACING
    Label (mw, text= '               ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=10, column=0,)      #BOTTOM   SPACING
    Label (mw, text='                ', bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=1, column=0,)   #LEFT  SPACING
    Label (mw, text='STATIONARY MANAGEMENT', bg='black', fg='white', font='Algerian 24 ') .grid(row=1, column=1,)
    Label (mw, text='                ', bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=1, column=2,)   #RIGHT  SPACING
    Label (mw, text='Welcome Sir !!!', bg='black', fg='white', font=' impact 18 ') .grid(row=2, column=1)
    Button (mw, text='Stock \nManagement', width=15, height=2, command=stalkmanagement) .grid(row=3, column=1,pady=2)
    Button (mw, text='Product \nDescription', width=15, height=2, command=productdescription) .grid(row=5, column=1,pady=2)
    Button (mw, text='Sell an Item', width=15, height=2, command=sellitem) .grid(row=7, column=1,pady=2)
    Button (mw, text='Exit', width=10, height=1, command=exitmw) .grid(row=9, column=1,pady=2)
    
    mw.mainloop()

def exitmw():
    mw.destroy()


#===============STOCK MANAGEMENT==========================

def stalkmanagement():
    global sm
    global item_n,item_c,sp,cp,qty,manf,ctgry,splyd,totc
    sm = Tk()
    sm.title('STOCK MANAGEMENT')
    sm.configure(bg='#D8BFD8')
    mw.destroy()

                            # LABELS
    
    Label (sm, text= '                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=0, column=0, sticky=W)     #TOP  SPACING
    Label (sm, text= '                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=10, column=0, sticky=W)    #BOTTOM   SPACING
    Label (sm, text= '                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=1, column=0, sticky=W)     #LEFT  SPACING
    Label (sm, text= 'STOCK MANAGEMENT',bg='black', fg='white', font='Algerian 18 ') .grid(row=1, column=1, sticky=W)
    Label (sm, text= '                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=1, column=2, sticky=W)     #RIGHT  SPACING

    Label (sm, text='Item Name',bg='#FFDD44', fg='black', font='Georgia 12 bold',width=9) .grid(row=2, column=0, pady=2,columnspan=2)
    Label (sm, text='Item Code',bg='#FFDD44', fg='black', font='Georgia 12 bold',width=9) .grid(row=3, column=0, pady=2,columnspan=2)
    Label (sm, text='Selling Price',bg='#FFDD44', fg='black', font='Georgia 12 bold',width=9) .grid(row=4, column=0, pady=2,columnspan=2)
    Label (sm, text='Cost Price',bg='#FFDD44', fg='black', font='Georgia 12 bold',width=9) .grid(row=5, column=0, pady=2,columnspan=2)
    Label (sm, text='Quantity',bg='#FFDD44', fg='black', font='Georgia 12 bold',width=9) .grid(row=6, column=0, pady=2,columnspan=2)
    Label (sm, text='Manufacturer',bg='#FFDD44', fg='black', font='Georgia 11 bold',width=10) .grid(row=7, column=0, pady=2,columnspan=2)
    Label (sm, text='Category',bg='#FFDD44', fg='black', font='Georgia 12 bold',width=9) .grid(row=8, column=0, pady=2,columnspan=2)
    Label (sm, text='Supply Date',bg='#FFDD44', fg='black', font='Georgia 12 bold',width=9) .grid(row=9, column=0, pady=2,columnspan=2)
    Label (sm, text='Total Cost',bg='#FFDD44', fg='black', font='Georgia 12 bold',width=9) .grid(row=10, column=0, pady=2,columnspan=2)

                            #BUTTONS
    
    Button(sm, text='Submit',width=10, height=1,command=submitsm) .grid(row=11, column=1,pady=2,columnspan=3)
    Button(sm, text='Back',width=10, height=1,command=exitsm) .grid(row=11, column=0,pady=2,columnspan=2)
    Button(sm, text='Clear',width=10, height=1,command=clearsm) .grid(row=12, column=1,pady=2,columnspan=3)

                            # ENTRIES

    item_n=Entry (sm, width=15,bg='white')
    item_n.grid(row=2, column=1, pady=2,columnspan=2)

    item_c=Entry (sm, width=15,bg='white')
    item_c.grid(row=3, column=1, pady=2,columnspan=2)

    sp=Entry (sm, width=15,bg='white')
    sp.grid(row=4, column=1, pady=2,columnspan=2)

    cp=Entry (sm, width=15,bg='white')
    cp.grid(row=5, column=1, pady=2,columnspan=2)

    qty=Entry (sm, width=15,bg='white')
    qty.grid(row=6, column=1, pady=2,columnspan=2)

    manf=Entry (sm, width=15,bg='white')
    manf.grid(row=7, column=1, pady=2,columnspan=2)

    ctgry=Entry (sm, width=15,bg='white')
    ctgry.grid(row=8, column=1, pady=2,columnspan=2)

    splyd=Entry (sm, width=15,bg='white')
    splyd.grid(row=9, column=1, pady=2,columnspan=2)

    totc= Text(sm, width=11,height=1,bg='white',wrap=WORD)
    totc.grid(row=10, column=1, pady=2,columnspan=2)
    
                    # SETTING  DEFAULT VALUES
                    
    item_n.insert(END,'NONE')
    item_c.insert(END,'NONE')
    sp.insert(END,0.00)
    cp.insert(END,0.00)
    qty.insert(END,0)
    manf.insert(END,'NONE')
    ctgry.insert(END,'NONE')
    splyd.insert(END,'2000-01-01')
    totc.insert(END,0.00)
    

    
    sm.mainloop()

def exitsm():
    sm.destroy()
    mainwindow()

def clearsm():
    item_n.delete(0, END)
    item_c.delete(0, END)
    sp.delete(0, END)
    cp.delete(0, END)
    qty.delete(0, END)
    manf.delete(0, END)
    ctgry.delete(0, END)
    splyd.delete(0, END)
    totc.delete(0.0, END)
    
                        # RESETTING  DEFAULT VALUES
                        
    item_n.insert(END,'NONE')
    item_c.insert(END,'NONE')
    sp.insert(END,0.00)
    cp.insert(END,0.00)
    qty.insert(END,0)
    manf.insert(END,'NONE')
    ctgry.insert(END,'NONE')
    splyd.insert(END,'2000-01-01')
    totc.insert(END,0.00)

def submitsm():

                    #SETTING THE VALUE OF TOTAL COST
                    # c1 , c2 , c3 , ...  are column1, column2, column3, ...
                    
    c4=float(cp.get())
    c5=float(qty.get())
    c9=c4*c5
    c9=str(c9)
    totc.delete(0.0, END)
    totc.insert(END,c9)

    c1=str(item_n.get())
    c2=str(item_c.get())
    c3=float(sp.get())
    c6=str(manf.get())
    c7=str(ctgry.get())
    c8=str(splyd.get())

                    #STORING INFORMATION IN MYSQL
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=password)
    mycursor = mydb.cursor()
    mycursor.execute('USE Stationary_Management')
    sql="INSERT INTO stock_management(item_name,item_code, CP, SP,quantity,manufacturer,total_cost,category,supply_d) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val= (c1,c2,c4,c3,c5,c6,c9,c7,c8)
    mycursor.execute(sql, val )
    mydb.commit()
    mycursor.execute('SELECT * FROM stock_management; ')
    for x in mycursor:
        print(x)
    mycursor.close()
    mydb.close()
    

#================PRODUCT DESCRIPTION=======================

def productdescription():
    global pd
    pd = Tk()
    pd.title('PRODUCT DESCRIPTION')
    pd.configure(bg='#D8BFD8')
    mw.destroy()

                    #FRAMES
    
    fmpd1= Frame(pd)
    fmpd1.grid(row=1,column=0)
    fmpd1.configure(bg='#D8BFD8')
    fmpd2=Frame(pd)
    fmpd2.configure(bg='#D8BFD8')
    fmpd2.grid(row=2,column=0)
    fmpd3=Frame(pd)
    fmpd3.configure(bg='#D8BFD8')
    fmpd3.grid(row=3,column=0)
    fmpd4=Frame(pd)
    fmpd4.configure(bg='#D8BFD8')
    fmpd4.grid(row=4,column=0)


    w1=13
    w2=16

                    #LABELS

    Label (pd, text= '                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=0, column=0, sticky=W)     #TOP  SPACING
    Label (pd, text= '                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=10, column=0, sticky=W)    #BOTTOM   SPACING
    Label (fmpd1, text= '                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=1, column=0, sticky=W)     #LEFT  SPACING
    Label (fmpd1, text= 'PRODUCT DESCRIPTION',bg='black', fg='white', font='Algerian 18 ') .grid(row=1, column=1, sticky=W)
    Label (fmpd1, text= '                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=1, column=2, sticky=W)     #RIGHT  SPACING

    Label (fmpd2, text='Item Name',bg='#FFDD44', fg='black', font='none 12 bold',width=w1) .grid(row=2, column=0, pady=2)
    Label (fmpd2, text='Item Code',bg='#FFDD44', fg='black', font='none 12 bold',width=w1) .grid(row=2, column=1, pady=2)
    Label (fmpd2, text='Selling Price',bg='#FFDD44', fg='black', font='none 12 bold',width=w1) .grid(row=2, column=2, pady=2)
    Label (fmpd2, text='Cost Price',bg='#FFDD44', fg='black', font='none 12 bold',width=w1) .grid(row=2, column=3, pady=2)
    Label (fmpd2, text='Quantity',bg='#FFDD44', fg='black', font='none 12 bold',width=w1) .grid(row=2, column=4, pady=2)
    Label (fmpd2, text='Manufacturer',bg='#FFDD44', fg='black', font='none 12 bold',width=w1) .grid(row=2, column=5 ,pady=2)
    Label (fmpd2, text='Total Cost',bg='#FFDD44', fg='black', font='none 12 bold',width=w1) .grid(row=2, column=6, pady=2)
    Label (fmpd2, text='Category',bg='#FFDD44', fg='black', font='none 12 bold',width=w1) .grid(row=2, column=7, pady=2)
    Label (fmpd2, text='Supply Date',bg='#FFDD44', fg='black', font='none 12 bold',width=w1) .grid(row=2, column=8, pady=2)
    Button(fmpd4, text='Back',width=10, height=1,command=exitpd) .grid(row=11, column=0,pady=2,columnspan=2)
    Button(fmpd4, text='Delete Item',width=10, height=1,command=deletewindow) .grid(row=11, column=2,pady=2,columnspan=2)

    

                            #SQL COMMANDS    
   
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=password)
    mycursor = mydb.cursor()
    mycursor.execute("USE Stationary_Management;")
    

    w=22
    
    mycursor.execute('SELECT item_name FROM stock_management; ')
    
    lb1=Listbox(fmpd3)
    lb1.grid(column=0,row=0)
    lb1.configure(width=w)
    
    for x in mycursor:
        y=str(x)
        y=y[2:-3]
        lb1.insert(END,y)
    

    mycursor.execute('SELECT item_code FROM stock_management; ')
    
    lb2=Listbox(fmpd3)
    lb2.grid(column=1,row=0)
    lb2.configure(width=w)
    
    for x in mycursor:
        y=str(x)
        y=y[2:-3]
        lb2.insert(END,y)

    mycursor.execute('SELECT CP FROM stock_management; ')
    
    lb3=Listbox(fmpd3)
    lb3.grid(column=2,row=0)
    lb3.configure(width=w)
    
    for x in mycursor:
        y=str(x)
        y=y[1:-2]
        lb3.insert(END,y)

    mycursor.execute('SELECT SP FROM stock_management; ')
    
    lb4=Listbox(fmpd3)
    lb4.grid(column=3,row=0)
    lb4.configure(width=w)
    
    for x in mycursor:
        y=str(x)
        y=y[1:-2]
        lb4.insert(END,y)
    
    mycursor.execute('SELECT quantity FROM stock_management; ')
    
    lb5=Listbox(fmpd3)
    lb5.grid(column=4,row=0)
    lb5.configure(width=w)
    
    for x in mycursor:
        y=str(x)
        y=y[1:-2]
        lb5.insert(END,y)

    mycursor.execute('SELECT manufacturer FROM stock_management; ')
    
    lb6=Listbox(fmpd3)
    lb6.grid(column=5,row=0)
    lb6.configure(width=w)
    
    for x in mycursor:
        y=str(x)
        y=y[2:-3]
        lb6.insert(END,y)

    mycursor.execute('SELECT total_cost FROM stock_management; ')
    
    lb7=Listbox(fmpd3)
    lb7.grid(column=6,row=0)
    lb7.configure(width=w)
    
    for x in mycursor:
        y=str(x)
        y=y[1:-2]
        lb7.insert(END,y)

    mycursor.execute('SELECT category FROM stock_management; ')
    
    lb8=Listbox(fmpd3)
    lb8.grid(column=7,row=0)
    lb8.configure(width=w)
    
    for x in mycursor:
        y=str(x)
        y=y[2:-3]
        lb8.insert(END,y)

    mycursor.execute('SELECT supply_d FROM stock_management; ')
    
    lb9=Listbox(fmpd3)
    lb9.grid(column=8,row=0)
    lb9.configure(width=w)
    
    for x in mycursor:
        y=str(x)
        y=y[15:-3]
        lb9.insert(END,y)

       

    pd.mainloop()



def exitpd():
    pd.destroy()
    mainwindow()

#================DELETE AN ITEM==============================

def deletewindow():
    global tv,dw
    dw=Tk()
    dw.title('DELETE AN ITEM')
                                #FRAMES
    fmdw1= Frame(dw)
    fmdw1.grid(row=1,column=0)
    fmdw1.configure(bg='#D8BFD8')
    fmdw2=Frame(dw)
    fmdw2.configure(bg='#D8BFD8')
    fmdw2.grid(row=2,column=0)

    tv=ttk.Treeview(fmdw1)

                                #COLUMNS
    
    tv.configure(column=('#0'))
    tv.column('#0',width=100,anchor='center')
    tv.heading('#0',text='Item name')
    
    tv.configure(column=('#1'))
    tv.column('#1',width=100,anchor='center')
    tv.heading('#1',text='Item code')
    
                                #BUTTON
    
    Button(fmdw2, text='Delete',width=10, height=1,command=delete)   .grid(row=11, column=2)
    
                                #SQL COMMANDS
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=password)
    mycursor = mydb.cursor()
    mycursor.execute("USE Stationary_Management;")
    mycursor.execute('SELECT item_name FROM stock_management; ')
    count=0
    for x in mycursor:
        count+=1
        y=str(x)
        y=y[2:-3]
        tv.insert('',str(count),'item'+str(count), text=y)

    tv.configure(column=('#1'))
    tv.column('#1',width=100,anchor='center')
    tv.heading('#1',text='Item code')
  

    mycursor.execute('SELECT item_code FROM stock_management; ')
    count=0
    for x in mycursor:
        count+=1
        y=str(x)
        y=y[2:-3]
        tv.set('item'+str(count),'#1',y)

    tv.pack()
#    tv.bind('<<TreeviewSelect>>',tvselect)
                            #EVENTS
def delete():
    tvselect()

def tvselect():
    x=tv.selection()
    print(x)
    
    
#================SELL AN ITEM================================

def sellitem():
    global si,cust_n,ph,selld,itmn,price,qtt,disc,totp
    si= Tk()
    si.title('SELL AN ITEM')
    si.configure(bg='#D8BFD8')
    

    mw.destroy()

                            # LABELS
    
    Label (si, text= '                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=0, column=0, sticky=W)     #TOP  SPACING
    Label (si, text= '                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=10, column=0, sticky=W)    #BOTTOM   SPACING
    Label (si, text= '                                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=1, column=0, sticky=W)     #LEFT  SPACING
    Label (si, text= 'SELL AN ITEM',bg='black', fg='white', font='Algerian 18 ') .grid(row=1, column=1, sticky=W)
    Label (si, text= '                                        ',bg='#D8BFD8', fg='white', font='none 12 bold') .grid(row=1, column=2, sticky=W)     #RIGHT  SPACING

    Label (si, text='Customer Name',bg='#FFDD44', fg='black', font='none 12 bold',width=15) .grid(row=2, column=0, pady=2,columnspan=2)
    Label (si, text='Phone Number',bg='#FFDD44', fg='black', font='none 12 bold',width=15) .grid(row=3, column=0, pady=2,columnspan=2)
    Label (si, text='Selling Date',bg='#FFDD44', fg='black', font='none 12 bold',width=15) .grid(row=4, column=0, pady=2,columnspan=2)
    Label (si, text='Item Name',bg='#FFDD44', fg='black', font='none 12 bold',width=15) .grid(row=5, column=0, pady=2,columnspan=2)
    
    Label (si, text='Price',bg='#FFDD44', fg='black', font='none 12 bold',width=15) .grid(row=6, column=0, pady=2,columnspan=2)
    Label (si, text='Quantity',bg='#FFDD44', fg='black', font='none 12 bold',width=15) .grid(row=7, column=0, pady=2,columnspan=2)
    Label (si, text='Discount',bg='#FFDD44', fg='black', font='none 12 bold',width=15) .grid(row=8, column=0, pady=2,columnspan=2)
    Label (si, text='Total Price',bg='#FFDD44', fg='black', font='none 12 bold',width=15) .grid(row=9, column=0, pady=2,columnspan=2)


                            # ENTRIES

    cust_n=Entry (si, width=15,bg='white')
    cust_n.grid(row=2, column=1, pady=2,columnspan=2)

    ph=Entry (si, width=15,bg='white')
    ph.grid(row=3, column=1, pady=2,columnspan=2)

    selld=Entry (si, width=15,bg='white')
    selld.grid(row=4, column=1, pady=2,columnspan=2)

    itmn=Entry (si, width=15,bg='white')
    itmn.grid(row=5, column=1, pady=2,columnspan=2)

    

    price=Entry (si, width=15,bg='white')
    price.grid(row=6, column=1, pady=2,columnspan=2)

    qtt=Entry (si, width=15,bg='white')
    qtt.grid(row=7, column=1, pady=2,columnspan=2)

    disc=Entry (si, width=15,bg='white')
    disc.grid(row=8, column=1, pady=2,columnspan=2)

    totp= Text(si, width=11,height=1,bg='white',wrap=WORD)
    totp.grid(row=9, column=1, pady=2,columnspan=2)

                            #BUTTONS
    Button(si, text='Submit',width=10, height=1,command=submitsi) .grid(row=10, column=0,pady=2,columnspan=2)
    Button(si, text='Clear',width=10, height=1,command=clearsi) .grid(row=10, column=1,pady=2,columnspan=3)
    Button(si, text='Back',width=10, height=1,command=exitsi) .grid(row=11, column=1,pady=2,columnspan=2)

                    # SETTING  DEFAULT VALUES

    cust_n.insert(0,'NONE')
    ph.insert(0,0000000000)
    selld.insert(0,'2000-01-01')
    itmn.insert(0,'NONE')
    price.insert(0,0.00)
    qtt.insert(0,0)
    disc.insert(0,0.00)
    totp.insert(0.0,0.00)
    
    si.mainloop()

def exitsi():
    si.destroy()
    mainwindow()

def submitsi():
    c1=str(cust_n.get())
    c2=float(ph.get())
    c3=str(selld.get())
    c4=str(itmn.get())
    c5=float(price.get())
    c6=int(qtt.get())
    c7=float(disc.get())
    c8=c5*c6 - c5*c6*c7/100

    totp.delete(0.0,END)
    totp.insert(END, c8)

    #STORING VALUES IN TABLE

    mydb=mysql.connector.connect(host="localhost",user="root",passwd=password)
    mycursor = mydb.cursor()
    mycursor.execute('USE Stationary_Management')
    sql="INSERT INTO sell_item(customer_name , phone_no , selling_d ,item_n,price ,quantity ,discount, total_price ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(c1,c2,c3,c4,c5,c6,c7,c8)
    mycursor.execute(sql, val )
    mydb.commit()

    mycursor.close()
    mydb.close()

def clearsi():
    cust_n.delete(0, END)
    ph.delete(0, END)
    selld.delete(0, END)
    itmn.delete(0, END)
    price.delete(0, END)
    qtt.delete(0, END)
    disc.delete(0, END)
    totp.delete(0.0, END)
    
                        # RESETTING  DEFAULT VALUES

    cust_n.insert(0,'NONE')
    ph.insert(0,0000000000)
    selld.insert(0,'2000-01-01')
    itmn.insert(0,'NONE')
    price.insert(0,0.00)
    qtt.insert(0,0)
    disc.insert(0,0.00)
    totp.insert(0.0,0.00)



mainwindow()

