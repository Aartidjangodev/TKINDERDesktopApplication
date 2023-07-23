from tkinter import *
import pymysql
from tkinter import messagebox
win=Tk()
win.title('CRUD APP')
win.geometry('700x800')
win.configure(bg='gray')
def insertRecord():
    myconn=pymysql.connect(host='localhost',user='root',passwd='',database='tkinterdb')
    mycur=myconn.cursor()
    vempid=e1.get() # get the value from tesxbox
    vname= e2.get()
    vsalary = e3.get()
    mycur.execute("insert into employee values('"+vempid+"','"+vname+"', '"+vsalary+"')")

    messagebox.showinfo('insert','Record inserted')
    myconn.commit()
    myconn.close()
from tkinter import  ttk # treeview
def showAll():
    myconn=pymysql.connect(host='localhost',user='root',passwd='',database='tkinterdb')
    mycur=myconn.cursor()

    mycur.execute("select * from employee")
    data=mycur.fetchall()
    # create tree view which dislplay the data in rows and columns...
    tv=ttk.Treeview(win,columns=(1,2,3),show="headings",height="10")
    tv.place(x=200,y=280)
    tv.heading(1,text="ID")
    tv.heading(2, text="E.Name")
    tv.heading(3, text="E.Salary")
    # display the data in the TREEview
    for d in data:
        tv.insert('','end',values=d)

    myconn.close()
def getRecord():
    if(e1.get()==""):
        messagebox.showinfo("info"," id is compulsory to get the values")
    else:
        myconn = pymysql.connect(host='localhost', user='root', passwd='', database='tkinterdb')
        cur = myconn.cursor()
        vempid = e1.get()
        #cur.execute(" select name,salary from employee where empid='"+vempid+"'")
        cur.execute(" select * from employee where empid='" + vempid + "'")
        result=cur.fetchall()

        for d in result: # data[0] empid   data[1]   name data[3]= salary
            e2.insert(0,d[1]) # e2 is the name of the texbox displaying values in the testbox
            e3.insert(0,d[2])
        myconn.close()
def updateRecord():
    # fetch the value of textboxex
    vempid=e1.get()
    vname=e2.get()
    vsalary=e3.get()

    if(vempid=="" or vname=="" or vsalary==""):
        messagebox.showinfo("update status"," values should be visible")
    else:
        myconn = pymysql.connect(host='localhost', user='root', passwd='', database='tkinterdb')
        cur = myconn.cursor()
        vempid = e1.get()
        #update employee set name"john",sal=3778 ehere id=1011
        cur.execute(" update employee set name='" + vname + "',salary='" + vsalary + "' where empid='" + vempid + "'")
        myconn.commit()
        myconn.close()
def DeleteRecord():
    #
    vempid=e1.get()
    if(vempid=="" ):
        messagebox.showinfo(" Delete status"," id compulsary to delete")
    else:
        myconn = pymysql.connect(host='localhost', user='root', passwd='', database='tkinterdb')
        cur = myconn.cursor()
        vempid = e1.get()
        # delete from tablename where id=101;
        cur.execute(" delete from employee where empid='"+vempid+"'")
        myconn.commit()
        messagebox.showinfo('Delete','Deleted succesfuly')
        myconn.close()
def clear(): # clearing the texboxes
    e1.delete(0,'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
lb1=Label(win,text='Enter the Empid')
lb1.place(x=50,y=50)
lb2=Label(win,text='Enter the Name')
lb2.place(x=50,y=80)
lb3=Label(win,text='Enter the Salary')
lb3.place(x=50,y=110)
e1=Entry(win,bd=5,bg='pink')
e1.place(x=150,y=50)
e2=Entry(win,bd=5,bg='pink')
e2.place(x=150,y=80)
e3=Entry(win,bd=5,bg='pink')
e3.place(x=150,y=110)

b1=Button(win,text='Insert',command=insertRecord)
b1.place(x=100,y=160)
b2=Button(win,text='Update',command=updateRecord)
b2.place(x=200,y=160)
b3=Button(win,text='Delete',command=DeleteRecord)
b3.place(x=300,y=160)
b4=Button(win,text='GETData',command=getRecord)
b4.place(x=400,y=160)
b5=Button(win,text='ShowALL',command=showAll)
b5.place(x=500,y=160)
b6=Button(win,text='Clear',command=clear)
b6.place(x=600,y=160)

win.mainloop()