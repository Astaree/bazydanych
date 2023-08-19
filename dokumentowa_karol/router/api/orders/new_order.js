const express = require('express');
const router = express.Router();
const order = require('../../../models/order');
const Client = require('../../../models/client');
const Drink = require('../../../models/drink');
const Meal = require('../../../models/meal');
const { Timestamp } = require('mongodb');

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

  const { 
    newClientName, 
    newClientAddress,
    newClientPhoneNumber, 
    newClientEmail,
    dateOfDelivery,
    state } = req.body;

    // to zostaje to samo
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

    //get client if not exists create new one
    const client = new Client({
      name: newClientName,
      address: newClientAddress,
      phoneNumber: newClientPhoneNumber,
      email: newClientEmail,
    });

    const exists = await Client.find({ $or: [{ phoneNumber: newClientPhoneNumber }] });
    
    if (exists.length > 0) {
      client._id = exists[0]._id;
    } else {
      await client.save();
    }

    const newOrder = new order({
      client: client._id,
      drinks: tempDrinks,
      meals: tempMeals,
      dateOfDelivery: Timestamp(new Date().getTime()),
      state,
    });
    
    await newOrder.save();
    res.redirect('/api/orders');

  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;