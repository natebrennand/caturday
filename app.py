from flask import flask, render_template, request
app = Flask(__name__)

@app.route('/devfest')
def devfest():
	return redirect('http://adicu.com/devfest')

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.debug = True
	app.run()
	


