const Client = require('../models/client');


async function getClients() {
    try {
        const clients = await Client.find();
        return clients;
    } catch (err) {
        return err;
    }
}

async function addClient(client) {
    try {
        const newClient = await Client.create(client);
        return newClient;
    } catch (err) {
        return err;
    }
}

async function deleteClients() {
    try {
        const clients = await Client.deleteMany();
        return clients;
    } catch (err) {
        return err;
    }
}

async function getClientById(id) {
    try {
        const client = await Client.findById(id);
        return client;
    } catch (err) {
        return err;
    }
}

async function updateClientById(id, client) {
    try {
        await Client.updateOne({ _id: id }, client).then(
            (result) => {
                return result;
            }
        );
    } catch (err) {
        return err;
    }
}

async function deleteClientById(id) {
    try {
        await Client.deleteOne({ _id: id }).then(
            (result) => {
                return result;
            }
        );
    } catch (err) {
        return err;
    }
}

module.exports = {
    getClients,
    addClient,
    deleteClients,
    getClientById,
    updateClientById,
    deleteClientById
}