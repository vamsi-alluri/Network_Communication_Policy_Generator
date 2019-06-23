import sys
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
import csv
import re
import socket




nGui= Tk()

def mhello():
    myload=filedialog.askopenfile()
    inputbox.config(state='normal')
    inputbox1.config(state='normal')
    inputbox2.config(state='normal')
    inputbox3.config(state='normal')
    inputbox4.config(state='normal')
    inputbox5.config(state='normal')
    inputbox6.config(state='normal')
    inputbox7.config(state='normal')
    inputbox8.config(state='normal')
    inputbox9.config(state='normal')
    inputbox10.config(state='normal')
    inputbox2.config(highlightthickness=0)
    inputbox3.config(highlightthickness=0)
    inputbox4.config(highlightthickness=0)
    inputbox5.config(highlightthickness=0)
    inputbox10.config(highlightthickness=0)
    inputbox9.config(highlightthickness=0)
    inputbox.delete(0,END)
    inputbox1.delete(0,END)
    inputbox2.delete(0,END)
    inputbox3.delete(0,END)
    inputbox4.delete(0,END)
    inputbox5.delete(0,END)
    inputbox6.delete(0,END)
    inputbox7.delete(0,END)
    inputbox8.delete(0,END)
    inputbox9.delete(0,END)
    inputbox10.delete(0,END)
    filepath=myload.name
    inputbox9.delete(0,END)
    inputbox9.insert(0,filepath)
    f1=0
    f2=0
    f3=0
    f4=0
    try:
        with open(filepath) as f:
            read= csv.reader(f, delimiter = ',')
            next(read)        

            for row in read:
                
                inputbox.insert(0,row[0])
                inputbox.config(state='disable')
                inputbox1.insert(0,row[1])
                inputbox1.config(state='disable')
                inputbox2.insert(0,row[3])
                if(ipFormatChk(row[3])==False):
                     inputbox2.config(highlightthickness=3,highlightbackground='red',state='disable')
                     f1=1
                else:
                   {inputbox2.config(state='disable')}
                inputbox3.insert(0,row[6])
                if(ipFormatChk(row[6])==False):
                     inputbox3.config(highlightthickness=3,highlightbackground='red',state='disable')
                     f2=1
                else:
                   {inputbox3.config(state='disable')}
                inputbox4.insert(0,row[2])
                if(macFormatChk(row[2])==False):
                     inputbox4.config(highlightthickness=3,highlightbackground='red',state='disable')
                     f3=1
                else:
                   {inputbox4.config(state='disable')}
                inputbox5.insert(0,row[5])
                if(macFormatChk(row[5])==False):
                     inputbox5.config(highlightthickness=3,highlightbackground='red',state='disable')
                     f4=1
                else:
                   {inputbox5.config(state='disable')}
                inputbox6.insert(0,row[4])
                inputbox6.config(state='disable')
                inputbox7.insert(0,row[7])
                inputbox7.config(state='disable')
                inputbox8.insert(0,row[8])
                inputbox8.config(state='disable')
                
                if (row[9]=='1')and(f1==0)and(f2==0)and(f3==0)and(f4==0):
                    
                    
                     inputbox10.insert(0,"ALLOWED BECAUSE CONNECTION HAS GOOD PACKETS")
                     inputbox10.config(highlightthickness=3,highlightbackground='GREEN',fg='red',state='disable')
                     inputbox9.config(state='disable')
                else:
                    
                     inputbox10.insert(0,"BLOCKED may be because of bad packets or errors above")
                     inputbox10.config(highlightthickness=3,highlightbackground='red',fg='red',state='disable')
                     inputbox9.config(state='disable')
                        
    except:
    
        inputbox10.delete(0,END)
        inputbox10.insert(0,"FILE PATH SHOULD BE .CSV  OR FILE PATH INCORRECT")
        inputbox10.config(highlightthickness=3,highlightbackground='red',fg='red',state='disable')
        inputbox9.config(highlightthickness=3,highlightbackground='red',fg='red',state='disable')
        inputbox.config(state='disable')
        inputbox1.config(state='disable')
        inputbox2.config(state='disable')
        inputbox3.config(state='disable')
        inputbox4.config(state='disable')
        inputbox5.config(state='disable')
        inputbox6.config(state='disable')
        inputbox7.config(state='disable')
        inputbox8.config(state='disable')
        
        
            
                
    
