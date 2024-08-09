from tkinter import *
root=Tk()
root.title("Simple Calculator")
#ابعاد النافذة
root.geometry("300x400")
#لمنع تكبير - تصغير النافذة
root.resizable(0,0)
#لتغيير لون الخلفية إلى اللون البيج
root.configure(bg="beige")
#لعمل شاشة إدخال بأعلى الشاشة
e=Entry(root, bd=10,width=30,font="Tohama",bg="LightGrey")
#لجعل البوكس يظهر بأعلى النافذة
e.pack()
#انشاء دوال الأزرار
# وضعت 32 كـ index
# لكى يعيد وضع 0 بالترتيب الصحيح
def click(number):
    e.insert(32,number)
def addition():
    e.insert(32,"+")
def subtract():
    e.insert(32,"-")
# لعمل زر الـ clear
def clear():
    e.delete(0,END)
# لعمل زى الـ equal
def equal():
    '''current1=e.get()
    list=current1.split("+")
    result=int(list[0])+int(list[1])
    clear()
    e.insert(32,result)
    def equal():'''
    try:
        current1 = e.get()
        result = eval(current1)
        clear()
        e.insert(END, result)
    except Exception:
        clear()
        e.insert(END, "Error")

#لانشاء الأزرار
button1=Button(root,text="7",font="Tohama",bg="gray",bd=10,padx=10, pady=5,command=lambda:click(7))
button1.place(x=10,y=60)
button2=Button(root,text="8",font="Tohama",bg="gray",bd=10,padx=10, pady=5,command=lambda:click(8))
button2.place(x=85,y=60)
button3=Button(root,text="9",font="Tohama",bg="gray",bd=10,padx=10, pady=5,command=lambda:click(9))
button3.place(x=160,y=60)
button4=Button(root,text="4",font="Tohama",bg="gray",bd=10,padx=10, pady=5,command=lambda:click(4))
button4.place(x=10,y=145)
button5=Button(root,text="5",font="Tohama",bg="gray",bd=10,padx=10, pady=5,command=lambda:click(5))
button5.place(x=85,y=145)
button6=Button(root,text="6",font="Tohama",bg="gray",bd=10,padx=10, pady=5,command=lambda:click(6))
button6.place(x=160,y=145)
button7=Button(root,text="1",font="Tohama",bg="gray",bd=10,padx=10, pady=5,command=lambda:click(1))
button7.place(x=10,y=230)
button8=Button(root,text="2",font="Tohama",bg="gray",bd=10,padx=10, pady=5,command=lambda:click(2))
button8.place(x=85,y=230)
button9=Button(root,text="3",font="Tohama",bg="gray",bd=10,padx=10, pady=5,command=lambda:click(3))
button9.place(x=160,y=230)
button10=Button(root,text="0",font="Tohama",bg="gray",bd=10,padx=10, pady=5,command=lambda:click(0))
button10.place(x=10,y=320)
button11=Button(root,text="+",font="Tohama",height=4,bg="skyblue",bd=10,command=addition)
button11.place(x=235,y=60)
button11=Button(root,text="-",font="Tohama",height=2,bg="skyblue",bd=5,command=subtract)
button11.place(x=235,y=320)
button12=Button(root,text="C",font="Tohama",width=8,height=1,bg="crimson",bd=10,command=clear)
button12.place(x=85,y=320)
button13=Button(root,text="=",font="Tohama",height=3,bd=10,bg="khaki",command=equal)
button13.place(x=235,y=230)

#لجعل الشاشة تستمر حتى نهاية العملية
root.mainloop()
