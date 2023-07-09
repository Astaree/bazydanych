const mongoose = require('mongoose');

const pictureSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
    },
    picture: {
        type: String,
        required: true,
    },
});

module.exports = mongoose.model('Picture', pictureSchema);