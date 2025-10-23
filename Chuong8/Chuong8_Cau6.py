from tkinter import*

from Chuong8.Chuong8_Cau2 import tiepAction

def GiaiPTB1():
    a= float (stringA.get())
    b= float (stringA.get())
    if a==0 and b==0:
        stringKQ.set("Vô số nghiệm")
    elif a==0 and b!=0:
        stringKQ.set("Vô nghiệm")
    else:
        stringKQ.set("x="+str((-b/a)))
def TiepPTB1():
    stringA.set("")
    stringB.set("")
    stringKQ.set("")




PTB1= Tk()
stringA= StringVar()
stringB= StringVar()
stringKQ= StringVar()
PTB1.title("PTB1")
PTB1.minsize(height=300,width=450)
PTB1.resizable(True,True)


Label(PTB1,text="Phương Trình Bậc 1",fg="red",font=("tohama",16),justify=CENTER).grid(row=0,columnspan=2)

Label(PTB1,text="Hệ số a:").grid(row=1,column=0)
Entry(PTB1,width=30,textvariable=stringA).grid(row=1,column=1)
Label(PTB1,text="Hệ số b:").grid(row=2,column=0)
Entry(PTB1,width=30,textvariable=stringB).grid(row=2,column=1)
frameButton=Frame()
Button(frameButton,text="Giải",command=GiaiPTB1).pack(side=LEFT)
Button(frameButton,text="Tiếp",command=tiepAction).pack(side=LEFT)
Button(frameButton,text="Thoát",command=PTB1.quit).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)
Label(PTB1,text="Kết quả:").grid(row=4,column=0)
Entry(PTB1,width=30,textvariable=stringKQ).grid(row=4,column=1)

PTB1.mainloop()