def mNew():
    messagebox.showinfo(title="new",message="you have pressed new" )
    inputbox.config(state='normal')
    inputbox1.config(state='normal')
    inputbox2.config(state='normal')
    inputbox3.config(state='normal')
    inputbox4.config(state='normal')
    inputbox5.config(state='normal')
    inputbox6.config(state='normal')
    inputbox7.config(state='normal')
    inputbox8.config(state='normal')
    inputbox9.config(state='normal')
    inputbox10.config(state='normal')
    inputbox2.config(highlightthickness=0)
    inputbox3.config(highlightthickness=0)
    inputbox4.config(highlightthickness=0)
    inputbox5.config(highlightthickness=0)
    inputbox10.config(highlightthickness=0)
    inputbox9.config(highlightthickness=0)
    inputbox.delete(0,END)
    inputbox1.delete(0,END)
    inputbox2.delete(0,END)
    inputbox3.delete(0,END)
    inputbox4.delete(0,END)
    inputbox5.delete(0,END)
    inputbox6.delete(0,END)
    inputbox7.delete(0,END)
    inputbox8.delete(0,END)
    inputbox9.delete(0,END)
    inputbox10.delete(0,END)
    return
def mquit():
    nexit=messagebox.askyesno(title="Quit",message="Are you sure to Quit")
    if nexit >0:
        nGui.destroy();
    return

def mopen():
    myload=filedialog.askopenfile()
    filepath=myload.name
    inputbox9.delete(0,END)
    inputbox9.insert(0,filepath)
def mhelp():
     messagebox.showinfo(title="HELP",message="CLICK <\"CHECK CONNECTIONS\" >BUTTON AND LOAD THE CSV FILE TO CHECK NETWORK COMMUNICATION POLICY GENERATION ....!" )
def about():
    messagebox.showinfo(title="ABOUT",message="SOFTWARE WAS MADE BY KISHORE & MADHAV" )
    
def macFormatChk(addr):
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    if re.match(pattern,addr):
      return True
    else:
      return False

def ipFormatChk(ip_str):            
        try:
            socket.inet_aton(ip_str)
            return True       
        
        except socket.error:
            return False
#creating window
nGui.geometry('600x280+200+300')

#sizexsize+windowpositon+windowposition
#title
nGui.title('Network Communication Policy Generation')


mp=StringVar()   

#label
mlabel = Label(text='DATE',fg='blue',bg='white').place(x=10,y=10)
mlabel2 = Label(text='TIME',fg='blue',bg='white').place(x=300,y=10)
mlabel3 = Label(text='SOURCE IP ',fg='blue',bg='white').place(x=10,y=40)
mlabel4= Label(text='DESTINATION IP',fg='blue',bg='white').place(x=300,y=40)
mlabel5 = Label(text='SOURCE MAC',fg='blue',bg='white').place(x=10,y=70)
mlabel6 = Label(text='DESTINATION MAC',fg='blue',bg='white').place(x=300,y=70)
mlabel7 = Label(text='SOURCE PORT',fg='blue',bg='white').place(x=10,y=100)
mlabel8= Label(text='DESTINATION PORT',fg='blue',bg='white').place(x=300,y=100)
mlabel9= Label(text='PROTOCOL',fg='blue',bg='white').place(x=10,y=130)
mlabel10= Label(text='FILE PATH',fg='blue',bg='white').place(x=10,y=160)
mlabel10= Label(text='CONNECTION STATUS',fg='blue',bg='white').place(x=10,y=190)
#button
 
mbutton= Button(text='              CHECK CONNECTION                ',command=mhello,fg='black',bg='white').place(x=380,y=130)
mbutton= Button(text='    PREVIOUS        ',command=mhello,fg='white',bg='grey').place(x=280,y=130)
mbutton= Button(text='    NEXT            ',command=mhello,fg='white',bg='grey').place(x=590,y=130)
#textbox
inputbox = Entry()
inputbox.place(x=130,y=10)
inputbox1 = Entry()
inputbox1.place(x=430,y=10)
inputbox2 = Entry()
inputbox2.place(x=130,y=40)
inputbox3 = Entry()
inputbox3.place(x=430,y=40)
inputbox4 = Entry()
inputbox4.place(x=130,y=70)
inputbox5 = Entry()
inputbox5.place(x=430,y=70)
inputbox6 = Entry()
inputbox6.place(x=130,y=100)
inputbox7 = Entry()
inputbox7.place(x=430,y=100)
inputbox8 = Entry()
inputbox8.place(x=130,y=130)
inputbox9= Entry(width=70)
inputbox9.place(x=170,y=160)
inputbox10= Entry(width=70)
inputbox10.place(x=170,y=190)





menubar=Menu(nGui)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=mNew)
filemenu.add_command(label="Check Connection",command=mhello)
filemenu.add_command(label="Close",command=mquit)
menubar.add_cascade(label="File",menu=filemenu)


helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Help Docs",command=mhelp)
helpmenu.add_command(label="About",command=about)
menubar.add_cascade(label="Help",menu=helpmenu)
nGui.config (menu=menubar)

nGui.mainloop()
