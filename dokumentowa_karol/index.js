const express = require('express');
const router = require('./router/router');
const morgan = require('morgan');
const { imortEnv } = require('./config/env');
const { connectToDatabase } = require('./config/database');
const mime = require('mime');
const cors = require('cors');


const env = imortEnv();
const db = connectToDatabase(env.DATABASE_URL);

// Use morgan for logging
const app = express();

app.use(new morgan('combined'));

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cors());

// Use the router for handling routes
app.use('/', router);

//file server
app.use(express.static('public', {
  setHeaders: (res, path) => {
    if (mime.getType(path) === 'text/css') {
      res.setHeader('Content-Type', 'text/css');
    }
  }
}));
app.set('view engine', 'pug');
// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
