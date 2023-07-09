const mongoose = require('mongoose');
const client = require('./client');

const orderSchema = new mongoose.Schema({
    //embeded client
    client: {
        type: client.schema,
        required: true,
    },
    //ref to drinks
    drinks: [{
        quantity: Number,
        drink: {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'Drink',
            required: true,
        }
    }],
    //ref to meal
    meals: [
        {
            quantity: Number,
            meal:
            {
                type: mongoose.Schema.Types.ObjectId,
                ref: 'Meal',
                required: true,
            }
        }
    ],
    //status of order
    state: {
        type: String,
        required: true,
    },
});

module.exports = mongoose.model('Order', orderSchema);
