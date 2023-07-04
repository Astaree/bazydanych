const Picture = require('../models/picture');

async function getPictureById(id) {
    try {
        const picture = await Picture.findById(id);
        return picture;
    } catch (err) {
        return {
            picture: {},
        }
    }
}

module.exports = {
    getPictureById,
}