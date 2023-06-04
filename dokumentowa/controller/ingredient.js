const Ingree = require('../models/ingredient');

//all ingredients functions
async function getIngredients() {
    try {
        const ingredients = await Ingree.find();
        return ingredients;
    } catch (err) {
        return err;
    }

}

async function addIngredient(ing) {
    try {
        const ingredient = await Ingree.create(ing);
        return ingredient;
    } catch (err) {
        return err;
    }
}

async function deleteIngredients() {
    try {
        const ingredients = await Ingree.deleteMany();
        return ingredients;
    } catch (err) {
        return err;
    }
}

//ingredient by id functions
async function getIngredientById(id) {
    try {
        const ingredient = await Ingree.findById(id);
        return ingredient;
    } catch (err) {
        return err;
    }
}

async function updateIngredientById(id, ing) {
    try {
        await Ingree.updateOne({ _id: id }, ing).then(
            (result) => {
                return result;
            }
        );
    } catch (err) {
        return err;
    }
}

async function deleteIngredientById(id) {
    try {
        await Ingree.deleteOne({ _id: id }).then(
            (result) => {
                return result;
            }
        );
    } catch (err) {
        return err;
    }
}


module.exports = {
    getIngredients,
    addIngredient,
    deleteIngredients,
    getIngredientById,
    updateIngredientById,
    deleteIngredientById
}