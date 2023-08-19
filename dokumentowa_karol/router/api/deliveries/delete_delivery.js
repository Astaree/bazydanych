const express = require('express');
const router = express.Router();
const Delivery = require('../../../models/delivery');



router.get('/:id', async (req, res) => {
  console.log(req.params.id);
  try {
    const deletedDelivery = await Delivery.findByIdAndRemove(req.params.id);
    if (!deletedDelivery) {
      return res.status(404).json({ message: 'Delivery not found' });
    }

    res.redirect('/api/deliveries');
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;