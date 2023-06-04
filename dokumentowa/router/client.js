const express = require('express');
const router = express.Router();
const Client = require('../controller/client');


//get all ingredients
router.get('/', async (req, res) => {
    await Client.getClients().then((client) => {
        res.status(200).json({
            route: "Clients",
            clients: client
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Clients",
            error: err
        });
    });
});

//crates a new ingredient
router.post('/', async (req, res) => {
    await Client.addClient(req.body).then((client) => {
        res.status(201).json({
            route: "Clients",
            client: client
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Clients",
            error: err
        });
    });
});

//delete all ingredients
router.delete('/', async (req, res) => {
    await Client.deleteClients().then(() => {
        res.status(200).json({
            route: "Clients",
            clients: []
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Clients",
            error: err
        });
    }
    );
});

//get ingredient by id
router.get('/:id', async (req, res) => {
    await Client.getClientById(req.params.id).then((client) => {
        res.status(200).json({
            route: "Clients",
            client: client
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Clients",
            error: err
        });
    });
});

//delete an ingredient by id
router.put('/:id', async (req, res) => {
    await Client.updateClientById(req.params.id, req.body).then((client) => {
        res.status(200).json({
            route: "Clients",
            client: client
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Clients",
            error: err
        });
    });
});

//delete an ingredient by id
router.delete('/:id', async (req, res) => {
    await Client.deleteClientById(req.params.id).then((client) => {
        res.status(200).json({
            route: "Clients",
            client: client
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Clients",
            error: err
        });
    });
});

module.exports = router;
