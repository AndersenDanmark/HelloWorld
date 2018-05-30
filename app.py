print("Hello World! monkeymonkey")

from flask import Flask
from flask import send_from_directory
from flask import request
import pymongo
from pymongo import MongoClient
import json
import pymysql
import json

#build connection

client =MongoClient("mongodb://andrewyan:andrewyan!23@ds237660.mlab.com:37660/heroku_zdtgskz7")

#creating a database called jobs_database
db = client.heroku_zdtgskz7

#creating a collection (table) called collection
collection = db.datasciencejobs

cursor=collection.find({"Company Name":"eBay Inc."})
job_descriptions={}
for doc in cursor:
    job_descriptions=doc

print(job_descriptions)

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

@app.route('/')
def getjob():
    ret=json.dumps(job_descriptions)

    print(ret)
    
if __name__=='__main__':

    app.run(host='0.0.0.0',port=8080,debug=True)



