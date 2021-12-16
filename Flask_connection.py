from flask import Flask, render_template, url_for, request
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='static')
	       
# configre db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lanamodern#1999'
app.config['MYSQL_DB'] = 'gatedown'


mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	

    return render_template('mainPage.html')

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		userDetails = request.form
		email = userDetails['email']
		pswd = userDetails['pswd']
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM customer WHERE email = %s AND password = %s", (email, pswd,))
		mysql.connection.commit()
		account = cur.fetchone()
		cur.close()
		if account:
			return "success"
		else:
			return render_template('logInPage.html')


		
		cur.close()
	return render_template('logInPage.html')

@app.route('/create', methods=['GET','POST'])
def create():
	if request.method == 'POST':
		userDetails = request.form
		first = userDetails['first']
		last = userDetails['last']
		email = userDetails['email']
		password = userDetails['pswd']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO customer(customerfirst,customerlast,email,password) VALUES(%s,%s,%s,%s)",(first,last,email,password))
		mysql.connection.commit()
		cur.close()
		return render_template('accountLog.html')
	return render_template('accountLog.html')

@app.route('/checkout', methods=['GET','POST'])
def checkout():
	if request.method == 'POST':
		userDetails = request.form
		address = userDetails['address']
		first = userDetails['first']
		last = userDetails['last']
		email = userDetails['email']
		city = userDetails['City']
		zipcode = userDetails['zipcode']
		cc = userDetails['cc']
		phone = userDetails['phone']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO order(cardnumber,billingaddress,zip,phone,city) VALUES(%s,%s,%s,%s,%s)",(cc,address,zipcode,phone,city))
		mysql.connection.commit()
		cur.close()
		return render_template('checkout.html')
	return render_template('checkout.html')




@app.route('/shop', methods=['GET','POST'])
def shop():
	return render_template('basicStore.html') 

@app.route('/js', methods=['GET','POST'])
def js():
	return render_template('main.js')

if __name__ == '__main__':
    app.run(port = 3000, debug = True)