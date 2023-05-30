const { MongoClient } = require('mongodb');

const url = 'mongodb://localhost:27017'; // Replace with your MongoDB connection string
const dbName = 'mydatabase'; // Replace with your database name

// Connect to MongoDB
const connectToDatabase = async () => {
    try {
        const client = new MongoClient(url);
        await client.connect();
        console.log('Connected to the database');

        return client.db(dbName);
    } catch (error) {
        console.error('Failed to connect to the database', error);
        process.exit(1);
    }
};


module.exports = connectToDatabase;