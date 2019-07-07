from flask import Flask, redirect, url_for, request, render_template
from queries import *
from mail import send
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/insert', methods = ['POST','GET'])
def insert_members_form():
    if(request.method == 'POST'):
        params = request.get_json(force=True)
        print(params)
        name = params['name']
        contact = params['contact']
        email=params['email']
        send(email)
		#return render_template('mail.py')
    else:
        return "Hello World"
if __name__ == '__main__':
	
	app.secret_key = 'super secret key'

	app.debug = True # debug is used for developing since it allows us to make changes in the python file without having to restart the server again and again.
	app.run('0.0.0.0')

