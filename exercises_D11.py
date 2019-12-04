from tkinter import *
from tkinter.colorchooser import *
from tkinter import messagebox
from tkinter import scrolledtext
print("""\nExercises 1\n """)
"""****************************************************************************************"""
#def vald ():
#    if v1.get() == "Orange" and v2.get() == "CodingAcademy" :
#         z = messagebox.showinfo("Login", "Successful login")
#         if z == "ok":
#             parent.destroy()
#    else:
#         messagebox.showinfo("Login", "Wrong User Name or Password")
#parent = Tk()
#v1 = StringVar()
#v2 = StringVar()
#
#name = Label(parent, text = "Name").grid(row=0, column = 0)
#x = Entry(parent, textvariable= v1).grid(row = 0, column =1)
#password = Label(parent, text ="Password").grid(row = 1, column = 0)
#x = Entry(parent, textvariable= v2).grid(row = 1, column =1)
#submit = Button(parent, text="Submit", command= vald).grid(row = 3, column = 0)
#parent.mainloop()

print("""\nExercises 2\n """)
"""****************************************************************************************"""
#def child1():
#    title=""
#    text="This is a message"
#    x=messagebox.showinfo(title,text)
#    
#def child2():
#    top=Tk()
#    top.title('Child  2')
#    top.geometry('400x250')
#    name=Label(top,text="Emy Number").grid(row=0, column = 0)
#    email=Label(top,text="Emy Name").grid(row=1, column = 0)
#    m1=Entry(top).grid(row=0, column = 1)
#    m2=Entry(top).grid(row=1, column = 1)
#    button=Button(top,text="exit",command=top.destroy).grid(row=3, column = 0)
#    button.pack()
#    top.mainloop()
#    
#def child3():
#   child3_sc = Toplevel(root)
#   child3_sc.title("View Student")
#   child3_sc.geometry("600x600+"+str(int((screen_width-300)/4))+"+"+str(int((screen_height-150)/4)) )
#   frame1 = Frame(master = child3_sc)
#   frame1.pack(fill='both', expand='yes')
#   textArea = tkst.ScrolledText(  master = frame1,    wrap   = WORD,    width  = 200,    height = 100)
#   textArea.pack(padx=10, pady=10, fill=BOTH, expand=True)
#   for item in range(5):
#       textArea.insert(END,"the count is :")
#       textArea.insert(END,item)
#       textArea.insert(END,"\n\n") 
#    
#root = Tk()
#root.title('Root window')
#screen_width=root.winfo_screenwidth()/2
#screen_height=root.winfo_screenheight()/2
#root.geometry("400x150+"+str(int(screen_width-300/2))+"+"+str(int(screen_height-150/2)) )
#Button(root, text = 'open child window 1', command = child1).grid(row=0, column = 0)
#Button(root, text = 'open child window 2', command = child2).grid(row=1, column = 0)
#Button(root, text = 'open child window 3', command = child3).grid(row=2, column = 0)
#root.mainloop()

print("""\nExercises 3\n """)
"""****************************************************************************************"""
#root = Tk()
#screen_width=root.winfo_screenwidth()/2
#screen_height=root.winfo_screenheight()/2
#root.geometry("400x150+"+str(int(screen_width-300/2))+"+"+str(int(screen_height-150/2)) )
#
#def getcolor():
#    color=askcolor()
#    root.config(background=color[1])
#
#Button(root,text="select",command=getcolor).pack()
#mainloop()
