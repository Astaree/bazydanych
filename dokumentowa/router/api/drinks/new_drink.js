const express = require('express');
const router = express.Router();
const drink = require('../../../models/drink');

router.get('/', async (req, res) => {
  res.render('new_drink', {
    title: 'New Drink',
  });
});


router.post('/', async (req, res) => {
  const { name, type, price,  } = req.body;
  
  const new_drink = new drink({
    name: name,
    type: type,
    price: price,
  });

  try {
    const existingDrink = await drink.findOne({ name: name });
    if (existingDrink) {
      console.log('Drink already exists');
      res.redirect('/api/new_drink');
    } else {
      await new_drink.save();
      res.redirect('/api/drinks');
    }
  } catch (err) {
    console.log(err);
    res.redirect('/api/new_drink');
  }
});


module.exports = router;