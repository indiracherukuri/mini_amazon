from flask import Flask,render_template,request,redirect,url_for,session

app=Flask(__name__)


app.secret_key="indu"
@app.route('/')
def home():	



	return render_template('home.html')

@app.route('/about')
def about():	



	return render_template('about.html',title='About')
@app.route('/contact')
def contact():	



	return render_template('contact.html',title='Contact')
@app.route('/login',methods=['GET','POST'])

def login():
	if request.method=='POST':	
		users={
		'user1':'123',
		'user2':'234',
		'user3':'1234',
		'user4':'2345'
		}
		username = request.form['username']
		password = request.form['password']

		if username not in users:
			return "user doesnt exist"
		if users[username]!= password:
			return "incorrect password"
		session[username]=username
		return redirect(url_for('home'))
	return redirect(url_for('home'))
@app.route('/logout')
def logout():	

	session.clear()
	return redirect(url_for('home'))
app.run(debug=True)