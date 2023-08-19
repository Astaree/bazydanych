const express = require('express');
const router = express.Router();
const order = require('../../../models/order');

router.get('/', async (req, res) => {
  try {
    const orders = await order.find()
      .populate({
        path: 'client',
        model: 'Client',
      })
      .populate({
        path: 'drinks.drink',
        model: 'Drink',
      })
      .populate({
        path: 'meals.meal',
        model: 'Meal',
      });

    res.render('orders', { orders });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;