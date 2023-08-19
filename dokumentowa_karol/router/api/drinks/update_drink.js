const express = require('express');
const router = express.Router();
const Drink = require('../../../models/drink');

router.get('/:id', async (req, res) => {
  try {
    const drink = await Drink.findById(req.params.id);
    res.render('update_drink', { drink });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.post('/:id', async (req, res) => {
  const { name, type, price } = req.body;

  try {
    // Check if the drink exists
    const existingDrink = await Drink.findById(req.params.id);
    if (!existingDrink) {
      return res.status(404).json({ message: 'Drink not found' });
    }

    // Update the drink details
    existingDrink.name = name;
    existingDrink.type = type;
    existingDrink.price = price;
    const updatedDrink = await existingDrink.save();

    res.redirect('/api/drinks');
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;
