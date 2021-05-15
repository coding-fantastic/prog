from flask import Flask  , render_template , request , redirect , url_for
from main2 import ach
from collections import deque
# from dbConn import readDb

app = Flask(__name__)

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
         return render_template('/set2/a.html', ans="can you please try again ")
      else:
         if "intution" in temp:
            temp  = temp[1]
         else:
            temp = temp[0]
         if len(finaltype) != 1:
            # finaltype.popleft()
            return render_template('/set1/a.html', ans="queue was greater than one.")
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
         return render_template('/set3/a.html', ans="can you please try again ")
      else:
         temp = temp[0]
         if len(finaltype) != 2:
            return render_template('/set1/a.html', ans="queue was greater than two.")
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
         return render_template('/set4/a.html', ans="can you please try again ")
      else:
         temp = temp[0]
         if len(finaltype) != 3:
            return render_template('/set1/a.html', ans="queue was greater than three.")
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
   return render_template('/final.html', type = abrr)


if __name__ =="__main__":
    app.run(debug=True)