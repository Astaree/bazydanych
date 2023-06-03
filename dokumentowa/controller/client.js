const mongoose = require('mongoose');
const Client = require('../model/client');


async function getClients(req, res) {
    await Client.find().exec().then((x) => {
        if (x.length > 0) {
            res.status(200).send(x);
        } else {
            res.status(204).send();
        }
    }).catch((err) => {
        console.log(err);
    });
}

function getClient(req, res) {
    Client.findById(req.params.id)
        .exec()
        .then((x) => res.status(200).send(x));
}

function postClient(req, res) {
    Client.create(req.body).then((x) => res.status(201).send(x));
}

function putClient(req, res) {
    Client.findOneAndUpdate(req.params.id, req.body)
        .then(() => res.sendStatus(204));
}

function deleteClient(req, res) {
    Client.findOneAndDelete(req.params.id).exec().then(() => res.sendStatus(204));
}

module.exports = {
    getClients,
    getClient,
    postClient,
    putClient,
    deleteClient
}