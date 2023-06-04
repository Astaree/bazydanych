const Drink = require('../models/drink');

async function getDrinks() {
    try {
        const drinks = await Drink.find();
        return drinks;
    } catch (err) {
        return err;
    }
}

async function addDrink(drink) {
    try {
        const newDrink = await Drink.create(drink);
        return newDrink;
    } catch (err) {
        return err;
    }
}

async function deleteDrinks() {
    try {
        const drinks = await Drink.deleteMany();
        return drinks;
    } catch (err) {
        return err;
    }
}

async function getDrinkById(id) {
    try {
        const drink = await Drink.findById(id);
        return drink;
    } catch (err) {
        return err;
    }
}

async function updateDrinkById(id, drink) {
    try {
        await Drink.updateOne({ _id: id }, drink).then(
            (result) => {
                return result;
            }
        );
    } catch (err) {
        return err;
    }
}

async function deleteDrinkById(id) {
    try {
        await Drink.deleteOne({ _id: id }).then(
            (result) => {
                return result;
            }
        );
    } catch (err) {
        return err;
    }
}

module.exports = {
    getDrinks,
    addDrink,
    deleteDrinks,
    getDrinkById,
    updateDrinkById,
    deleteDrinkById
}