from flask import Flask  , render_template , request , redirect , url_for  , session
from main2 import ach
from collections import deque
from dbConn import readDb , checkUser , newAns , insertComment
import hashlib


app = Flask(__name__)
app.secret_key = 'any random string'
finaltype =  deque()

@app.route("/")
def home():
   return redirect(url_for("set1a"))

@app.route('/set1/a', methods=["POST","GET"])
def set1a():
   if request.method =="POST":
      
      tempans = request.form["query1"]

      temp = "working alone"
      temp = ach(tempans)

      if  "can you repeat that please" in temp:
         queryNumber = 1
         newAns(tempans , queryNumber)
         return render_template('/set1/a.html', ans="can you please try again ")
      else:

         print("response => " + str(temp))
         temp = temp[0]
         if len(finaltype) != 1:
            finaltype.clear()
         finaltype.append(temp.upper())
         print("\nqueue =>" + str(finaltype)+ "\n")         
         return render_template('/set2/a.html')
      # return redirect(url_for("set1b", ans=temp))
         # return redirect(url_for("set1a"))
   return render_template('/set1/a.html')


@app.route('/set2/a', methods=["POST","GET"])
def set2():
   if request.method =="POST":
      
      tempans = request.form["query2"]

      temp = "working alone"
      temp = ach(tempans)

      if  "can you repeat that please" in temp:
         queryNumber = 2
         newAns(tempans , queryNumber)
         return render_template('/set2/a.html', ans="can you please try again ")
      else:
         if "intution" in temp:
            temp  = temp[1]
         else:
            temp = temp[0]
         if len(finaltype) != 1:
            # finaltype.popleft()
            return render_template('/set1/a.html', ans="queue was greater than one. Start again")
         finaltype.append(temp.upper())
         print("\nqueue =>" + str(finaltype)+ "\n")         
         return render_template('/set3/a.html')
   return render_template('/set2/a.html')

@app.route('/set3/a', methods=["POST","GET"])
def set3():
   if request.method =="POST":
      
      tempans = request.form["query3"]

      temp = "working alone"
      temp = ach(tempans)

      if  "can you repeat that please" in temp:
         queryNumber = 3
         newAns(tempans , queryNumber)
         return render_template('/set3/a.html', ans="can you please try again ")
      else:
         temp = temp[0]
         if len(finaltype) != 2:
            return render_template('/set1/a.html', ans="queue was greater than two. Start again")
         finaltype.append(temp.upper())
         print("\nqueue =>" + str(finaltype)+ "\n")         
         return render_template('/set4/a.html')
   return render_template('/set3/a.html')

abrr = ""
@app.route('/set4/a', methods=["POST","GET"])
def set4():
   if request.method =="POST":
      
      tempans = request.form["query4"]

      temp = "working alone"
      temp = ach(tempans)

      if  "can you repeat that please" in temp:
         queryNumber = 4
         newAns(tempans , queryNumber)
         return render_template('/set4/a.html', ans="can you please try again ")
      else:
         temp = temp[0]
         if len(finaltype) != 3:
            return render_template('/set1/a.html', ans="queue was greater than three.Start again")
         finaltype.append(temp.upper())
         print("\nqueue =>" + str(finaltype)+ "\n")         
         cleanedAbrr = finaltype[0] + finaltype[1] + finaltype[2] + finaltype[3]
         # readDb(cleanedAbrr)
         # return render_template('/final.html', type = cleanedAbrr)
         return redirect(url_for("result" , abrr =  cleanedAbrr) )
   return render_template('/set4/a.html')
   # return render_template('/final.html')

@app.route('/result/<string:abrr>')
def result(abrr):
   # this value is used as a control on readDb function eg number 1  is for result
   num = 1
   typeTblAndCareersTblList , careersToAvoidList = readDb(abrr,num)
   
   return render_template('/final.html', type = abrr , typeTblAndCareersTblList = typeTblAndCareersTblList , careersToAvoidList = careersToAvoidList)

@app.route("/cover")
def cover():
   return render_template('cover.html')


@app.route("/login", methods=["POST","GET"])
def login():
   if request.method =="POST":
      
      email = request.form["email"]
      passwd = request.form["passwd"]
      passwd = hashlib.md5(passwd.encode())
      passwd = passwd.hexdigest()
      print("\njpassword -+ "  + str(passwd))
      msg, username = checkUser(email, passwd)
      print(msg)
      if  "user not found" in msg:
         return render_template('login.html', ans="User was not found ")
      else:
         session['username'] = username
         # return render_template('dashboard.html' )

         return redirect(url_for("dashboard" ) )

      
   return render_template('login.html')

@app.route('/dashboard')
def dashboard():
   # check if session is set if not go back to login 
   if 'username'  in session:
      num =2
      abrr = "a"
      rows = readDb(abrr , num )
      return render_template('dashboard.html' , answersMissedList = rows)
   else:
      return render_template('login.html', ans="Please login")

@app.route('/register', methods=["POST","GET"])
def register():
   # check if session is set if not go back to login 
   if 'username'  in session:
      if request.method == "POST":
         username = request.form["username"]
         email = request.form["email"]
         passwd = request.form["passwd"]
         confirmPasswd = request.form['confirmPasswd']
         if passwd != confirmPasswd:
            return render_template('register.html', ans = "password and confirm password didn't match . Please Try again")

      return render_template('dashboard.html' )
   else:
      return render_template('login.html', ans="Please login")
   

@app.route("/logout")
def logout():
   session.pop("username", None)
   return redirect(url_for("cover"))

@app.route("/comment" , methods=["POST","GET"])
def comment():
   if request.method =="POST":
      name = request.form["name"]
      comment = request.form["comment"]
      print ("name - " + str(name) + " comment " + str(comment) )
      insertComment(name,comment)
      return render_template('comment.html', ans = "Thank you for the comment")
      
   return render_template("comment.html")



if __name__ =="__main__":
    app.run(debug=True)