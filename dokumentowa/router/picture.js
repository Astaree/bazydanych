const express = require('express');
const router = express.Router();

const morgan = require('morgan');

router.get('/', (req, res) => {
    res.status(200).json({
        route:"picture"
    })
});

router.post('/', (req, res) => {

});

router.put('/', (req, res) => {

});

router.delete('/', (req, res) => {

});

router.get('/:id', (req, res) => {

});

router.post('/:id', (req, res) => {

});

router.put('/:id', (req, res) => {

});

router.delete('/:id', (req, res) => {

});

module.exports = router;
