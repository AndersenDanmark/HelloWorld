print("Hello World! monkeymonkey")

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
'''
conn = pymysql.connect(host='s0znzigqvfehvff5.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                        port=3306, 
                        user='yln2gxt9djlnxre6',
                        passwd='gzkozs8m6j1gfk4h',
                        db='b59xwd91o4xf8moh')
cur = conn.cursor()

sql="INSERT INTO b59xwd91o4xf8moh.HOUSES (MLS_Number,SQF,Land_Size,Price,Mag_Fees,Year_Built,Sotreys,Bedrooms,Washrooms) VALUES ('C4172305', '1896', '143','504900','0','1990','2','4','4');"

cur.execute(sql)
conn.commit()

#cur.execute(print([i [0] for i in cur] [0]))

cur.execute("SELECT * FROM b59xwd91o4xf8moh.HOUSES")
for row in cur:
  print(row)
conn.close()
'''
if __name__=='__main__':

    app.run(host='0.0.0.0',port=8080,debug=True)



