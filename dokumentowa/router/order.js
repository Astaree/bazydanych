const express = require('express');
const router = express.Router();
const Order = require('../controller/order');

router.get('/', async (req, res) => {
    let orders = Order.getOrders();
    res.status(200).json({
        route: "order",
        orders: orders
    });
});

router.post('/', async (req, res) => {

});

router.put('/', async (req, res) => {

});

router.delete('/', async (req, res) => {

});

router.get('/:id', async (req, res) => {

});

router.post('/:id', async (req, res) => {

});

router.put('/:id', async (req, res) => {

});

router.delete('/:id', async (req, res) => {

});

module.exports = router;
