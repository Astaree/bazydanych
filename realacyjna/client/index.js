const express = require('express');
const path = require('path');

const app = express();

app.use(express.static(path.join(__dirname, 'build'))); //static files from build folder
app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname,'pages', './index.html'));
    }
);


app.listen(9000); //port on which server is listening
console.log('Server is listening on port 9000');
