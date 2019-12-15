from flask import Flask,render_template,request,redirect,url_for, session
import sqlite3 as sql
import os  

app = Flask(__name__)
app.secret_key=os.urandom(24)
@app.route("/")
def home():
    if "username"in session:
       return render_template("home.html")
    return render_template("login.html",msg="")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        try:
            username=request.form["username"]
            password=request.form["password"]
            print(username,password)
            with sql.connect("Org.db") as con:
                cur = con.cursor()
                cur.execute("""SELECT * FROM login WHERE userName='{}' AND password ='{}'""".format(username,password))
                rows = cur.fetchall()
                print (rows)
                if rows==[]:
                     msg="wrong username or password"
                     return render_template("login.html",msg=msg)  
                if username == rows[0][0] and password == rows[0][1]:
                     msg="Logged in successfully!"
                     session["username"]=username
                     print(msg)
                     return redirect(url_for("home"))
                else: print ("error")
  
        except:
             print("Something Wrong Happened")
        
    elif request.method == "GET":
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("home"))

@app.route("/departmentslist")
def departmentslist():
     try:
         with sql.connect("Org.db") as con:
             cur = con.cursor()
             cur.execute("select * from departments")
             rows = cur.fetchall()
             print(rows)
             return render_template("departments_list.html",data=rows)
     except:
         print("Something Wrong Happened")
 
@app.route("/addDepartment",methods=["POST","GET"])
def addDepartment():
    if request.method == "POST":
         try:
             department_name=request.form["department_name"]
             location_id=request.form["location_id"]
             with sql.connect("Org.db") as con:
                 cur = con.cursor()
                 cur.execute("insert into departments (department_name,location_id) \
                         values (?,?)",(department_name,location_id))
                 con.commit()
             msg="Department Added Successfully!"
             return render_template("add_department.html",msg=msg)
         except:
             print("Something  Wrong")
    elif request.method=="GET":
             return render_template("add_department.html")
      
       
@app.route("/viewEmployees",methods=["POST","GET"])
def view_employees():
     if request.method == "POST":
         department_id=request.form["department_id"]
         print(department_id)
         with sql.connect("Org.db") as con:
             cur = con.cursor()
             cur.execute("select * from employees where department_id = ?",(department_id,))
             rows = cur.fetchall()
             print(rows)
             if(rows !=[]):
               return render_template("employees_list.html",data=rows,depid=department_id)     
             else:
                 print ("---------------",rows)
                 return render_template("add_employees.html",department_id=department_id)

@app.route("/delete",methods=["POST","GET"])
def delete():
     delete_id=request.form["rip"]
     with sql.connect("Org.db") as con:
         cur = con.cursor()
         cur.execute("delete from employees where employee_id = ?",(delete_id,))
         con.commit()
         msg="Employee Deleted Successfully!"
     return  redirect(url_for("home"))

@app.route("/edit",methods=["POST","GET"])
def updateform():
     if request.method == "POST":
         employee_id=request.form["employee_id"]
         with sql.connect("Org.db") as con:
             cur = con.cursor()
             cur.execute("select * from employees Where employee_id=?",(employee_id,))
             rows = cur.fetchone()
             print(rows)
             return render_template("update_employee.html",rows=rows)
    
@app.route("/update",methods=["POST","GET"])
def update():
     if request.method == "POST":
         fname=request.form["fname"]
         lname=request.form["lname"]
         email=request.form["email"]
         phone_number=request.form["phone_number"]
         job_id=request.form["job_id"]
         salary=request.form["salary"]
         hire_date=request.form["hire_date"]
         department_id=request.form["department_id"]
         employee_id=request.form["employee_id"]
         with sql.connect("Org.db") as con:
             cur = con.cursor()
             cur.execute("update employees set fname = ?,lname=?,email=?,phone_number=?,job_id=?,salary=?,hire_date=?,department_id=? where employee_id = ?",(fname,lname,email,phone_number,job_id,salary,hire_date,department_id,employee_id,))
             con.commit()
             msg="Employee Edited Successfully!"
             return render_template("home.html",msg=msg)
#         
@app.route("/addEmployees",methods=["POST","GET"])
def add_employees():
    if request.method == "POST":
             department_id=request.form["department_id"]
             return render_template("add_employees.html",department_id=department_id)
    elif request.method=="GET":
             return redirect(url_for("home"))
         
@app.route("/saveEmployees",methods=["POST","GET"])
def saveEmployees():
    if request.method == "POST":
       try:
         fname=request.form["fname"]
         lname=request.form["lname"]
         email=request.form["email"]
         phone_number=request.form["phone_number"]
         job_id=request.form["job_id"]
         salary=request.form["salary"]
         hire_date=request.form["hire_date"]
         department_id=request.form["department_id"]
         print((fname,lname,email,phone_number,job_id,salary,hire_date,department_id))
         with sql.connect("Org.db") as con:
              cur = con.cursor()
              cur.execute("insert into employees (fname,lname,email,phone_number,job_id,salary,hire_date,department_id) values (?,?,?,?,?,?,?,?)",(fname,lname,email,phone_number,job_id,salary,hire_date,department_id,))
              con.commit()
              msg="Department Added Successfully!"
              return redirect(url_for("departmentslist"))
       except:
             print("Something  Wrong")
    elif request.method=="GET":
             return redirect(url_for("home"))
        

if __name__ == "__main__":
    app.run()
    
    