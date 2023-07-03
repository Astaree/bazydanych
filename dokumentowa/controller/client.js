const Client = require('../models/client');
const { $or, $not } = require('mongoose').Types.ObjectId;


async function getClients() {
    try {
        const clients = await Client.find($not[{ isDeleted: true }]);
        return clients;
    } catch (err) {
        return {
            clients: [],
        }
    }

}

async function getClientById(id) {
    try {
        const client = await Client.findById(id);
        return client;
    } catch (err) {
        return {
            client: {},
        }
    }
}

async function addClient(client) {
    try {
        await Client.find($or[{ email: client.email }, { phoneNumber: client.phoneNumber }]).then((clients) => {
            if (clients.length > 0) {
                return {
                    info: { "message": "Client already exists" },
                    client: {},
                }
            }
        });
        const newClient = new Client(client);
        await newClient.save();
        return newClient;
    } catch (err) {
        return {
            client: {},
        }
    }
}

async function deleteClient(id) {
    try {
        await Client.findByIdAndUpdate({ _id: id }, { isDeleted: true });
        return {
            info: { "message": "Client deleted" },
            client: {},
        }
    } catch (err) {
        return {
            client: {},
        }
    }
}

async function getDeleted() {
    try {
        const clients = await Client.find();
        return clients;
    } catch (err) {
        return {
            clients: [],
        }
    }
}
module.exports = {
    getClients,
    getClientById,
    addClient,
    deleteClient,
    getDeleted,
}