const express = require('express');
const router = express.Router();
const Order = require('../../../models/order');

router.get('/:id', async (req, res) => {
  try {
    const deletedOrder = await Order.findByIdAndRemove(req.params.id);
    if (!deletedOrder) {
      return res.status(404).json({ message: 'Order not found' });
    }

    res.redirect('/api/orders');
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;
