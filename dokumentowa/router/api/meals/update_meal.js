const express = require('express');
const router = express.Router();
const Meal = require('../../../models/meal');

router.get('/:id', async (req, res) => {
  try {
    const meal = await Meal.findById(req.params.id);
    res.render('update_meal', { meal });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.post('/:id', async (req, res) => {
  const { name, description, averageTimeToCook, price } = req.body;

  try {
    // Check if the meal exists
    const existingMeal = await Meal.findById(req.params.id);
    if (!existingMeal) {
      return res.status(404).json({ message: 'Meal not found' });
    }

    // Update the meal details
    existingMeal.name = name;
    existingMeal.description = description;
    existingMeal.averageTimeToCook = averageTimeToCook;
    existingMeal.price = price;
    const updatedMeal = await existingMeal.save();

    res.redirect('/api/meals');
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;
