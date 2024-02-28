from tkinter import *
from tkinter import messagebox

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
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei Ui Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
####### end username
######............................password
passw = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei Ui Light',11))
passw.place(x=30,y=150)
passw.insert(0,'Password')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
####### end password

root.mainloop()