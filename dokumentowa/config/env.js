const dotenv = require('dotenv');
const morgan = require('morgan');

function imortEnv() {
    dotenv.config();
    return process.env;
}

module.exports = {
    imortEnv,
};