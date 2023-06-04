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

async function addOrder(order) {
    let newOrder = new Order({
        client: order.client,
        meal: order.meal,
        delivery: order.delivery,
        price: order.price,
        date: order.date,
        status: order.status,
    });

    try {
        await newOrder.save((err, order) => {
            if (err) {
                return err;
            }
            else {
                return order;
            }
        });
    }
    catch (err) {
        return err;
    }
}

    module.exports = {
        getOrders,
        addOrder,
    }