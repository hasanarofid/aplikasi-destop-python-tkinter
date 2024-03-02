from tkinter import *
from tkinter import messagebox
from database import create_database, verify_login

def login():
    username = user.get()
    password = passw.get()

    if verify_login(username, password):
        messagebox.showinfo("Berhasil", "Selamat Datang")
        # Tambahkan kode untuk membuka layar beranda setelah login berhasil
    else:
        messagebox.showerror("Gagal", "Username atau password salah")

# Panggil fungsi create_database untuk membuat atau mengakses database
create_database()

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei Ui Light',23,'bold'))
heading.place(x=100,y=5)

######............................ username
def on_enter(e) :
    user.delete(0,'end')

def on_leave(e):
    name = user.get()
    if name=='' :
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei Ui Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
####### end username
######............................password
def on_enter(e) :
    passw.delete(0,'end')

def on_leave(e):
    passs = passw.get()
    if passs=='' :
        passw.insert(0,'Username')
passw = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei Ui Light',11))
passw.place(x=30,y=150)
passw.insert(0,'Password')
passw.bind('<FocusIn>',on_enter)
passw.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
####### end password

Button(frame, width=30, pady=7, text='Login', bg='#FF0000', fg='#57a1f8', border=0,command=login).place(x=35, y=204)

root.mainloop()