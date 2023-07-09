const mongoose = require('mongoose');

const clientSchema = new mongoose.Schema({
    name: {
        type: String,
    },
    address: {
        type: String,
    },
    phoneNumber: {
        type: String,
    },
    email: {
        type: String,
    },
});

module.exports = mongoose.model('Client', clientSchema);