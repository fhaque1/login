from flask import Flask, render_template, request, redirect, url_for, session
from utils import csv_tools as csv
import hashlib

app = Flask(__name__)
app.secret_key = "H\x90Z\x0b*j\xe8\xd9B\xfb\x05\xab\x06I\x0cw0\xca\xc6g\xe0/\x07\xf5~'\xe0l\xca\x87B?"

@app.route("/")
def root():
    if "user" in session.keys():
        return redirect(url_for("welcome"))
    return redirect(url_for("login"))

@app.route("/welcome")
def welcome():
	return render_template("welcome.html", name = session["user"]) 
	
@app.route("/login")
def login():
    if "user" in session.keys():
		return redirect(url_for("welcome"))
    return render_template('login.html')
	
@app.route("/authenticate", methods = ['POST'])
def auth():
	usrPass = csv.convertToDict('data/passwords.csv')
	user = request.form["user"]
	if user not in usrPass:
		return render_template("auth.html", message = "NO SUCH USERNAME EXISTS")
	if usrPass[user] == hashlib.md5(request.form["pswrd"]).hexdigest():
		session["user"] = request.form["user"]
		return redirect(url_for("root"))
	return render_template("auth.html", message = "WRONG PASSWORD")
	
@app.route("/makeAccount", methods = ['POST'])
def makeAccount():
	usrPass = csv.convertToDict('data/passwords.csv')
	user = request.form["newuser"]
	if user in usrPass:
		return render_template("makeAccount.html", made = "ACCOUNT NOT MADE", message = "Username Taken")
	pswrd = request.form["newpswrd"]
	pswrd2 = request.form["renewpswrd"]
	if pswrd != pswrd2:
		return render_template("makeAccount.html", made = "ACCOUNT NOT MADE", message = "Passwords Do Not Match")
	hashed = hashlib.md5(pswrd).hexdigest()
	string = user + "," + hashed + "\n"
	csv.editFile(string , 'data/passwords.csv')
	return render_template('makeAccount.html', made = "ACCOUNT MADE", message = "Account Successfully Made")
	
@app.route("/logout", methods = ['POST'])
def logout():
    session.pop("user")
    return redirect(url_for("login"))
	
if __name__ == "__main__":
    app.debug = True 
    app.run()
