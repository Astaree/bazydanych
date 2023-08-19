const express = require('express');
const router = express.Router();
const Drink = require('../../../models/drink');

router.get('/:id', async (req, res) => {
  try {
    const deletedDrink = await Drink.findByIdAndRemove(req.params.id);
    if (!deletedDrink) {
      return res.status(404).json({ message: 'Drink not found' });
    }

    res.redirect('/api/drinks');
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;
