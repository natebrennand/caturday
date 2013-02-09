
from flask import Flask, render_template, request, redirect
from credentials import filepicker
from random import random

app = Flask(__name__)

@app.route('/devfest')
def devfest():
	return redirect('http://adicu.com/devfest')

@app.route('/upload')
def upload():
	random_id = int(random() * 10**6)
	return render_template('upload.html',
		filekey = filepicker,
		id = random_id)

@app.route('/photo')
@app.route('/photo/<photo_id>')
def photo( photo_id = 'FvnGx5agRwCEIWnat6W9'):
	return render_template('photo.html',
		url = photo_id)


@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.debug = True
	app.run()

