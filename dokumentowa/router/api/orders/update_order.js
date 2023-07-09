const express = require('express');
const router = express.Router();
const Order = require('../../../models/order');

router.get('/:id', async (req, res) => {
  try {
    const order = await Order.findById(req.params.id);
    res.render('update_order', { order });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.post('/:id', async (req, res) => {
  const { clientName, clientAddress, clientPhoneNumber, clientEmail, dateOfDelivery, state } = req.body;

  try {
    // Check if the order exists
    const existingOrder = await Order.findById(req.params.id);
    if (!existingOrder) {
      return res.status(404).json({ message: 'Order not found' });
    }

    // Update the order details
    existingOrder.client.name = clientName;
    existingOrder.client.address = clientAddress;
    existingOrder.client.phoneNumber = clientPhoneNumber;
    existingOrder.client.email = clientEmail;
    existingOrder.state = state;
    const updatedOrder = await existingOrder.save();

    res.redirect('/api/orders');
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;
