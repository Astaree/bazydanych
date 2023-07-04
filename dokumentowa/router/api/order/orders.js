const express = require('express');
const router = express.Router();
const Order = require('../../../controller/order');


router.get('/', async (req, res) => {
  await Order.getOrders().then((orders) => {
    res.status(200).json({
      route: "Orders",
      orders: orders
    });
  }
  ).catch((err) => {
    res.status(400).json({
      route: "Orders",
      error: err
    });
  }
  );
});

router.get('/:id', async (req, res) => {
  await Order.getOrderById(req.params.id).then((order) => {
    res.status(200).json({
      route: "Orders",
      order: order
    });
  }
  ).catch((err) => {
    res.status(400).json({
      route: "Orders",
      error: err
    });
  }
  );
});

router.post('/', async (req, res) => {
  await Order.addOrder(req.body).then((order) => {
    res.status(200).json({
      route: "Orders",
      order: order
    });
  }
  ).catch((err) => {
    res.status(400).json({
      route: "Orders",
      error: err
    });
  }
  );
});

module.exports = router;
