const Order = require('../models/order');

async function getOrders() {
    try {
        const orders = await Order.find();
        return orders;
    } catch (err) {
        return {
            orders: [],
        }
    }
}

module.exports = {
    getOrders,
}