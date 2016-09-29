from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    print request.headers
    return render_template('forms.html', foo = 'Formpage')

@app.route("/authenticate", methods = ['POST'])
def auth():
	usrPass = {'username':'password'}
	print request.headers
	print request.form
	if usrPass[request.form["user"]] == request.form["pswrd"]:
		return render_template("auth.html", foo = 'Authentication' , message = "SUCCESS")
	return render_template("auth.html", foo = 'Authentication' ,  message = "FAILURE")

if __name__ == "__main__":
    app.debug = True 
    app.run()
