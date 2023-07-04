const express = require('express');
const router = express.Router();
const Meal = require('../../../controller/meal');

router.get('/', async (req, res) => {
  await Meal.getMeals().then((meals) => {
    res.status(200).json({
      route: "Meals",
      meals: meals
    });
  }
  ).catch((err) => {
    res.status(400).json({
      route: "Meals",
      error: err
    });
  }
  );
});

module.exports = router;