const express = require('express');
const router = express.Router();
const order = require('../../../models/order');
const Drink = require('../../../models/drink');
const Meal = require('../../../models/meal');

router.get('/', async (req, res) => {
  try {
    const drinks = await Drink.find();
    const meals = await Meal.find();
    res.render('new_order', { drinks, meals });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});



router.post('/', async (req, res) => {
  const tempDrinks = [];
  const tempMeals = [];

  const { newClientName, newClientAddress, newClientPhoneNumber, newClientEmail, dateOfDelivery, state } = req.body;

  try {
    for (const key in req.body) {
      if (key.startsWith('drinks[')) {
        const drinkId = key.match(/\[(.*?)\]/)[1];
        const tempDrink = await Drink.findById(drinkId);
        tempDrinks.push({
          quantity: req.body[key],
          drink: tempDrink._id,
        });
      }

      if (key.startsWith('meals[')) {
        const mealId = key.match(/\[(.*?)\]/)[1];
        const tempMeal = await Meal.findById(mealId);
        tempMeals.push({
          quantity: req.body[key],
          meal: tempMeal._id,
        });
      }
    }
    tempDrinks.forEach(drink => {
      if (drink.quantity == 0) {
        const index = tempDrinks.indexOf(drink);
        tempDrinks.splice(index, 1);
      }
    });

    tempMeals.forEach(meal => {
      if (meal.quantity == 0) {
        const index = tempMeals.indexOf(meal);
        tempMeals.splice(index, 1);
      }
    });

    const client = {
      name: newClientName,
      address: newClientAddress,
      phoneNumber: newClientPhoneNumber,
      email: newClientEmail,
    };

    console.log(client);

    const newOrder = new order({
      client: {
        name: newClientName,
        address: newClientAddress,
        phoneNumber: newClientPhoneNumber,
        email: newClientEmail,
      },
      drinks: tempDrinks,
      meals: tempMeals,
      state,
    });
    
    await newOrder.save();

    res.redirect('/api/orders');
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;