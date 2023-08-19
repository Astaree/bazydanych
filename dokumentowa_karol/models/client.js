const mongoose = require('mongoose');
const opinion = require('./opinion');

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
    opinion: [{
        type: opinion.schema,
        ref: 'Opinion',
        required: false,
    }],
});

module.exports = mongoose.model('Client', clientSchema);