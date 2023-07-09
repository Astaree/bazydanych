const express = require('express');
const router = express.Router();
const Deliveries  = require('../../../models/delivery');
const Order = require('../../../models/order');

router.get('/', async (req, res) => {
  try {
    const undeliveredOrders = await Order.find({ delivery: { $exists: false } });
    res.render('new_delivery', { orders: undeliveredOrders });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.post('/', async (req, res) => {
  const { name, company, order } = req.body;
  try {
    // Check if the order exists and doesn't belong to any delivery
    const existingOrder = await Order.findOne({ _id: order, delivery: { $exists: false } });
    if (!existingOrder) {
      return res.status(404).json({ message: 'Invalid or already delivered order' });
    }

    // Create a new delivery
    const newDelivery = new Deliveries({
      name,
      company,
      order,
    });
    // Save the delivery
    const savedDelivery = await newDelivery.save();

    // Update the order with the delivery information
    existingOrder.delivery = savedDelivery._id;
    await existingOrder.save();

    res.redirect('/api/deliveries');
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});


module.exports = router;