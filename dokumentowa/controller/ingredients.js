const Ingree = require('../models/ingredients');

async function getIngredients() {
    try {
        const ingredients = await Ingree.find();
        return ingredients;
    } catch (err) {
        return {
            ingredients: [],
        }
    }
}

exports.default = {
    getIngredients,
}