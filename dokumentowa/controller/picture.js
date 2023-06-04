const Picture = require('../models/picture');

async function getPictures() {
    try {
        const pictures = await Picture.find();
        return pictures;
    } catch (err) {
        return err;
    }
}

async function addPicture(pic) {
    try {
        const picture = await Picture.create(pic);
        return picture;
    } catch (err) {
        return err;
    }
}

async function deletePictures() {
    try {
        const pictures = await Picture.deleteMany();
        return pictures;
    } catch (err) {
        return err;
    }
}

async function getPictureById(id) {
    try {
        const picture = await Picture.findById(id);
        return picture;
    } catch (err) {
        return err;
    }
}

async function updatePictureById(id, pic) {
    try {
        await Picture.updateOne({ _id: id }, pic).then(
            (result) => {
                return result;
            }
        );
    } catch (err) {
        return err;
    }
}   

async function deletePictureById(id) {
    try {
        await Picture.deleteOne({ _id: id }).then(
            (result) => {
                return result;
            }
        );
    } catch (err) {
        return err;
    }
}

module.exports = {
    getPictures,
    addPicture,
    deletePictures,
    getPictureById,
    updatePictureById,
    deletePictureById
}