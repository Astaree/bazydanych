const express = require('express');
const router = express.Router();
const Delivery = require('../../../models/delivery');
const Order = require('../../../models/order');

router.get('/:id', async (req, res) => {
  try {
    const delivery = await Delivery.findById(req.params.id);
    const orders = await Order.find();
    res.render('update_delivery', { delivery, orders });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.post('/:id', async (req, res) => {
  const { name, company, order } = req.body;
  console.log(req.body);
  try {
    // Check if the delivery exists
    const existingDelivery = await Delivery.findById(req.params.id);
    if (!existingDelivery) {
      return res.status(404).json({ message: 'Delivery not found' });
    }

    // Check if the order exists and doesn't belong to any other delivery
    const existingOrder = await Order.findOne({ _id: order, delivery: { $ne: req.params.id } });
    if (!existingOrder) {
      return res.status(404).json({ message: 'Invalid or already assigned order' });
    }

    // Update the delivery details
    existingDelivery.name = name;
    existingDelivery.company = company;
    existingDelivery.order = order;
    const updatedDelivery = await existingDelivery.save();

    res.redirect('/api/deliveries');
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});


module.exports = router;
