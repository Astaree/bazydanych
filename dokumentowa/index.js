const express = require('express');
const router = require('./router/router');
const morgan = require('morgan');
const { imortEnv } = require('./config/env');
const { connectToDatabase } = require('./config/database');


const env = imortEnv();
const db = connectToDatabase(env.DATABASE_URL);

// Use morgan for logging
const app = express();

app.use(new morgan('combined'));

app.use(express.json());

// Use the router for handling routes
app.use('/', router);

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
