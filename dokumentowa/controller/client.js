const Client = require('../models/client');


async function getClients() {
    try{
    const clients = await Client.find();
    return clients;
    } catch (err) { 
        return {
            clients: [],
        }
    }
}

function getClient(req, res) {
}

function postClient(req, res) {
}

function putClient(req, res) {
}

function deleteClient(req, res) {
}

module.exports = {
    getClients,
    getClient,
    postClient,
    putClient,
    deleteClient
}
