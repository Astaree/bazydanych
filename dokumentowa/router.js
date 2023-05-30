const express = require('express');
const router = express.Router();
const connectToDatabase = require('./database');
const morgan = require('morgan');

// Define routes
router.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Example route that interacts with the database
router.get('/users', async (req, res) => {
  const db = await connectToDatabase();
  const users = await db.collection('users').find().toArray();
  res.json(users);
});

module.exports = router;
