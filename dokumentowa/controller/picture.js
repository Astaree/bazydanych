const Picture = require('../models/picture');

async function getPictures() {
    try {
        const pictures = await Picture.find();
        return pictures;
    } catch (err) {
        return {
            pictures: [],
        }
    }
}

exports.default = {
    getPictures,
}