const express = require('express');
const router = express.Router();
const Drink = require('../../../controller/drink');

router.get('/', async (req, res) => {
  await Drink.getDeleted().then((drinks) => {
    res.status(200).json({
      route: "Drinks",
      drinks: drinks
    });
  }
  ).catch((err) => {
    res.status(400).json({
      route: "Drinks",
      error: err
    });
  }
  );
});

router.delete('/:id', async (req, res) => {
  await Drink.deletePern(req.params.id).then((drink) => {
    res.status(200).json({
      route: "Drinks",
      drink: drink
    });
  }
  ).catch((err) => {
    res.status(400).json({
      route: "Drinks",
      error: err
    });
  }
  );
});

module.exports = router;