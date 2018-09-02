import sqlite3
from flask import render_template, flash, redirect, request
from app import app
from app.form import EnterForm
import os
import glob

user = os.getenv("USER")
path = '/home/' + str(user) + '/.mozilla/firefox/*.default'
path = glob.glob(path)[0]
path = str(path) + '/permissions.sqlite'

@app.route('/',  methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
	form = EnterForm()
	if form.validate_on_submit():
		return redirect('/result')
	return render_template('home.html', title='Home',  form=form)
	
@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		url = request.form['website']
		connection = sqlite3.connect( path ,check_same_thread=False)
		connection.row_factory = sqlite3.Row
		cur = connection.cursor()
		cur.execute("SELECT * FROM moz_perms WHERE Origin LIKE '" + str('%' +str(url)) + "'")
		rows = cur.fetchall();
		return render_template('result.html', title='Result', rows = rows, url = url)
	else:
		pass
@app.route('/about')
def about():
	return render_template('about.html', title='About')