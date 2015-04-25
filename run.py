from flask import Flask, render_template, redirect, url_for, session
from flaskext.mysql import MySQL
from flask import request


mysql = MySQL()
app = Flask(__name__)
app.debug = True
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'challenge_for_people'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def show_challenges():
	cursor = mysql.connect().cursor()
	query = "SELECT name FROM challenges;"
	cursor.execute(query)
	challenges = cursor.fetchall()
	return render_template("challenges.html", challenges = challenges)		

@app.route("/projects")
def projects():
	cursor = mysql.connect().cursor()
	query = "SELECT id_project, hashtag FROM projects;"
	cursor.execute(query)
	projects = cursor.fetchall()
	return render_template("projects.html", projects = projects)

@app.route("/donate")
def donate():

	return "0"

@app.route("/challenge/<challenge>")
def challenge(challenge):
	#project = request.args.get('project', '')
	cursor = mysql.connect().cursor()
	query = "SELECT * FROM challenges WHERE name = '%s'" % challenge
	print challenge
	cursor.execute(query)
	challenge_structure = cursor.fetchone()
	return render_template("challenge.html", challenge = challenge_structure);

if __name__ == "__main__":
	app.run()