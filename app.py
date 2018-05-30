print("Hello World! monkeymonkey")

from flask import Flask, render_template,abort
from flask import send_from_directory
from flask import request
import pymongo
from pymongo import MongoClient
import json
import pymysql
import json

app=Flask(__name__,static_url_path='',static_folder='web/')

print('Starting Flask')
'''
@app.route('/add')
def add():
    x= int(request.args.get('x'))
    y = int(request.args.get('y'))
    z=x+y
    ret = json.dumps(z)
    return ret
'''
@app.route('/')
def home():

    print('Flask')
    return send_from_directory('','index.html')
#build connection

client =MongoClient("mongodb://andrewyan:andrewyan!23@ds237660.mlab.com:37660/heroku_zdtgskz7")

#creating a database called db
db = client.heroku_zdtgskz7

#creating a collection (table) called collection
collection = db.datasciencejobs

cursor=collection.find({"Company Name":"eBay Inc."},{"_id":0})
job_descriptions={}
for doc in cursor:
    job_descriptions=doc
print(job_descriptions)  


@app.route('/getjob')
def getjob():
    ret=json.dumps(job_descriptions)
    print("this is the getjob function")
    return(ret)
    
print('123')  
@app.route('/company/<name>')
def company(name):
    print(name)
    
    cursor=collection.find({"Company Name":str(name)},{"_id":0})
    for doc in cursor:
        xjob_descriptions=doc
    print(xjob_descriptions)

    ret = json.dumps(xjob_descriptions)

    return ret
    
company("Indeed")
print('456') 


if __name__=='__main__':

    app.run(host='0.0.0.0',port=8080,debug=True)



