const mongoose = require('mongoose');


function connectToDatabase(url) {
    mongoose.connect(url, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    });
    const db = mongoose.connection;
    db.once('open', () => console.log('Connected to database'));
    db.on('error', (err) => console.log('Error', err));

    return db;
}


module.exports = {
    connectToDatabase,
};