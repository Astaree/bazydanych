const express = require('express');
const router = express.Router();
const Meal = require('../../../models/meal');

router.get('/:id', async (req, res) => {
  try {
    const deletedMeal = await Meal.findByIdAndRemove(req.params.id);
    if (!deletedMeal) {
      return res.status(404).json({ message: 'Meal not found' });
    }

    res.redirect('/api/meals');
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;
