from tkinter import *

from tkinter import ttk

import pymysql
from PIL import Image, ImageTk
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #=====Background========
        bgRight=Label(self.root, bg="#021e2f").place(width=1350,relheight=1)
        bgLeft=Label(self.root, bg="#08A3D2").place(width=480, relheight=1)


          #=======Register Frame======
        frame1=Frame(self.root, bg="white")
        frame1.place(x=300,y=70,width=800,height=550)

        title=Label(frame1,text="Login", font=("times new roman",30,"bold","underline"),bg="white",fg="#021e2f").place(x=410,y=30)

         #=====Login Image========

        self.original = Image.open('images/login.png')
        resized = self.original.resize((400, 400),Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(resized) 
        image=Label(self.root, image=self.image).place(x=150,y=140,width=400,height=400)

        #======Email=======
        email=Label(frame1,text="Email", font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=340,y=150)
        self.input_email=Entry(frame1,font=("times new roman",18),bg="lightgray")
        self.input_email.place(x=340,y=180,width=360)


        password=Label(frame1,text="Password", font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=340,y=230)
        self.input_password=Entry(frame1,font=("times new roman",18),bg="lightgray")
        self.input_password.place(x=340,y=260,width=360)

        reg_btn=Button(frame1,text="Register New Account?",command=self.register_toggle,font=("times new roman",13),bd=0,cursor="hand2",bg="white",fg="#B00857").place(x=340,y=300)

        frgt_btn=Button(frame1,text="Forgot Password?",command=self.forgot_pswd_toggle,font=("times new roman",13),bd=0,cursor="hand2",bg="white",fg="#B00857").place(x=570,y=300)

        login_btn=Button(frame1,text="Login",font=("times new roman",20),command=self.login_user,bg="#B00857",fg="white",cursor="hand2").place(x=340,y=360,width=180, height=40)


    #========Registration Tab==========

    def register_toggle(self):
         self.root.destroy()
         import Register

    #=======Forgot Password======
    def forgot_pswd(self):
        if self.cmbo_question.get()=="Select" or self.input_answer.get()=="" or self.input_newPass.get()=="":
            messagebox.showerror("Error","All Fields are Required", parent=self.root2)

        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="student management system")
                cur=con.cursor()
                cur.execute("select * from users where email=%s and question=%s and answer=%s",(self.input_email.get(),self.cmbo_question.get(),self.input_answer.get()))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error", "Invalid Details", parent=self.root)

                else:
                    cur.execute("update users set password=%s where email=%s",(self.input_newPass.get(),self.input_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your Password has been Reset! Please Login Again.",parent=self.root2)
                    self.root2.destroy()

            except Exception as es:
                 messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)


    def forgot_pswd_toggle(self):
        if self.input_email.get()=="":
            messagebox.showerror("Error", "Please Enter a Valid Email", parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="student management system")
                cur=con.cursor()
                cur.execute("select * from users where email=%s",self.input_email.get())
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error", "Please Enter a Valid Email", parent=self.root)

                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Reset Password")
                    self.root2.geometry("400x400+450+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forgot Password", font=("times new roman",20,"bold"),bg="white",fg="#B00857").place(x=0,y=10,relwidth=1)

                    #========Security Question=========
                    question=Label(self.root2,text="Security Question", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
                    self.cmbo_question=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly')
                    self.cmbo_question['values']=("Select", "Your Pet Name", "Your Birth Place", "Your Favorite Food")
                    self.cmbo_question.place(x=50,y=130,width=250)
                    self.cmbo_question.current(0)

                    answer=Label(self.root2,text="Security Answer", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
                    self.input_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.input_answer.place(x=50,y=200,width=250)


                    newPass=Label(self.root2,text="New Password", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
                    self.input_newPass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.input_newPass.place(x=50,y=270,width=250)

                    resetPassBtn=Button(self.root2,text="Reset Password", command=self.forgot_pswd,bg="#B00857",fg="white",font=("times new roman",15,"bold")).place(x=50,y=320)
                    
               

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)


           




    def login_user(self):
        if self.input_email.get()=="" or self.input_password=="":
            messagebox.showerror("Error","All Fields are Required", parent=self.root)
        
        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="student management system")
                cur=con.cursor()
                cur.execute("select * from users where email=%s and password=%s",(self.input_email.get(),self.input_password.get()))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)

                else:
                    messagebox.showinfo("Success", "Login Successful! Welcome.", parent=self.root)
                    self.root.destroy()
                    import Student

                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)





root=Tk()
obj=Login(root)
root.mainloop()