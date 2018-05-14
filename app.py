print("Hello World! Python")

from flask import Flask
from flask import send_from_directory
from flask import request
import pymysql
import json

app=Flask(__name__,static_url_path='',static_folder='web/')

print('Starting Flask')

@app.route('/add')
def add():
    x= int(request.args.get('x'))
    y = int(request.args.get('y'))
    z=x+y
    ret = json.dumps(z)
    return ret

@app.route('/')
def home():

    print('Flask')
    return send_from_directory('','index.html')

conn = pymysql.connect(host='s0znzigqvfehvff5.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', port=3306, user='yln2gxt9djlnxre6', passwd='gzkozs8m6j1gfk4h', db='b59xwd91o4xf8moh')


if __name__=='__main__':

    app.run(host='0.0.0.0',port=8080,debug=True)



