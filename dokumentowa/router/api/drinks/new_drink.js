const express = require('express');
const router = express.Router();
const Drink = require('../../../controller/drink');
const drink = require('../../../models/drink');

router.get('/', async (req, res) => {
  res.render('new_drink', {
    title: 'New Drink',
  }
  );
});


router.post('/', async (req, res) => {
  const { name, type, price } = req.body;

  const new_drink = new drink({
    name,
    type,
    price,
  });
  
  try{
    await Drink.addDrink(new_drink).then((result) => {
      console.log(result);
      res.redirect('/api/drinks');
    }
    );
  }
  catch(err){
  }
});


module.exports = router;