
import socket
from tkinter import *
def fanc1(event):
    try:
        host=str(in_1.get())
        port=int(in_2.get())
    except ValueError:
        resalt.insert(1.0,'not a valid input')
    scan = socket.socket()

    try:
        scan.connect((host, port))
    except socket.error:
        ress="Port -- ",port," -- [CLOSED]---HOST","  --",host
    else:
        ress=" Port -- ",port," -- [OPEN]---HOST","  --",host

    resalt.insert(1.0,ress)
#GUI
root=Tk()
root.title('scanner')
root.geometry("700x550")
instruction=Label(root,text='''this is a very simple scanner, enter the value in the fields and
the scan result will be at the bottom ''',font='bold')
lab_1=Label(root,text='input HOST')
in_1=Entry(root,width=20,bd=3) #input HOST!
lab_2=Label(root,text='input PORT')
in_2=Entry(root,width=20,bd=3) #input PORT!
button=Button(root,text='scan')
button.bind('<Button-1>',fanc1)
resalt=Text(root,width=53, height=20,wrap=WORD)
instruction.pack(side=TOP, padx=10,pady=10)
lab_1.pack()
in_1.pack()
lab_2.pack()
in_2.pack()
button.pack(side=TOP, padx=20,pady=10)
resalt.pack()
root.mainloop()
