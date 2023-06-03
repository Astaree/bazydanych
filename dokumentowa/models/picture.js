const mongoose = require('mongoose');

const pictureSchema = new mongoose.Schema({
    _id: mongoose.Schema.Types.ObjectId,
    name: {
        type: String,
        required: true,
    },
    picture: {
        type: Buffer,
        required: true,
    },
});

module.exports = mongoose.model('Picture', pictureSchema);