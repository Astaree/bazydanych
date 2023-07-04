const express = require('express');
const router = express.Router();
const Order = require('../../../controller/order');

router.get('/', async (req, res) => {
  res.render('new_order', {
    title: 'New Order',
  }
  );
});

router.post('/', async (req, res) => {

});

module.exports = router;
