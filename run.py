from flask import Flask, render_template, redirect, url_for, session, jsonify
import psycopg2
import logging
import braintree
from flask import request
import os
import urlparse

app = Flask(__name__)
app.debug = True
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
braintree.Configuration.configure(
	braintree.Environment.Sandbox,
	'xzk9p3947gggzsgt',
	'wgp52v9n7stqjd2c',
	'beae8f107b64b387a434dbe4b1686a16'
)

# Uncomment when deploy to heroku
host = os.environ['DATABASE_URL']
#host = 'localhost'
#global_challenge = ''


@app.route("/")
def show_challenges():

	try:
		urlparse.uses_netloc.append("postgres")
		url = urlparse.urlparse(os.environ["DATABASE_URL"])

		conn = psycopg2.connect(
		database=url.path[1:],
		user=url.username,
		password=url.password,
		host=url.hostname,
		port=url.port
	)
	
		#conn = psycopg2.connect("dbname='challenge_for_people' user='root' host= " + host + " password='root'")
		cursor = conn.cursor()
		query = "SELECT name FROM challenges;"
		cursor.execute(query)
		challenges = cursor.fetchall()
		return render_template("challenges.html", challenges = challenges)
	except:
		logging.exception("Something awful happened!")
		return "-1"
		

@app.route("/projects")
def projects():
	cursor = mysql.connect().cursor()
	query = "SELECT id_project, hashtag FROM projects;"
	cursor.execute(query)
	projects = cursor.fetchall()
	return render_template("projects.html", projects = projects)

@app.route("/register_event")
def register_event():
	#project = request.args.get('project', '')
	
	return render_template("register_event.html")

@app.route("/become_hero")
def become_hero():
	project = request.args.get('project', '')
	
	return render_template("register_event.html")


@app.route("/challenge/<challenge>")
def challenge(challenge):
	
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	conn = psycopg2.connect(
		database=url.path[1:],
		user=url.username,
		password=url.password,
		host=url.hostname,
		port=url.port
	)
	
	#conn = psycopg2.connect("dbname='challenge_for_people' user='root' host= " + host + " password='root'")
	cursor = conn.cursor()
	token = client_token()
	print token
	session['challenge'] = challenge
	print "global_challenge %s" % session['challenge']
	query = "SELECT * FROM challenges WHERE name = '%s'" % challenge
	print challenge
	cursor.execute(query)
	challenge_structure = cursor.fetchone()
	return render_template("challenge.html", challenge = challenge_structure, token = token);

# Functions
@app.route("/client_token", methods=["GET"])
def client_token():
	return braintree.ClientToken.generate()

@app.route("/checkout", methods=["POST"])
def create_checkout():
	print "create checkout"
	nonce = request.form["payment_method_nonce"]
	amount = request.form["amount"]
	amount = amount[1:]
	print amount

	result = braintree.Transaction.sale({
		"amount": str(amount),
		"payment_method_nonce": nonce
	})

	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	conn = psycopg2.connect(
		database=url.path[1:],
		user=url.username,
		password=url.password,
		host=url.hostname,
		port=url.port
	)

	#conn = psycopg2.connect("dbname='challenge_for_people' user='root' host= " + host + " password='root'")
	print "global challenge %s" % session['challenge']
	query = "UPDATE challenges SET levying = levying + %d, donators = donators + 1 WHERE name = '%s'" % (int(amount), session['challenge'])
	print challenge
	cursor = conn.cursor()
	cursor.execute(query)
	conn.commit()
	conn.close()
	return render_template("thanks.html");

if __name__ == "__main__":
	app.run()