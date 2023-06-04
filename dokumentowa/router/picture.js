const express = require('express');
const router = express.Router();
const Picture = require('../controller/picture');

//--------------------Picture--------------------
//
//
//              FOR NOW ABAONDONED
//
//
//--------------------Picture--------------------

//get all pictures
router.get('/', async (req, res) => {
    try {
        const pictures = await Picture.getPictures();
        res.json(pictures);
    } catch (err) {
        res.json({ message: err });
    }
});

//crates a new picture
router.post('/', async (req, res) => {
    try {
        const picture = await Picture.addPicture(req.body);
        res.json(picture);
    } catch (err) {
        res.json({ message: err });
    }
});

//delete all pictures
router.delete('/', async (req, res) => {
    try {
        const pictures = await Picture.deletePictures();
        res.json(pictures);
    } catch (err) {
        res.json({ message: err });
    }
});

//get picture by id
router.get('/:id', async (req, res) => {
    try {
        const picture = await Picture.getPictureById(req.params.id);
        res.json(picture);
    } catch (err) {
        res.json({ message: err });
    }
});

//delete an picture by id
router.put('/:id', async (req, res) => {
    try {
        const picture = await Picture.updatePictureById(req.params.id, req.body);
        res.json(picture);
    } catch (err) {
        res.json({ message: err });
    }
});

//delete an picture by id
router.delete('/:id', async (req, res) => {
    try {
        const picture = await Picture.deletePictureById(req.params.id);
        res.json(picture);
    } catch (err) {
        res.json({ message: err });
    }
});

module.exports = router;
