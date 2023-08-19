const express = require('express');
const router = express.Router();
const delivery = require('../../../models/delivery');

router.get('/', async (req, res) => {
  try {
    const deliveries = await delivery.find();
    res.render('deliveries', { deliveries });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.get('/:id', async (req, res) => {
  try {
    const delivery = await delivery.findById(req.params.id).populate('order');
    if (!delivery) {
      return res.status(404).json({ message: 'Delivery not found' });
    }

    res.json(delivery);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});






module.exports = router;