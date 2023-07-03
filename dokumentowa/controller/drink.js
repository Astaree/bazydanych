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


async function getDrinkById(id) {
    try {
        const drink = await Drink.findById(id);
        return drink;
    } catch (err) {
        return err;
    }
}

async function deleteDrinkById(id) {
    try {
        await Drink.findByIdAndUpdate(id, { isDeleted: true });
    } catch (err) {
        return err;
    }
}

module.exports = {
    getDrinks,
    addDrink,
    getDrinkById,
    deleteDrinkById
}