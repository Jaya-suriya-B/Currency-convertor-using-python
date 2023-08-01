from tkinter import Tk,ttk
from tkinter import *


A = Tk()
A.title("Currency Convertor")
A.geometry('1000x300')
A.configure(background='white')

LeftMainFrame = Frame(A, width=660, height=400, bd=8)
LeftMainFrame.pack(side=LEFT)
RightMainFrame = Frame(A, width=200, height=400, bd=8)
RightMainFrame.pack(side=RIGHT)


value0 = StringVar()
convert = DoubleVar()
currency = DoubleVar()

def ConCurrency():
    if value0.get() == "British Pound":
        convert1= float(convert.get() * 0.0099)
        convert2= str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "United states Dollar":
        convert1= float(convert.get() * 0.014)
        convert2= str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "South Korean Won":
        convert1= float(convert.get() * 15.42)
        convert2= str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "Bangladeshi Taka":
        convert1= float(convert.get() * 1.16)
        convert2= str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "Canadian Dollar":
        convert1= float(convert.get() * 0.017)
        convert2= str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "Egyptian Pound":
        convert1= float(convert.get() * 0.21)
        convert2= str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "UAE Dirham":
        convert1= float(convert.get() * 0.050)
        convert2= str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "Yemeni Rial":
        convert1= float(convert.get() * 3.42)
        convert2= str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "Japanese Yen":
        convert1= float(convert.get() * 1.48)
        convert2= str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "Euro":
        convert1= float(convert.get() * 0.011)
        convert2= str('%.2f' %(convert1))
        currency.set(convert2)

def Reset():
    value0.set("")
    convert.set(" ")
    currency.set(" ")


EntCurrency= Entry(LeftMainFrame, font=('Times New Roman',20,'italic'), textvariable=convert, bd=2, width=28, justify='center')
EntCurrency.grid(row=0,column=1)

lblIndianRupee= Label(LeftMainFrame, font=('Times New Roman',20,'italic'), text='Indian Rupee', bd=2,fg="black", width=14)
lblIndianRupee.grid(row=0,column=2,sticky=W)

box= ttk.Combobox(LeftMainFrame, textvariable=value0, state='readonly', font=('arial',20,'bold'), width=20)
box['values']=(' ','British Pound', 'United states Dollar','South Korean Won', 'Bangladeshi Taka', 'Canadian Dollar','Egyptian Pound','UAE Dirham','Yemeni Rial','Japanese Yen', 'Euro')
box.current(0)
box.grid(row=4, column=2)

lblCurrency= Label(LeftMainFrame, font=('Times New Roman',20,'bold'), textvariable=currency, bd=2, width=25, bg='white', padx=2,pady=2, relief='sunken')
lblCurrency.grid(row=4,column=1)

btnConvert= Button(RightMainFrame, text='Convert', bd=2, fg="black", font=('arial',20,'bold'), width=12, height=1, command=ConCurrency).grid(row=1,column=0)
btnReset= Button(RightMainFrame, text='Reset', bd=2, fg="black", font=('arial',20,'bold'), width=12, height=1, command=Reset).grid(row=2,column=0)





A.mainloop()
