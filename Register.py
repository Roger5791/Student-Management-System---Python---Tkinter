from tkinter import *

from tkinter import ttk

import pymysql
from PIL import Image, ImageTk
from tkinter import messagebox


class Register:
    def __init__(self, root):
        self.root=root
        self.root.title("Registration")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

       

        #=====Background========
        bgRight=Label(self.root, bg="#021e2f").place(width=1350,relheight=1)
        bgLeft=Label(self.root, bg="#08A3D2").place(width=480, relheight=1)

        


        #=======Register Frame======
        frame1=Frame(self.root, bg="white")
        frame1.place(x=300,y=100,width=800,height=500)

        title=Label(frame1,text="Register", font=("times new roman",30,"bold","underline"),bg="white",fg="#021e2f").place(x=360,y=20)

          #=====Login Image========


        self.original = Image.open('images/registration.jpg')
        resized = self.original.resize((400, 400),Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(resized) 
        image=Label(self.root, image=self.image).place(x=80,y=140,width=400,height=400)

        #======First Name & last Name=======
        self.firstNameVar=StringVar()
        firstName=Label(frame1,text="First Name", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=220,y=100)
        self.input_firstName=Entry(frame1,font=("times new roman",15),textvariable=self.firstNameVar,bg="lightgray")
        self.input_firstName.place(x=220,y=130,width=250)

        lastName=Label(frame1,text="Last Name", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=100)
        self.input_lastName=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.input_lastName.place(x=500,y=130,width=250)


        #======Contact & Email==========
        contact=Label(frame1,text="Contact No", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=220,y=170)
        self.input_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.input_contact.place(x=220,y=200,width=250)

        email=Label(frame1,text="Email", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=170)
        self.input_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.input_email.place(x=500,y=200,width=250)


        #========Security Question=========
        question=Label(frame1,text="Security Question", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=220,y=240)
        self.cmbo_question=ttk.Combobox(frame1,font=("times new roman",13),state='readonly')
        self.cmbo_question['values']=("Select", "Your Pet Name", "Your Birth Place", "Your Favorite Food")
        self.cmbo_question.place(x=220,y=270,width=250)
        self.cmbo_question.current(0)

        answer=Label(frame1,text="Security Answer", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=240)
        self.input_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.input_answer.place(x=500,y=270,width=250)


        
        #======Password==========
        password=Label(frame1,text="Password", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=220,y=310)
        self.input_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.input_password.place(x=220,y=340,width=250)

        cnPassword=Label(frame1,text="Confirm Password", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=310)
        self.input_cnPassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.input_cnPassword.place(x=500,y=340,width=250)


        #=======Terms & Conditions=======
        self.chkBoxVar=IntVar()
        chkBox=Checkbutton(frame1,text="I Agree to the Terms & Conditions",variable=self.chkBoxVar,onvalue=1,offvalue=0,font=("times new roman",12),bg="white").place(x=220,y=380)

        #===========Buttons=============

        self.btn_img = Image.open('images/button.jpg')
        resizedBtn = self.btn_img.resize((200, 60),Image.Resampling.LANCZOS)
        self.btnImage = ImageTk.PhotoImage(resizedBtn) 
        reg_btn=Button(frame1,image=self.btnImage,bd=0,cursor="hand2",command=self.register_user).place(x=220,y=420)
        login_btn=Button(self.root,text="Login",command=self.login_toggle,font=("times new roman",20),bg="#B00857",fg="white",cursor="hand2").place(x=200,y=460,width=150,height=40)

    def register_user(self):
        if self.input_firstName.get()=="" or self.input_email.get()=="" or self.input_contact.get()=="" or self.cmbo_question.get()=="Select" or self.input_answer.get()=="" or self.input_password.get()=="" or self.input_cnPassword.get()=="":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)

        elif self.input_password.get()!=self.input_cnPassword.get():
            messagebox.showerror("Error", "Password & Confirm Password should match", parent=self.root)

        elif self.chkBoxVar.get()==0:
             messagebox.showerror("Error", "Please Agree to the Terms & Conditions", parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="student management system")
                cur=con.cursor()
                cur.execute("select * from users where email=%s",self.input_email.get())
                row=cur.fetchone()

                if row!=None:
                     messagebox.showerror("Error", "User Already Exists, Please try anothe Email", parent=self.root)

                else:
                    cur.execute("insert into users (firstName,lastName,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    self.input_firstName.get(),
                                    self.input_lastName.get(),
                                    self.input_contact.get(),
                                    self.input_email.get(),
                                    self.cmbo_question.get(),
                                    self.input_answer.get(),
                                    self.input_password.get(),
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                    self.clear()

            except Exception as es:
                 messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


       
    def clear(self):
        self.input_firstName.delete(0,END)
        self.input_lastName.delete(0,END)
        self.input_contact.delete(0,END)
        self.input_email.delete(0,END)
        self.cmbo_question.current(0)
        self.input_answer.delete(0,END)
        self.input_password.delete(0,END)
        self.input_cnPassword.delete(0,END)


    def login_toggle(self):
         self.root.destroy()
         import Login


root=Tk()
obj=Register(root)
root.mainloop()