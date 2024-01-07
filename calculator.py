from tkinter import*
window=Tk()
window.geometry('400x400')
#Entry box
e=Entry(window,width=56,borderwidth=5)
e.place(x=15,y=10)
#Buttons

def click(num): # function
    result = e.get() # here e is object of entry,mentioned above
    e.delete(0,END) # to delete the first entered number
    e.insert(0,str(result)+str(num)) # 0 is pos. str(res.) is given to concatenate

b=Button(window,text='1',width='12',command=lambda:click(1))
b.place(x=50,y=60)

b=Button(window,text='2',width='12',command=lambda:click(2))
b.place(x=130,y=60)

b=Button(window,text='3',width='12',command=lambda:click(3))
b.place(x=220,y=60)

b=Button(window,text='4',width='12',command=lambda:click(4))
b.place(x=50,y=120)

b=Button(window,text='5',width='12',command=lambda:click(5))
b.place(x=130,y=120)

b=Button(window,text='6',width='12',command=lambda:click(6))
b.place(x=220,y=120)

b=Button(window,text='7',width='12',command=lambda:click(7))
b.place(x=50,y=180)

b=Button(window,text='8',width='12',command=lambda:click(8))
b.place(x=130,y=180)

b=Button(window,text='9',width='12',command=lambda:click(9))
b.place(x=220,y=180)

b=Button(window,text='0',width='12',command=lambda:click(0))
b.place(x=50,y=240)


#Operators
def add():
    n1=e.get() #to get value from entry box 
    global math  #to help in equal to operator
    math="addition" 
    global i
    i=int(n1) #converting from string to integer
    e.delete(0,END) #deleting and storing entered value

b=Button(window,text='+',width='12',command=add)  
b.place(x=130,y=240)

def sub():
    n1=e.get()
    global math 
    math="substraction" 
    global i
    i=int(n1)
    e.delete(0,END)
    
b=Button(window,text='-',width='12',command=sub)
b.place(x=220,y=240)

def mult():
    n1=e.get()
    global math 
    math="multiplication" 
    global i
    i=int(n1)
    e.delete(0,END)
    
b=Button(window,text='*',width='12',command=mult)
b.place(x=50,y=300)

def div():
    n1=e.get()
    global math 
    math="divison" 
    global i
    i=int(n1)
    e.delete(0,END)
    
b=Button(window,text='/',width='12',command=div)
b.place(x=130,y=300)

def equal():
    n2=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,i+int(n2))
    elif math=="substraction":
        e.insert(0,i-int(n2))   
    elif math=="multiplication":
        e.insert(0,i*int(n2))   
    elif math=="divison":
        e.insert(0,i/int(n2))            

b=Button(window,text='=',width='12',command=equal)
b.place(x=220,y=300)

def clear():
    e.delete(0,END)

b=Button(window,text='CLEAR',width='12',command=clear)
b.place(x=130,y=350)



mainloop()