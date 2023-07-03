const express = require('express');
const router = express.Router();
const Client = require('../controller/client');


//get all ingredients
router.get('/', async (req, res) => {
    await Client.getClients().then((clients) => {
        res.status(200).json({
            route: "Clients",
            clients: clients
        });
    }
    ).catch((err) => {
        res.status(400).json({
            route: "Clients",
            error: err
        });
    }
    );
});

router.get('/:id', async (req, res) => {
    await Client.getClientById(req.params.id).then((client) => {
        res.status(200).json({
            route: "Clients",
            client: client
        });
    }
    ).catch((err) => {
        res.status(400).json({
            route: "Clients",
            error: err
        });
    }
    );
});

router.post('/', async (req, res) => {
    await Client.addClient(req.body).then((client) => {
        res.status(200).json({
            route: "Clients",
            client: client
        });
    }
    ).catch((err) => {
        res.status(400).json({
            route: "Clients",
            error: err
        });
    }
    );
});

router.delete('/:id', async (req, res) => {
    await Client.deleteClient(req.params.id).then((client) => {
        res.status(200).json({
            route: "Clients",
            client: client
        });
    }
    ).catch((err) => {
        res.status(400).json({
            route: "Clients",
            error: err
        });
    }
    );
});


module.exports = router;
