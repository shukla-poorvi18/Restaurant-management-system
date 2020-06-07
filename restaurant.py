import random
import time
import datetime
import tkinter.messagebox
from tkinter import*


root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant management system")
root.configure(background="White")

Tops = Frame(root,bg='Red',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)
lblTitle = Label(Tops,font=('aerial',60,'bold'),text="Restaurant Management System",bd=21,bg='pink',fg= 'Cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)


ReceiptCal_F = Frame(root,bg='Powder Blue',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F= Frame(ReceiptCal_F,bg='Powder Blue',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F= Frame(ReceiptCal_F,bg='Powder Blue',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F= Frame(ReceiptCal_F,bg='Powder Blue',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)



MenuFrame = Frame(root,bg='Cadet Blue',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F= Frame(MenuFrame,bg='Powder Blue',bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F= Frame(MenuFrame,bg='Cadet Blue',bd=10)
Drinks_F.pack(side=TOP)



Drinks_F= Frame(MenuFrame,bg='Powder Blue',bd=10,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F= Frame(MenuFrame,bg='Powder Blue',bd=10,relief=RIDGE)
Cake_F.pack(side=RIGHT)

#########################################################VARIABLE####################################################################
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

dateoforder=StringVar()
Receipt_Ref=StringVar()
paidtax=StringVar()
subtotal=StringVar()
totalcost=StringVar()
costofcake=StringVar()
costofdrink=StringVar()
servicecharge=StringVar()

text_Input=StringVar()
operator=""

E_latta=StringVar()
E_expresso=StringVar()
E_iced_latta=StringVar()
E_vale_coffee=StringVar()
E_cappuccino=StringVar()
E_african_coffee=StringVar()
E_american_coffee=StringVar()
E_iced_cappuccino=StringVar()

E_schoolcake=StringVar()
E_pineapple=StringVar()
E_darkforest=StringVar()
E_blackforest=StringVar()
E_pancake=StringVar()
E_redvelvet=StringVar()
E_sunny_o_cake=StringVar()
E_chocolava=StringVar()

E_latta.set("0")
E_expresso.set("0")
E_iced_latta.set("0")
E_vale_coffee.set("0")
E_cappuccino.set("0")
E_african_coffee.set("0")
E_american_coffee.set("0")
E_iced_cappuccino.set("0")

E_schoolcake.set("0")
E_pineapple.set("0")
E_darkforest.set("0")
E_blackforest.set("0")
E_pancake.set("0")
E_redvelvet.set("0")
E_sunny_o_cake.set("0")
E_chocolava.set("0")

dateoforder.set(time.strftime("#d/#m/#y"))


def iexit():
    iexit=tkinter.messagebox.askyesno("Exit Restaurant System","CONFIRM IF YOU WANT TO EXIT")
    if iexit >0:
        root.destroy()
        return

def reset():
    E_latta.set("0")
    E_expresso.set("0")
    E_iced_latta.set("0")
    E_vale_coffee.set("0")
    E_cappuccino.set("0")
    E_african_coffee.set("0")
    E_american_coffee.set("0")
    E_iced_cappuccino.set("0")

    E_schoolcake.set("0")
    E_pineapple.set("0")
    E_darkforest.set("0")
    E_blackforest.set("0")
    E_pancake.set("0")
    E_redvelvet.set("0")
    E_sunny_o_cake.set("0")
    E_chocolava.set("0")
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    
    txtReceipt.delete("1.0",END)
    paidtax.set("")
    subtotal.set("")
    totalcost.set("")
    costofcake.set("")
    costofdrink.set("")
    servicecharge.set("")

    txtLatta.configure(state=DISABLED)
    txtExpresso.configure(state=DISABLED)
    txtIced_latta.configure(state=DISABLED)
    txtVale_Coffee.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtAfrican_Coffee.configure(state=DISABLED)
    txtAmerican_Coffee.configure(state=DISABLED)
    txtIced_Cappuccino.configure(state=DISABLED)
    txtSchoolcake.configure(state=DISABLED)
    txtPineapple.configure(state=DISABLED)
    txtDarkforest.configure(state=DISABLED)
    txtBlackforest.configure(state=DISABLED)
    txtPancake.configure(state=DISABLED)
    txtRedvelvet.configure(state=DISABLED)
    txtSunny_o_Cake.configure(state=DISABLED)
    txtChocolava.configure(state=DISABLED)

def costofitem():
    item1=float(E_latta.get())
    item2=float(E_expresso.get())
    item3=float(E_iced_latta.get())
    item4=float(E_vale_coffee.get())
    item5=float(E_cappuccino.get())
    item6=float(E_african_coffee.get())
    item7=float(E_american_coffee.get())
    item8=float(E_iced_cappuccino.get())

    item9=float(E_schoolcake.get())
    item10=float(E_pineapple.get())
    item11=float(E_darkforest.get())
    item12=float(E_blackforest.get())
    item13=float(E_pancake.get())
    item14=float(E_redvelvet.get())
    item15=float(E_sunny_o_cake.get())
    item16=float(E_chocolava.get())

    priceofdrink=(item1*1.2)+(item2*1.99)+(item3*2.05)\
                  +(item4*1.89)+(item5*1.99)+(item6*2.99)+(item7*2.39)+(item8*1.29)
    priceofcake=(item9*1.35)+(item10*2.2)+(item11*1.99)\
                 +(item12*1.49)+(item13*1.8)+(item14*1.67)+(item15*1.6)+(item16*1.99)
    drinksprice="$",str('%.2f'%(priceofdrink))
    cakeprice="$",str('%.2f'%(priceofcake))
    costofcake.set(cakeprice)
    costofdrink.set(drinksprice)
    sc="$",str('%.2f'%(1.59))
    servicecharge.set(sc)
    subtotalofitem="$",str('%.2f'%(priceofdrink+priceofcake+1.59))
    subtotal.set(subtotalofitem)
    tax='$',str('%.2f'%((priceofdrink+priceofcake+1.59)*0.15))
    paidtax.set(tax)
    tt=((priceofdrink+priceofcake+1.59)*0.15)
    tc="$",str('%.2f'%(priceofdrink+priceofcake+1.59+tt))
    totalcost.set(tc)

def chklatta():
    if(var1.get()==1):
        txtLatta.configure(state=NORMAL)
        txtLatta.focus()
        txtLatta.delete('0',END)
        E_latta.set("")
    elif(var1.get()==0):
        txtLatta.configure(state=DISABLED)
        E_latta.set("0")
def chkexpresso():
    if(var2.get()==1):
        txtExpresso.configure(state=NORMAL)
        txtExpresso.focus()
        txtExpresso.delete('0',END)
        E_expresso.set("")
    elif(var2.get()==0):
        txtExpresso.configure(state=DISABLED)
        E_expresso.set("0")
def chkicedlatta():
    if(var3.get()==1):
        txtIced_Latta.configure(state=NORMAL)
        txtIced_Latta.focus()
        txtIced_Latta.delete('0',END)
        E_icedlatta.set("")
    elif(var3.get()==0):
        txtIced_Latta.configure(state=DISABLED)
        E_icedlatta.set("0")
       
def chkvalecoffee():
    if(var4.get()==1):
        txtVale_Coffee.configure(state=NORMAL)
        txtVale_Coffee.focus()
        txtVale_Coffee.delete('0',END)
        E_vale_coffee.set("")
    elif(var4.get()==0):
        txtVale_Coffee.configure(state=DISABLED)
        E_Vale_coffee.set("0")
        
def chkcappuccino():
    if(var5.get()==1):
        txtCappuccino.configure(state=NORMAL)
        txtCappuccino.focus()
        txtCappuccino.delete('0',END)
        E_cappuccino.set("")
    elif(var5.get()==0):
        txtCappuccino.configure(state=DISABLED)
        E_cappuccino.set("0")
def chkafricancoffee():
    if(var6.get()==1):
        txtAfrican_Coffee.configure(state=NORMAL)
        txtAfrican_Coffee.focus()
        txtAfrican_Coffee.delete('0',END)
        E_africancoffee.set("")
    elif(var6.get()==0):
        txtAfrican_Coffee.configure(state=DISABLED)
        E_africancoffee.set("0")
def chkamericancoffee():
    if(var7.get()==1):
        txtAmerican_Coffee.configure(state=NORMAL)
        txtAmerican_Coffee.focus()
        txtAmerican_Coffee.delete('0',END)
        E_americancoffee.set("")
    elif(var7.get()==0):
        txtAmerican_Coffee.configure(state=DISABLED)
        E_americancoffee.set("0")
def chkicedcappuccino():
    if(var8.get()==1):
        txtIced_Cappuccino.configure(state=NORMAL)
        txtIced_Cappuccino.focus()
        txtIced_Cappuccino.delete('0',END)
        E_icedcappuccino.set("")
    elif(var8.get()==0):
        txtIced_Cappuccino.configure(state=DISABLED)
        E_icedcappuccino.set("0")
def chkschoolcake():
    if(var9.get()==1):
        txtSchoolcake.configure(state=NORMAL)
        txtSchoolcake.focus()
        txtSchoolcake.delete('0',END)
        E_schoolcake.set("")
    elif(var9.get()==0):
        txtSchoolcake.configure(state=DISABLED)
        E_schoolcake.set("0")
def chkpineapple():
    if(var10.get()==1):
        txtPineapple.configure(state=NORMAL)
        txtPineapple.focus()
        txtPineapple.delete('0',END)
        E_pineapple.set("")
    elif(var10.get()==0):
        txtPineapple.configure(state=DISABLED)
        E_pineapple.set("0")
def chkdarkforest():
    if(var11.get()==1):
        txtDarkforest.configure(state=NORMAL)
        txtDarkforest.focus()
        txtDarkforest.delete('0',END)
        E_darkforest.set("")
    elif(var11.get()==0):
        txtDarkforest.configure(state=DISABLED)
        E_darkforest.set("0")
def chkblackforest():
    if(var12.get()==1):
        txtBlackforest.configure(state=NORMAL)
        txtBlackforest.focus()
        txtBlackforest.delete('0',END)
        E_blackforest.set("")
    elif(var12.get()==0):
        txtBlackforest.configure(state=DISABLED)
        E_blackforest.set("0")
def chkpancake():
    if(var13.get()==1):
        txtPancake.configure(state=NORMAL)
        txtPancake.focus()
        txtPancake.delete('0',END)
        E_pancake.set("")
    elif(var13.get()==0):
        txtPancake.configure(state=DISABLED)
        E_pancake.set("0")
def chkredvelvet():
    if(var14.get()==1):
        txtRedvelvet.configure(state=NORMAL)
        txtRedvelvet.focus()
        txtRedvelvet.delete('0',END)
        E_redvelvet.set("")
    elif(var14.get()==0):
        txtRedvelvet.configure(state=DISABLED)
        E_redvelvet.set("0")
def chksunnyocake():
    if(var15.get()==1):
        txtSunny_o_Cake.configure(state=NORMAL)
        txtSunny_o_Cake.focus()
        txtSunny_o_Cake.delete('0',END)
        E_sunnyocake.set("")
    elif(var15.get()==0):
        txtSunny_o_Cake.configure(state=DISABLED)
        E_sunnyocake.set("0")
def chkchocolava():
    if(var16.get()==1):
        txtChocolave.configure(state=NORMAL)
        txtChocolave.focus()
        txtChocolave.delete('0',END)
        E_chocolava.set("")
    elif(var16.get()==0):
        txtChocolave.configure(state=DISABLED)
        E_chocolava.set("0")

def receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10903,609235)
    randomRef=str(x)
    Receipt_Ref.set("BILL"+randomRef)

    txtReceipt.insert(END,"Receipt Ref:\t\t\t"+Receipt_Ref.get()+"\t"+dateoforder.get()+"\n")
    txtReceipt.insert(END,"Item:\t\t\t"+"cost of item\n")
    txtReceipt.insert(END,"Latta:\t\t\t\t\t"+E_latta.get()+"\n")
    txtReceipt.insert(END,"Expresso:\t\t\t\t\t"+E_expresso.get()+"\n")
    txtReceipt.insert(END,"Vale_coffee:\t\t\t\t\t"+E_vale_coffee.get()+"\n")
    txtReceipt.insert(END,"Iced_Latta:\t\t\t\t\t"+E_iced_latta.get()+"\n")
    txtReceipt.insert(END,"Cappuccino:\t\t\t\t\t"+E_cappuccino.get()+"\n")
    txtReceipt.insert(END,"African_Coffee:\t\t\t\t\t"+E_african_coffee.get()+"\n")
    txtReceipt.insert(END,"American_Coffee:\t\t\t\t\t"+E_american_coffee.get()+"\n")
    txtReceipt.insert(END,"Iced_Cappuccino:\t\t\t\t\t"+E_iced_cappuccino.get()+"\n")
    txtReceipt.insert(END,"Schoolcake:\t\t\t\t\t"+E_schoolcake.get()+"\n")
    txtReceipt.insert(END,"Pineapple:\t\t\t\t\t"+E_pineapple.get()+"\n")
    txtReceipt.insert(END,"Darkforest:\t\t\t\t\t"+E_darkforest.get()+"\n")
    txtReceipt.insert(END,"Blackforest:\t\t\t\t\t"+E_blackforest.get()+"\n")
    txtReceipt.insert(END,"Pancake:\t\t\t\t\t"+E_pancake.get()+"\n")
    txtReceipt.insert(END,"Redvelvet:\t\t\t\t\t"+E_redvelvet.get()+"\n")
    txtReceipt.insert(END,"Sunny_o_cake:\t\t\t\t\t"+E_sunny_o_cake.get()+"\n")
    txtReceipt.insert(END,"chocolava:\t\t\t\t\t"+E_chocolave.get()+"\n")
    txtReceipt.insert(END,"Costofdrinks:\t\t\t\t\t"+E_costofdrink.get().get()+"\n paid tax:\t\t\t\t" +paidtax.get()+"\n")
    txtReceipt.insert(END,"Costofcake:\t\t\t\t\t"+E_costofcake.get()+"\n sub total:\t\t\t\t" + str(subtotal.get())+"\n")
    txtReceipt.insert(END,"Servicecharge:\t\t\t\t\t"+E_servicecharge.get()+'\n Total Cost:\t\t\t\t' + str(totalcost.get()))
    
###################################################DRINKS#################################################################################
                      
Latta =  Checkbutton(Drinks_F,text="Latta",variable=var1,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chklatta).grid(row=0,sticky=W)

Expresso=Checkbutton(Drinks_F,text="Expresso",variable=var2,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkexpresso).grid(row=1,sticky=W)

Iced_Latta=Checkbutton(Drinks_F,text="Iced_Latta",variable=var3,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkicedlatta).grid(row=2,sticky=W)

Vale_Coffee=Checkbutton(Drinks_F,text="Vale_Coffee",variable=var4,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkvalecoffee).grid(row=3,sticky=W)

Cappuccino=Checkbutton(Drinks_F,text="Cappuccino",variable=var5,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkcappuccino).grid(row=4,sticky=W)

African_Coffee=Checkbutton(Drinks_F,text="African_Coffee",variable=var6,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkafricancoffee).grid(row=5,sticky=W)

American_Coffee=Checkbutton(Drinks_F,text="American_Coffee",variable=var7,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkamericancoffee).grid(row=6,sticky=W)

Iced_Cappuccino=Checkbutton(Drinks_F,text="Iced_Cappuccino",variable=var8,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkicedcappuccino).grid(row=7,sticky=W)


########################################ENTRY BOX FOR DRINKS####################################################################################

txtLatta=Entry(Drinks_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,
               textvariable=E_latta)
txtLatta.grid(row=0,column=1)
txtExpresso=Entry(Drinks_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED ,textvariable=E_expresso)
txtExpresso.grid(row=1,column=1)
txtIced_Latta=Entry(Drinks_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED ,textvariable=E_iced_latta)
txtIced_Latta.grid(row=2,column=1)

txtVale_Coffee=Entry(Drinks_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_vale_coffee)
txtVale_Coffee.grid(row=3,column=1)
txtCappuccino=Entry(Drinks_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_cappuccino)
txtCappuccino.grid(row=4,column=1)
txtAfrican_Coffee=Entry(Drinks_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED ,textvariable=E_african_coffee)
txtAfrican_Coffee.grid(row=5,column=1)
txtAmerican_Coffee=Entry(Drinks_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED ,textvariable=E_american_coffee)
txtAmerican_Coffee.grid(row=6,column=1)

txtIced_Cappuccino=Entry(Drinks_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED ,textvariable=E_iced_cappuccino)
txtIced_Cappuccino.grid(row=7,column=1)

###############################################CAKES############################################################################################

Schoolcake=Checkbutton(Cake_F,text="Schoolcake",variable=var9,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkschoolcake).grid(row=0,sticky=W)

Pineapple=Checkbutton(Cake_F,text="Pineapple",variable=var10,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkpineapple).grid(row=1,sticky=W)

Darkforest=Checkbutton(Cake_F,text="Darkforest",variable=var11,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkdarkforest).grid(row=2,sticky=W)

Blackforest=Checkbutton(Cake_F,text="Blackforest",variable=var12,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkblackforest).grid(row=3,sticky=W)

Pancake=Checkbutton(Cake_F,text="Pancake",variable=var13,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkpancake).grid(row=4,sticky=W)

Redvelvet=Checkbutton(Cake_F,text="Redvelvet",variable=var14,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkredvelvet).grid(row=5,sticky=W)

Sunny_o_Cake=Checkbutton(Cake_F,text="Sunny_o_Cake",variable=var15,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chksunnyocake).grid(row=6,sticky=W)

Chocolave=Checkbutton(Cake_F,text="Chocolava",variable=var16,onvalue=1,offvalue=0,font=('aerial',18,'bold'),bg='Powder Blue',command=chkchocolava).grid(row=7,sticky=W)

######################################################ENTRY BOX FOR CAKE############################################################################

txtSchoolcake=Entry(Cake_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,
                    textvariable=E_schoolcake)
txtSchoolcake.grid(row=0,column=1)
txtPineapple=Entry(Cake_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED ,textvariable=E_pineapple)
txtPineapple.grid(row=1,column=1)
txtDarkforest=Entry(Cake_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_darkforest)
txtDarkforest.grid(row=2,column=1)

txtBlackforest=Entry(Cake_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED ,textvariable=E_blackforest)
txtBlackforest.grid(row=3,column=1)
txtPancake=Entry(Cake_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED ,textvariable=E_pancake)
txtPancake.grid(row=4,column=1)
txtRedvelvet=Entry(Cake_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_redvelvet)
txtRedvelvet.grid(row=5,column=1)
txtSunny_o_Cake=Entry(Cake_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_sunny_o_cake)
txtSunny_o_Cake.grid(row=6,column=1)

txtChocolave=Entry(Cake_F,font=('aerial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_chocolava)
txtChocolave.grid(row=7,column=1)

###################################################################TOTAL COST#########################################################################
lblcostofdrinks = Label(Cost_F,font=('aerial',14,'bold'),text="Cost of drink",bg='green',fg= 'black')
lblcostofdrinks.grid(row=0,column=0,sticky=W)
txtcostofdrinks=Entry(Cost_F,font=('aerial',14,'bold'),bd=7,bg='white',insertwidth=2,justify=RIGHT ,textvariable=costofdrink)
txtcostofdrinks.grid(row=0,column=1)
lblcostofcake = Label(Cost_F,font=('aerial',14,'bold'),text="Cost of cake",bg='green',fg= 'black')
lblcostofcake.grid(row=1,column=0,sticky=W)
txtcostofcake=Entry(Cost_F,font=('aerial',14,'bold'),bd=7,bg='white',insertwidth=2,justify=RIGHT,textvariable=costofcake)
txtcostofcake.grid(row=1,column=1)

lblservicecharge = Label(Cost_F,font=('aerial',14,'bold'),text="Service Charges",bg='green',fg= 'black')
lblservicecharge.grid(row=2,column=0,sticky=W)
txtservicecharge=Entry(Cost_F,font=('aerial',14,'bold'),bd=7,bg='white',insertwidth=2,justify=RIGHT ,textvariable=servicecharge)
txtservicecharge.grid(row=2,column=1)

###############################################################PAYMENT INFORMATION###################################################################

lblpaidtax = Label(Cost_F,font=('aerial',14,'bold'),text="Paid Tax",bg='green',fg= 'black')
lblpaidtax.grid(row=0,column=2,sticky=W)
txtpaidtax=Entry(Cost_F,font=('aerial',14,'bold'),bd=7,bg='white',insertwidth=2,justify=RIGHT,textvariable=paidtax)
txtpaidtax.grid(row=0,column=3)
lblsubtotal = Label(Cost_F,font=('aerial',14,'bold'),text="Subtotal",bg='green',fg= 'black')
lblsubtotal.grid(row=1,column=2,sticky=W)
txtsubtotal=Entry(Cost_F,font=('aerial',14,'bold'),bd=7,bg='white',insertwidth=2,justify=RIGHT ,textvariable=subtotal)
txtsubtotal.grid(row=1,column=3)

lbltotalcost = Label(Cost_F,font=('aerial',14,'bold'),text="Total Cost",bg='green',fg= 'black')
lbltotalcost.grid(row=2,column=2,sticky=W)
txttotalcost=Entry(Cost_F,font=('aerial',14,'bold'),bd=7,bg='white',insertwidth=2,justify=RIGHT ,textvariable=totalcost)
txttotalcost.grid(row=2,column=3)



##########################################################RECEIPT######################################################################################
txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('aerial',12,'bold'))
txtReceipt.grid(row=0,column=0)


##########################################################BUTTON###################################################################

btnTotal= Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='total',bg='powder blue',command=costofitem).grid(row=0,column=0)
btnReceipt= Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='Receipt',bg='powder blue',command=receipt).grid(row=0,column=1)
btnReset= Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='Reset',bg='powder blue',command=reset).grid(row=0,column=2)
btnExit= Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='Exit',bg='powder blue',command=iexit).grid(row=0,column=3)

#################################################################CALCULATOR#######################################################################
def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnclear():
    global operator
    operator = ""
    text_Input.set("")

def btnequals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator = ""


txtdisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('aerial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtdisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtdisplay.insert(0,"0")

##########################################################CALCULATOR BUTTON###################################################################

btn7= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='7',bg='powder blue',command=lambda:btnclick(7)).grid(row=2,column=0)
btn8= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='8',bg='powder blue',command=lambda:btnclick(8)).grid(row=2,column=1)
btn9= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='9',bg='powder blue',command=lambda:btnclick(9)).grid(row=2,column=2)
btnadd= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='+',bg='powder blue',command=lambda:btnclick("+")).grid(row=2,column=3)

