#!flask/bin/python
from flask import Flask, jsonify, render_template, request
from flask.ext.httpauth import HTTPBasicAuth
from model import DBconn
import sys,flask

app = Flask(__name__)
auth = HTTPBasicAuth()

def spcall(qry, param, commit=False):
    try:
        dbo = DBconn()
        cursor = dbo.getcursor()
        cursor.callproc(qry, param)
        res = cursor.fetchall()
        if commit:
            dbo.dbcommit()
        return res
    except:
        res = [("Error: " + str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]),)]
    return res

@auth.get_password
def getpassword(username):
    return spcall("getpassword", (username,))[0][0]

@app.route('/', methods=['GET', 'POST'])
def inserttask():

	if request.method == 'POST':
		valueName = request.form.get('name')
		valueUsername = request.form.get('username')
		valuePass = request.form.get('pass')
		done = ""
		res = spcall("newuser", (valueName, valueUsername, valuePass, True), True)
		return jsonify({'status': 'ok',})

		if 'Error' in res[0][0]:
			return jsonify({'status': 'error', 'message': res[0][0]})

	return render_template('index.html')

@app.after_request
def add_cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = flask.request.headers.get('Origin', '*')
    resp.headers['Access-Control-Allow-Credentials'] = True
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET, PUT, DELETE'
    resp.headers['Access-Control-Allow-Headers'] = flask.request.headers.get('Access-Control-Request-Headers',
                                                                             'Authorization')
    # set low for debugging

    if app.debug:
        resp.headers["Access-Control-Max-Age"] = '1'
    return resp

if __name__ == '__main__':
    app.run(debug=True)