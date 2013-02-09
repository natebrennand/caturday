
from flask import Flask, render_template, request, redirect
from credentials import filepicker

app = Flask(__name__)

@app.route('/devfest')
def devfest():
	return redirect('http://adicu.com/devfest')

@app.route('/upload')
def upload():
	return render_template('upload.html',
			filekey = filepicker)


@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.debug = True
	app.run()

