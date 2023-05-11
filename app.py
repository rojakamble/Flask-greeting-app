from flask import Flask, render_template, request, flash, session
import os

app = Flask(__name__) #CREATES A CLASS FOR OUR APP
app.secret_key = "giraffee_HGHJGJHG666"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")
    

if __name__=="__main__":
    app.run(debug=True)