const express = require('express');
const router = express.Router();
const meal = require('../../../models/meal');

router.get('/', async (req, res) => {
  res.render('new_meal', {
    title: 'New Meal',
  });
});

router.post('/', async (req, res) => {
  const { name, description, price,averageTimeToCook } = req.body;
  const ingre = [];
  console.log(req.body);

  const ingredients = Object.keys(req.body)
  .filter(key => key.startsWith('ingredients['))
  .map(key => {
    const match = key.match(/ingredients\[(\d+)\]\[(\w+)\]/);
    const index = Number(match[1]);
    const property = match[2];
    return { index, property, value: req.body[key] };
  })
  .reduce((acc, { index, property, value }) => {
    if (!acc[index]) {
      acc[index] = {};
    }
    acc[index][property] = value;
    return acc;
  }, []);
  console.log(ingredients);

  const newMeal = new meal({
    name,
    description,
    price,
    averageTimeToCook,
    ingredients,
  });

  try {
    const savedMeal = await newMeal.save();
    res.redirect('/api/meals');
  }
  catch (err) {
    res.status(400).json({ message: err.message });
  }
});


module.exports = router;