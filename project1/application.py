import os
from flask import Flask, session, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
# Check for environment variable
#if not os.getenv("postgres://veyvwgmurymfsv:69b5667c92bfce605201072f1d795ba0b5d1ebd66b8acb655433e6e9746efac7@ec2-54-86-170-8.compute-1.amazonaws.com:5432/dfngc8qg8hpqb5"):
    #raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
#engine = create_engine(os.getenv("postgres://veyvwgmurymfsv:69b5667c92bfce605201072f1d795ba0b5d1ebd66b8acb655433e6e9746efac7@ec2-54-86-170-8.compute-1.amazonaws.com:5432/dfngc8qg8hpqb5"))
#db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email, password)
        return render_template("search.html")

@app.route("/submits", methods=['POST'])
def submits():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(email, password)
        return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()