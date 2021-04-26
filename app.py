from flask import Flask  , render_template , request , redirect , url_for
app = Flask(__name__)


@app.route('/set1/a')
def set1a():
   return render_template('/set1/a.html', myString="Jinja is awesome!!!")

@app.route('/set1/b')
def set1b():
   return render_template('/set1/b.html')

@app.route('/set1/c')
def set1c():
   return render_template('/set1/c.html')


if __name__ =="__main__":
    app.run(debug=True)