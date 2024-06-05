from tkinter import *

from tkinter import ttk

import pymysql
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        
        title=Label(self.root,text="Student Management System", bd=5, relief=RIDGE, font=("times new roman", 35,"bold"))
        title.pack(side=TOP,fill=X)

        #=========Variables==========

        self.rollNoVar=StringVar()
        self.nameVar=StringVar()
        self.emailVar=StringVar()
        self.genderVar=StringVar()
        self.mobileVar=StringVar()
        self.dobVar=StringVar()
        self.genderVar=StringVar()
        self.searchByVar=StringVar()
        self.searchTxtVar=StringVar()




        themeBtn=Button(self.root,text="Toggle Theme",width=10,bg="#0D1117",fg="#F5F3F3", font=("times new roman",12,"bold"),padx=10,command=change_theme).place(x=1200,y=20)


        #======Manage Frame========

        Manage_Frame=LabelFrame(self.root ,text="Manage Students",pady=35,font=("times new roman",25,"bold"))
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        #=======Roll No=========
        Roll_No=Label(Manage_Frame,text="Roll No:",font=("times new roman", 15,"bold"))
        Roll_No.grid(row=1,column=0,pady=10,padx=20,sticky=W)

        input_Roll=Entry(Manage_Frame, textvariable=self.rollNoVar,font=("times new roman", 15,"bold"))
        input_Roll.grid(row=1,column=1,pady=10,padx=20,sticky=EW)

         #=======Name=========
        name=Label(Manage_Frame,text="Name:",font=("times new roman", 15,"bold"))
        name.grid(row=2,column=0,pady=10,padx=20,sticky=W)

        input_Name=Entry(Manage_Frame, textvariable=self.nameVar,font=("times new roman", 15,"bold"))
        input_Name.grid(row=2,column=1,pady=10,padx=20,sticky=W)

         #=======Email=========
        email=Label(Manage_Frame,text="Email:",font=("times new roman", 15,"bold"))
        email.grid(row=3,column=0,pady=10,padx=20,sticky=W)

        input_Email=Entry(Manage_Frame, textvariable=self.emailVar,font=("times new roman", 15,"bold"))
        input_Email.grid(row=3,column=1,pady=10,padx=20,sticky=W)

         #=======Gender=========
        gender=Label(Manage_Frame,text="Gender:",font=("times new roman", 15,"bold"))
        gender.grid(row=4,column=0,pady=10,padx=20,sticky=W)


        input_Gender=ttk.Combobox(Manage_Frame, textvariable=self.genderVar,width=9,state="readonly")
        input_Gender["values"]=("Male", "Female", "Other")
        input_Gender.grid(row=4,column=1,pady=10,padx=20,ipadx=65)



          #=======DOB=========
        DOB=Label(Manage_Frame,text="D.O.B:",font=("times new roman", 15,"bold"))
        DOB.grid(row=5,column=0,pady=10,padx=20,sticky=W)

        input_DOB=Entry(Manage_Frame, textvariable=self.dobVar,font=("times new roman", 15,"bold"))
        input_DOB.grid(row=5,column=1,pady=10,padx=20,sticky=W)


        #=======Mobile=========
        mobile=Label(Manage_Frame,text="Mobile:",font=("times new roman", 15,"bold"))
        mobile.grid(row=6,column=0,pady=10,padx=20,sticky=W)

        input_mobile=Entry(Manage_Frame, textvariable=self.mobileVar,font=("times new roman", 15,"bold"))
        input_mobile.grid(row=6,column=1,pady=10,padx=20,sticky=W)

        #=======Address=========
        address=Label(Manage_Frame,text="Address:",font=("times new roman", 15,"bold"))
        address.grid(row=7,column=0,pady=10,padx=20,sticky=W)

        self.input_address=Text(Manage_Frame, width=34,height=6,font=("times new roman", 10))
        self.input_address.grid(row=7,column=1,pady=10,padx=20,sticky=W)



        #=========Buttom Frame=============
        
        btn_Frame=Frame(Manage_Frame, bd=4, relief=RIDGE,bg="gray")
        btn_Frame.place(x=15,y=430,width=420)

        addBtn=Button(btn_Frame,text="Add",width=10, bg="#0D1117", fg="#F5F3F3", font=("bold",10), command=self.add_students).grid(row=0,column=0,padx=6,pady=10)
        updateBtn=Button(btn_Frame,text="Update",  bg="#0D1117",fg="#F5F3F3",width=10,font=("bold",10), command=self.update_data).grid(row=0,column=1,padx=6,pady=10)
        deleteBtn=Button(btn_Frame,text="Delete", bg="#0D1117", fg="#F5F3F3",width=10,font=("bold",10), command=self.delete_data).grid(row=0,column=2,padx=6,pady=10)
        clearBtn=Button(btn_Frame,text="Clear",  bg="#0D1117",fg="#F5F3F3",width=10,font=("bold",10), command=self.clear).grid(row=0,column=3,padx=6,pady=10)



        #========Detail Frame=============

        Detail_Frame=Frame(self.root, bd=4, relief=RIDGE,bg="#0D1117")
        Detail_Frame.place(x=500,y=100,width=800,height=580)

        #=======Search========
        search=Label(Detail_Frame,fg="#F5F3F3",bg="#0D1117",text="Search By:",font=("times new roman", 20,"bold"))
        search.grid(row=0,column=0,pady=10,padx=20,sticky=W)
        variable = self.searchByVar

        combo_Search=ttk.OptionMenu(Detail_Frame, variable,"Select", "Roll_No", "Name", "Mobile")
       
        combo_Search.grid(row=0,column=1,pady=10,padx=20,ipadx=30)


        input_Search=Entry(Detail_Frame, textvariable=self.searchTxtVar, width=20,font=("times new roman", 16,"bold"))
        input_Search.grid(row=0,column=2,pady=10,padx=10,sticky=W)

        searchBtn=Button(Detail_Frame,text="Search",width=10, command=self.search_data,pady=4).grid(row=0,column=3,padx=5,pady=10)
        showAllBtn=Button(Detail_Frame,text="Show All",width=10, command=self.fetch_data,pady=4).grid(row=0,column=4,padx=10,pady=10)

        #=====Table Frame=========
        
        Table_Frame=Frame(Detail_Frame, bd=4, relief=RIDGE,bg="#0D1117")
        Table_Frame.place(x=10,y=60,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.student_Table=ttk.Treeview(Table_Frame, columns=("Roll No", "Name", "Email", "Gender", "Mobile", "D.O.B", "Address"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_Table.xview)
        scroll_y.config(command=self.student_Table.yview)
        self.student_Table.heading("Roll No", text="Roll No")
        self.student_Table.heading("Name", text="Name")
        self.student_Table.heading("Email", text="Email")
        self.student_Table.heading("Gender", text="Gender")
        self.student_Table.heading("Mobile", text="Mobile")
        self.student_Table.heading("D.O.B", text="D.O.B")
        self.student_Table.heading("Address", text="Address")

        self.student_Table['show']='headings'

        self.student_Table.column("Roll No",width=60)
        self.student_Table.column("Name",width=100)
        self.student_Table.column("Email",width=150)
        self.student_Table.column("Gender",width=100)
        self.student_Table.column("Mobile",width=100)
        self.student_Table.column("D.O.B",width=100)
        self.student_Table.column("Address",width=150)
        self.student_Table.pack(fill=BOTH,expand=1)
        self.student_Table.bind("<ButtonRelease-1>", self.get_data_onClick)


        self.fetch_data()

    def add_students(self):
        if self.rollNoVar.get()=="" or self.nameVar.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        else:
            con=pymysql.connect(host="localhost", user="root", password="",database="student management system")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.rollNoVar.get(),
                                                                         self.nameVar.get(),
                                                                         self.emailVar.get(),
                                                                         self.genderVar.get(),
                                                                         self.mobileVar.get(),
                                                                         self.dobVar.get(),
                                                                         self.input_address.get('1.0',END)

            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record added succesfully!")

    def fetch_data(self):
        con=pymysql.connect(host="localhost", user="root", password="",database="student management system")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_Table.delete(*self.student_Table.get_children())
            for row in rows:
                self.student_Table.insert('', END, values=row)

            self.searchTxtVar.set("")

            con.commit()
        con.close()    

   
    def clear(self):
        self.rollNoVar.set("")
        self.nameVar.set("")
        self.emailVar.set("")
        self.genderVar.set("Select")
        self.mobileVar.set("")
        self.dobVar.set("")
        self.input_address.delete("1.0", END)


    def get_data_onClick(self, event):
        selectedRow=self.student_Table.focus()
        contents=self.student_Table.item(selectedRow)
        row=contents['values']
        self.rollNoVar.set(row[0])
        self.nameVar.set(row[1])
        self.emailVar.set(row[2])
        self.genderVar.set(row[3])
        self.mobileVar.set(row[4])
        self.dobVar.set(row[5])
        self.input_address.delete("1.0", END)
        self.input_address.insert(END, row[6])


    
    def update_data(self):
        con=pymysql.connect(host="localhost", user="root", password="",database="student management system")
        cur=con.cursor()
        cur.execute("update students set name=%s, email=%s, gender=%s, mobile=%s, dob=%s, address=%s where Roll_No=%s",(
                                                                         
                                                                         self.nameVar.get(),
                                                                         self.emailVar.get(),
                                                                         self.genderVar.get(),
                                                                         self.mobileVar.get(),
                                                                         self.dobVar.get(),
                                                                         self.input_address.get('1.0',END),
                                                                         self.rollNoVar.get(),

        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost", user="root", password="",database="student management system")
        cur=con.cursor()
        cur.execute("delete from students where Roll_No=%s", self.rollNoVar.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()



    
    def search_data(self):
        con=pymysql.connect(host="localhost", user="root", password="",database="student management system")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.searchByVar.get())+" LIKE '%"+str(self.searchTxtVar.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_Table.delete(*self.student_Table.get_children())
            for row in rows:
                self.student_Table.insert('', END, values=row)

            con.commit()
        con.close()    



    
def change_theme():
    # NOTE: The theme's real name is azure-<mode>
    if root.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        root.call("set_theme", "light")
    else:
        # Set dark theme
        root.call("set_theme", "dark")

       



root=Tk()
ob=Student(root)

# Create a style
#style = ttk.Style(root)

# Import the tcl file
#root.call("source", "forest-light.tcl")

# Set the theme with the theme_use method
#style.theme_use("forest-light")

# Just simply import the azure.tcl file
root.call("source", "azure.tcl")

root.call("set_theme", "light")


root.mainloop()