##########################################################CALCULATOR BUTTON###################################################################

btn4= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='4',bg='powder blue',command=lambda:btnclick(4)).grid(row=3,column=0)
btn5= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='5',bg='powder blue',command=lambda:btnclick(5)).grid(row=3,column=1)
btn6= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='6',bg='powder blue',command=lambda:btnclick(6)).grid(row=3,column=2)
btnsub= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='-',bg='powder blue',command=lambda:btnclick("-")).grid(row=3,column=3)

##########################################################CALCULATOR BUTTON###################################################################

btn3= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='3',bg='powder blue',command=lambda:btnclick(3)).grid(row=4,column=0)
btn2= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='2',bg='powder blue',command=lambda:btnclick(2)).grid(row=4,column=1)
btn1= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='1',bg='powder blue',command=lambda:btnclick(1)).grid(row=4,column=2)
btnmulti= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='*',bg='powder blue',command=lambda:btnclick("*")).grid(row=4,column=3)
##########################################################CALCULATOR BUTTON###################################################################

btn0= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='0',bg='powder blue',command=lambda:btnclick(0)).grid(row=5,column=0)
btnclear= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='C',bg='powder blue',command=btnclear).grid(row=5,column=1)
btnequals= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='=',bg='powder blue',command=btnequals).grid(row=5,column=2)
btndiv= Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='/',bg='powder blue',command=lambda:btnclick("/")).grid(row=5,column=3)
root.mainloop()


