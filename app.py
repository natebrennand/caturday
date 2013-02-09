
from flask 			import Flask, render_template, request, redirect
from credentials 	import filepicker
from random 		import random
from time 			import sleep
from os				import system


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


@app.route('/photo', methods=['POST'])
def photo():
	url = request.form['url']
	command = "fd.sh",url		#awesome programming
	system( command )
	print url	# WORKS!!!!!
	sleep(.5)
	return render_template('photo.html',
		url = '/var/www/imgs/final.jpg')


@app.route('/')
def index():
	return render_template('index.html')



if __name__ == '__main__':
	app.debug = True
	app.run()

