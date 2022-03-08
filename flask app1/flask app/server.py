
import mysql.connector
from flask import Flask, render_template,request
app = Flask(__name__)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="hemodialysis department"
)
mycursor = mydb.cursor()
@app.route('/')
def home():
   return render_template ("home.html")
@app.route('/appointment')
def doctors():
   mycursor.execute("SELECT * FROM appointment")
   row_headers=[x[0] for x in mycursor.description] #this will extract row headers
   myresult = mycursor.fetchall()
   return render_template ("appointment.html",doctor=myresult)
@app.route('/doctorlist')
def doctorlist():
   mycursor.execute("SELECT name,start_time,end_time,degree,email FROM doctor")
   row_headers=[x[0] for x in mycursor.description] #this will extract row headers
   myresult = mycursor.fetchall()
   return render_template ("doctorlist.html",doctorlist=myresult)
@app.route('/booking',methods=['GET','POST'])
def booking():
   if request.method =="POST" :
      fname=request.form['fname']
      lname=request.form['lname']
      Appdate=request.form['appointment date']
      doctor_name=request.form['doctor_name']
      email=request.form['email']
      sql = "INSERT INTO appointment (fname,lname,Appdate,doctor_name,email) VALUES (%s,%s,%s,%s,%s)"
      val = (fname,lname,Appdate,doctor_name,email)
      mycursor.execute(sql, val)
      mydb.commit() 
      print(fname,lname,Appdate,doctor_name,email)
      return render_template ("home.html")
   else:   
      return render_template ("booking.html")
@app.route('/register',methods=['GET','POST'])
def register():
   if request.method =="POST" :
      fname=request.form['fname']
      lname=request.form['lname']
      phone_number=request.form['phone_number']
      email=request.form['email']
      medical_history=request.form['medical_history']
      birthdate=request.form['birthdate']
      ssn=request.form['ssn']
      sql = "INSERT INTO patient (fname,lname,phone_number,email,medical_history,birthdate,ssn) VALUES (%s, %s, %s,%s,%s,%s,%s)"
      val = (fname,lname,phone_number,email,medical_history,birthdate,ssn)
      mycursor.execute(sql, val)
      mydb.commit() 
      print(fname,lname,phone_number,email,medical_history,birthdate,ssn)
      return render_template ("home.html")
   else:   
      return render_template ("register.html")

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=80)
   