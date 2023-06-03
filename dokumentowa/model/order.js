const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema({
    _id: mongoose.Schema.Types.ObjectId,
    client: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Client',
        required: true,
    },
    drink: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Drink',
        required: true,
    }],
    meal: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Meal',
        required: true,
    }],
});

module.exports = mongoose.model('Order', orderSchema);
