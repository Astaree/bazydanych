const mongoose = require('mongoose');

const restaurantSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
    },
    address: {
        type: String,
    },
    phone: {
        type: String,
    },
    email: {
        type: String,
    },
    openHours: {
        type: String,
    },
  });

module.exports = mongoose.model('Restaurant', restaurantSchema);