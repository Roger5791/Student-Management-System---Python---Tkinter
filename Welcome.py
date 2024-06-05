from tkinter import *
from PIL import Image, ImageTk



class Welcome:
    def __init__(self, root):
        self.root=root
        self.root.title("Welcome")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #=====Background========
        bgRight=Label(self.root, bg="#021e2f").place(width=1350,relheight=1)
        bgLeft=Label(self.root, bg="#08A3D2").place(width=480, relheight=1)

      


        #=======Register Frame======
        welcomeFrame=Frame(self.root,bg="white")
        welcomeFrame.place(x=300,y=70,width=800,height=550)

        title=Label(welcomeFrame,text="Welcome", font=("times new roman",30,"bold","underline"),bg="white",fg="#021e2f").place(x=310,y=30)

        login_btn=Button(welcomeFrame,text="Login",font=("times new roman",20),command=self.go_to_login,bg="#B00857",fg="white",cursor="hand2").place(x=130,y=360,width=180, height=40)

        reg_btn=Button(welcomeFrame,text="Register",font=("times new roman",20),command=self.go_to_register,bg="#B00857",fg="white",cursor="hand2").place(x=460,y=360,width=180, height=40)

          #=====Login Image========

        self.loginImg = Image.open('images/login (1).png')
        resized = self.loginImg.resize((200, 200),Image.Resampling.LANCZOS)
        self.lImage = ImageTk.PhotoImage(resized) 
        lImage=Label(self.root, image=self.lImage).place(x=430,y=200,width=200,height=200)

        self.original = Image.open('images/login.png')
        resized = self.original.resize((200, 200),Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(resized) 
        image=Label(self.root, image=self.image).place(x=750,y=200,width=200,height=200)


    def go_to_login(self):
        self.root.destroy()
        import Login

    def go_to_register(self):
        self.root.destroy()
        import Register



root=Tk()
obj=Welcome(root)
root.mainloop()