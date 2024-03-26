from tkinter import *
from tkinter import messagebox

class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        
        #background Image
        self.bg = PhotoImage(file="images/349777791588.jpg")
        self.bg_image = Label(self.root, image=self.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)
    
        #Login frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=350, y=80, width=500, height=500)
        
        #Title&subtitle
        title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#40E0D0", bg="white")
        title.place(x=90, y=30)
        subtitle = Label(Frame_login, text="Members Login Area", font=("Goudy old style", 20, "bold"), fg="#1d1d1d", bg="white")
        subtitle.place(x=90, y=100)
        
        #username
        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 20, "bold"), fg="grey", bg="white")
        lbl_user.place(x=90, y=140)
        self.username = Entry(Frame_login,  font=("Goudy old style", 20, ),  bg="#E7E6E6")
        self.username.place(x=90, y=190, width=320, height=35)
        
        #password
        lbl_password = Label(Frame_login, text="Password", font=("Goudy old style", 20, "bold"), fg="grey", bg="white")
        lbl_password.place(x=90, y=230)
        self.password = Entry(Frame_login,  font=("Goudy old style", 20, ),  bg="#E7E6E6", show="*")
        self.password.place(x=90, y=280, width=340, height=35)
        
        #Button
        forget = Button(Frame_login, text="Forgot Password", bd=0,  font=("Goudy old style", 15, "bold"), fg="#6162FF", bg="white")
        forget.place(x=90, y=320)
        submit = Button(Frame_login, command=self.check_function, cursor="hand2", text="Login?", bd=0,  font=("Goudy old style", 17, "bold"), bg="#40E0D0", fg="white")
        submit.place(x=90, y=370, width=180, height=40)
    
    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root) 
        elif self.username.get() != "Clarice" or self.password.get() != "123456":
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root) 
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")

root = Tk()
obj = login(root)
root.mainloop()
