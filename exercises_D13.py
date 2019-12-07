from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import sqlite3
conn = sqlite3.connect('OrgDB.db')
c = conn.cursor()
    
def creat_tabile():
    c.execute('''CREATE TABLE IF NOT EXISTS allEmp (
            EmployeeNumber integer PRIMARY KEY,
            EmployeeName text NOT NULL,
            EmployeeGender text NOT NULL,
            EmployeeNationality text NOT NULL,
            EmployeeDateofBirth text NOT NULL,
            EmployeeAddress text NOT NULL,
            EmployeeDepartment text NOT NULL,
            EmployeeSalary real NOT NULL
            )''')
    print("done")
    conn.commit()
      
def del_Employees():
   
    def delete_emp_fn ():
            c.execute("SELECT * FROM allEmp" )
            check=len(c.fetchall())
            print(check)
            x=EmployeeNumber.get()
            c.execute(f"DELETE from allEmp where EmployeeNumber = {x}")
            conn.commit()
            c.execute("SELECT * FROM allEmp" )
            print("z",check)
            after=len(c.fetchall())
            print("after",after)
            if(check!=after):
                z = messagebox.showinfo("Delete Employee", "Successful Deleted")
                if z == "ok":
                    del_em_sc.destroy()  
            else:
                z=messagebox.showinfo("Delete Employee", "Wrong Number check agane")
        
    del_em_sc = Toplevel(root)
    del_em_sc.title("Delete Employees")
    del_em_sc.geometry("200x100+400+400") 
    EmployeeNumber= IntVar()
    employees_num = Label(del_em_sc, text = "Employee Number").grid(row=0, column = 0)
    e1 = Entry(del_em_sc, textvariable= EmployeeNumber).grid(row = 0, column =1)
    submit = Button(del_em_sc, text="Delete", command= delete_emp_fn).grid(row = 4, column = 0)




root = Tk()
screen_width=root.winfo_screenwidth()/2
screen_height=root.winfo_screenheight()/2
root.geometry("400x150+"+str(int(screen_width-300/2))+"+"+str(int(screen_height-150/2)) )
root.title('Project 2')

def notdone():
    messagebox.showinfo('Not implemented', 'Not yet available')

def Add_Employee():
    c.execute('SELECT MAX(EmployeeNumber) AS maximam FROM allEmp')  
    def Add_Employee_submit ():
        creat_tabile()
        c.execute("INSERT INTO allEmp VALUES ({},'{}','{}','{}','{}','{}','{}',{})".format(EmployeeNumber.get(), EmployeeName.get(),EmployeeGender.get(),EmployeeNationality.get(),EmployeeDateofBirth.get(),EmployeeAddress.get(),EmployeeDepartment.get(),EmployeeSalary.get()))
        conn.commit()
        print ("upload done")
        
    add_em_sc = Toplevel(root)
    add_em_sc.title("Add Employees")
    add_em_sc.geometry("280x190+400+400")
    
    EmployeeNumber= IntVar()
    try:
        EmployeeNumber.set(c.fetchone()[0]+1)
    except:
        EmployeeNumber.set(1)
    EmployeeName= StringVar()
    EmployeeGender=StringVar()
    EmployeeNationality=StringVar()
    EmployeeDateofBirth=StringVar()
    EmployeeAddress=StringVar()
    EmployeeDepartment=StringVar()
    EmployeeSalary=DoubleVar()


    employee1 = Label(add_em_sc, text = "Employee Number").grid(row=0, column = 0)
    e1 = Entry(add_em_sc, textvariable= EmployeeNumber).grid(row = 0, column =1)
    
    employee2 = Label(add_em_sc, text = "Employee Name").grid(row=1, column = 0)
    e2 = Entry(add_em_sc, textvariable= EmployeeName).grid(row = 1, column =1)
    
    employees3 = Label(add_em_sc, text = "Employee Gender").grid(row=2, column = 0)
#    e3= Entry(add_em_sc, textvariable=EmployeeGender).grid(row = 2, column =1)
    e04=Radiobutton(add_em_sc, text="male",padx = 20, variable=EmployeeGender, value="male").grid(row=2, column = 1)
    e04=Radiobutton(add_em_sc,text="female", padx = 20, variable=EmployeeGender, value="female").grid(row=3, column = 1)
        
    employees4 = Label(add_em_sc, text = "Employee Nationality").grid(row=4, column = 0)
    e4= Entry(add_em_sc, textvariable=EmployeeNationality).grid(row = 4, column =1)
    
    employees5 = Label(add_em_sc, text = "Birthday").grid(row=5, column = 0)
    e5= Entry(add_em_sc, textvariable=EmployeeDateofBirth).grid(row = 5, column =1)
    
    employees6 = Label(add_em_sc, text = "EmployeeAddress").grid(row=6, column = 0)
    e6= Entry(add_em_sc, textvariable=EmployeeAddress).grid(row = 6, column =1)

    employees8 = Label(add_em_sc, text = "Employee Department").grid(row=7, column = 0)
    e8= Entry(add_em_sc, textvariable=EmployeeDepartment).grid(row = 7, column =1)

    employees9 = Label(add_em_sc, text = "Employee Salary").grid(row=8, column = 0)
    e9= Entry(add_em_sc, textvariable=EmployeeSalary).grid(row = 8, column =1)
    
    submit = Button(add_em_sc, text="Add", command= Add_Employee_submit).grid(row = 9, column = 1)

    
def view_Employee():
       view_em_sc = Toplevel(root)
       view_em_sc.title("View Employees")
       view_em_sc.geometry("600x600+"+str(int((screen_width-300)/4))+"+"+str(int((screen_height-150)/4)) )
       frame1 = Frame(master = view_em_sc,bg = 'red')
       frame1.pack(fill='both', expand='yes')
       textArea = tkst.ScrolledText(
        master = frame1,
        wrap   = WORD,
        width  = 200,
        height = 100)
       textArea.pack(padx=10, pady=10, fill=BOTH, expand=True)
       c.execute("SELECT * FROM allEmp" )
#       
       result = c.fetchall()
       print(result)
       for item in result:
           textArea.insert(END,item)
           textArea.insert(END,"\n\n")

     


label=Label(root,text="Exercises Day 13",font=('times',20,'bold'),padx=10,pady=10)
label.pack()




top = Menu(root)
root.config(menu=top)
file = Menu(top,tearoff=0)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)
top.add_cascade(label='File', menu=file)

Employees = Menu(top,tearoff= 0)
Employees.add_command(label='Add', command=Add_Employee)
Employees.add_command(label='View', command=view_Employee)
Employees.add_command(label='Delete', command=del_Employees)
top.add_cascade(label='Employees', menu=Employees)


Help = Menu(top,tearoff= 0)
Help.add_command(label='About', command=notdone)
top.add_cascade(label='Help', menu=Help)
root.mainloop()




