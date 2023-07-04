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

async function getOrderById(id) {
    try {
        const order = await Order.findById(id);
        return order;
    } catch (err) {
        return {
            order: {},
        }
    }
}

async function addOrder(order) {
    try {
        const newOrder = new Order(order);
        await newOrder.save();
        return newOrder;
    } catch (err) {
        return {
            order: {},
        }
    }
}


module.exports = {
    getOrders,
    getOrderById,
    addOrder,
}