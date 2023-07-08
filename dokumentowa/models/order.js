const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema({
    //ref to client
    client: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Client',
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
    //date of order
    dateOfOrder: {
        type: Date,
        required: true,
    },
    //date when order client want to get
    dateOfDelivery: {
        type: Date,
        required: true,
    },
    //status of order
    status: {
        type: String,
        required: true,
    },
});

module.exports = mongoose.model('Order', orderSchema);
