const Drink = require('../models/drink');

async function getDrinks() {
    try {
        const drinks = await Drink.find();
        return drinks;
    } catch (err) {
        return {
            drinks: [],
        }
    }
}

module.exports = {
    getDrinks
}