const mongoose = require('mongoose');

const deliverySchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
    },
    company: {
        type: String,
        required: true,
    },
    order: {
        type: Number,
        required: true,
    },
});

module.exports = mongoose.model('Delivery', deliverySchema);