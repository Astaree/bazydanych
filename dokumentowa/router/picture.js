const express = require('express');
const router = express.Router();
const Picture = require('../controller/picture');

router.get('/', async (req, res) => {
    let pictures = Picture.getPictures();
    res.status(200).json({
        route: "picture",
        pictures: pictures
    });
});

router.post('/', async (req, res) => {

});

router.put('/', async (req, res) => {

});

router.delete('/', async (req, res) => {

});

router.get('/:id', async (req, res) => {

});

router.post('/:id', async (req, res) => {

});

router.put('/:id', async (req, res) => {

});

router.delete('/:id', async (req, res) => {

});

module.exports = router;
