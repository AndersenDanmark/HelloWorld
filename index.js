console.log('hello world')

var express = require('express') // npm install express
var app = express()
app.use(express.static('web'));
app.listen(8888, function () {
    console.log('starting web server');  
    });
app.get('/', function(request, response) {
response.sendFile(__dirname + '/index.html');
})

//http://localhost:8888/index.html 