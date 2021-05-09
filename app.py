from flask import Flask  , render_template , request , redirect , url_for
from main2 import ach
app = Flask(__name__)


@app.route("/")
def home():
   return redirect(url_for("set1a"))

@app.route('/set1/a', methods=["POST","GET"])
def set1a():
   if request.method =="POST":
      
      tempans = request.form["query1"]

      temp = "working alone"
      temp = ach(tempans)

      print (temp)
      return render_template('/set1/b.html', ans=temp)
      # return redirect(url_for("set1b", ans=temp))


@app.route('/set1/b')
def set1b():
   return render_template('/set1/b.html')

@app.route('/set1/c')
def set1c():
   return render_template('/set1/c.html')




if __name__ =="__main__":
    app.run(debug=True)