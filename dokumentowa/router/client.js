const express = require('express');
const router = express.Router();
const Client = require('../controller/client');

const morgan = require('morgan');

router.get('/', async (req, res) => {
    let clients = Client.getClients(req, res);
    res.status(200).json({
        route: "client",
        clients: clients
    })
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
