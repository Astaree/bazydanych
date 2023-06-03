const express = require('express');
const { default: mongoose } = require('mongoose');
const router = express.Router();

// Define routes
router.get('/', (req, res) => {
  //list all routes
  res.status(200).json({
    message: 'Welcome to the API',
    routes: [
      {
        name: 'drinks',
        url: 'http://localhost:3000/drinks',
      },
      {
        name: 'ingredients',
        url: 'http://localhost:3000/ingredients',
      },
    ],
  });
});


// Example route that interacts with the database
router.get('/ingredients', (req, res) => {
  const Ingredient = require('../model/ingredients');
  Ingredient.find()
    .exec()
    .then((docs) => {
      res.status(200).json(docs);
    })
    .catch((err) => {
      console.error(err);
      res.status(500).json({ error: err });
    });
});

router.get('/drinks', (req, res) => {
  const Drink = require('../model/drink');
  Drink.find()
    .exec()
    .then((docs) => {
      res.status(200).json(docs);
    })
    .catch((err) => {
      console.error(err);
      res.status(500).json({ error: err });
    });
});

module.exports = router;

