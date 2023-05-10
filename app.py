from flask import *
from database import init_db, db_session
from models import *
import time

app = Flask(__name__)

@app.route("/")
def base():
    if request.method == "GET":
        snacknames = []
        snackname = db_session.query(Snack.name).all()
        for name in snackname:
            snacknames.append(name[0])


        snackpics = []
        snackpic = db_session.query(Snack.picture).all()
        for picture in snackpic:
            snackpics.append(picture[0])
            
        
        return render_template("home_page.html", 
                                snack1=snackpics[0], 
                                snack2=snackpics[1], 
                                snack3=snackpics[2],
                                title1=snacknames[0],
                                title2=snacknames[1],
                                title3=snacknames[2],
                                snack1_page = "/snack/doritos",
                                snack2_page = "/snack/lays",
                                snack3_page = "/snack/cheetos")

@app.route("/home")
def home():
    if request.method == "GET":
        snacknames = []
        snackname = db_session.query(Snack.name).all()
        for name in snackname:
            snacknames.append(name[0])

        snackpics = []
        snackpic = db_session.query(Snack.picture).all()
        for picture in snackpic:
            snackpics.append(picture[0])
       
            
        
        return render_template("home_page.html", 
                                snack1=snackpics[0], 
                                snack2=snackpics[1], 
                                snack3=snackpics[2],
                                title1=snacknames[0],
                                title2=snacknames[1],
                                title3=snacknames[2],
                                snack1_page = "/snack/doritos",
                                snack2_page = "/snack/lays",
                                snack3_page = "/snack/cheetos")
                                
                                   

            

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login_page.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_list = db_session.query(User).where((username == User.username) & (password == User.password)).all()
        if len(user_list) > 0:
            session["username"] = username
            flash("Successfully logged in!", "message")
            time.sleep(1)
            return redirect(url_for("home"))
        else:
            flash("No user exists with that username / password, try again", "message")
            time.sleep(1)
            return redirect(url_for("login"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        # Code for handling GET requests
        return render_template("signup_page.html")
    elif request.method == "POST":
        # Code for handling POST requests
        username = request.form["username"]
        password = request.form["password"]
        conf_password = request.form["conf_password"]

        if password == conf_password:
            count = db_session.query(User).where(username == User.username).count()
            if count > 0:
                flash("Username already taken, try again", "error")
                time.sleep(1)
                return redirect(url_for("signup"))
            else:
                temp = User(username = username, password = password)
                db_session.add(temp)
                db_session.commit()
                session["username"] = username
                flash("Signed up successfully!", "error")
                time.sleep(1)
                return redirect(url_for("home"))
        else:
            flash("Passwords do not match", "error")
            time.sleep(1)
            return redirect(url_for("signup"))

        
        

@app.route("/snack")
def snack():
    if request.method == "GET":
            return render_template("snack_page.html")

@app.route("/snack/<snack>")
def choice(snack):
    if(snack=="doritos"):
        return render_template("doritos.html",snack=snack)
    elif(snack=="lays"):
        return render_template("lays.html",snack=snack)
    elif(snack=="cheetos"):
        return render_template("cheetos.html",snack=snack)
    else:
        return redirect(url_for("home_page.html"))

@app.route("/account")
def account():
    if request.method == "GET":
        curr_acc = db_session.query(User).where(User.username == session["username"]).first()
        return render_template("account_page.html", username = curr_acc.username,
                                                    password = curr_acc.password)





# TODO: Change the secret key
app.secret_key = "deez"
# TODO: Fill in methods and routes

@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
