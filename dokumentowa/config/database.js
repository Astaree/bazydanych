const mongoose = require('mongoose');

function connectToDatabase(url) {
    mongoose.connect(url, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    });
    const db = mongoose.connection;
    db.on('error', console.error.bind(console, 'Connection error:'));
    db.once('open', () => {
        console.log('Connected to the database');
    });
    
    return db;
}


module.exports = {
    connectToDatabase,
};