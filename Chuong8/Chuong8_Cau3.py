from tkinter import *
root=Tk()
stringA=StringVar()
stringB=StringVar()

stringKQ=StringVar()

root.minsize(height=150,width=200)
Label(root,text="Cộng Trừ Nhân Chia",fg="blue",font=("tahoma",16)).grid(row=0,columnspan=3)
frameButton=Frame(root)
Button(frameButton,text="Cộng").pack(side=TOP)
Button(frameButton,text="Trừ").pack(side=TOP,fill=X)
Button(frameButton,text="Nhân").pack(side=TOP)
Button(frameButton,text="Chia",).pack(side=TOP,fill= X)
frameButton.grid(row=1,column=0,rowspan=4)
Label(root,text="số a:").grid(row=1,column=1)
Entry(root,width=15,textvariable=stringA).grid(row=1,column=2)

Label(root,text="số b:").grid(row=2,column=1)
Entry(root,width=15,textvariable=stringB).grid(row=2,column=2)
Label(root,text="Kết quả:").grid(row=3,column=1)
Entry(root,width=15,textvariable=stringKQ).grid(row=3,column=2)
Button(root,text="Thoát",command=root.quit).grid(row=4,column=2)
root.mainloop()