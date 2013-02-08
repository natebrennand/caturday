
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/devfest')
def devfest():
	return redirect('http://adicu.com/devfest')

@app.route('/')
@app.route('/<name>')
def index(name='world'):
	return render_template('index.html',
				name = name)


if __name__ == '__main__':
	app.debug = True
	app.run()

