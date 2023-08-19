const mongoose = require('mongoose');

const opinionSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
    },
    opinion: {
        type: String,
        required: true,
    },
    rating: {
        type: Number,
        required: true,
    },
});

module.exports = mongoose.model('Opinion', opinionSchema);