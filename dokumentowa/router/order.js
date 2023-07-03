const express = require('express');
const router = express.Router();
const Order = require('../controller/order');


router.get('/', async (req, res) => {
    try {
        const orders = await Order.getOrders();
        res.status(200).json({
            route: "Orders",
            orders: orders
        });
    } catch (err) {
        res.status(400).json({
            route: "Orders",
            error: err
        });
    }
});

router.get('/:id', async (req, res) => {
    try {
        const order = await Order.getOrder(req.params.id);
        res.status(200).json({
            route: "Orders",
            orders: order
        });
    } catch (err) {
        res.status(400).json({
            route: "Orders",
            error: err
        });
    }
});

router.post('/', async (req, res) => {
    try {
        const order = await Order.addOrder(req.body);
        res.status(200).json({
            route: "Orders",
            orders: order
        });
    } catch (err) {
        res.status(400).json({
            route: "Orders",
            error: err
        });
    }
});

module.exports = router;
