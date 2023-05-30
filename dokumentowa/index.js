const express = require('express');
const router = require('./router');
const morgan = require('morgan');



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
