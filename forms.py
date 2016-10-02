from flask import Flask, render_template, request, redirect
from utils import csv_tools as csv
import hashlib

app = Flask(__name__)

@app.route("/")
def root():
	print request.headers
	return render_template("homepage.html")


@app.route("/login")
def login():
    print request.headers
    return render_template('login.html')
	
@app.route("/register")
def register():
	print request.headers
	return render_template('register.html')
	
	
@app.route("/authenticate", methods = ['POST'])
def auth():
	print request.headers
	print request.form
	usrPass = csv.convertToDict('data/passwords.csv')
	user = request.form["user"]
	if user not in usrPass:
		return render_template("auth.html", message = "NO SUCH USERNAME EXISTS")
	if usrPass[user] == hashlib.md5(request.form["pswrd"]).hexdigest():
		return render_template("auth.html", message = "SUCCESS")
	return render_template("auth.html", message = "WRONG PASSWORD")
	
@app.route("/makeAccount", methods = ['POST'])
def makeAccount():
	print request.headers
	print request.form
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
	return render_template('login.html', foo = 'Login', message = "Account Successfully Made")
	#return redirect("/login", code=301)

if __name__ == "__main__":
    app.debug = True 
    app.run()
