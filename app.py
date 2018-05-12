print("Hello World! Python")

from flask import Flask
from flask import send_from_directory

app=Flask(__name__,static_url_path='',static_folder='web/')

print('Starting Flask')

@app.route('/')

def home():

    print('Flask')
    return send_from_directory('','index.html')


if __name__=='__main__':

    app.run(host='0.0.0.0',port=9999,debug=True)
