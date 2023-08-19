const dotenv = require('dotenv');

function imortEnv() {
    dotenv.config();
    return process.env;
}

module.exports = {
    imortEnv,
};