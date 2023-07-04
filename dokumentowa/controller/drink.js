const Drink = require('../models/drink');

async function getDrinks() {
    try {
        const drinks = await Drink.find({ isDeleted: false });
        return drinks;
    } catch (err) {
        return {
            drinks: [],
        }
    }
}

async function getDrinkById(id) {
    try {
        const drink = await Drink.findById(id);
        return drink;
    } catch (err) {
        return {
            drink: {},
        }
    }
}

async function addDrink(drink) {
    try {
        await Drink.find({ name: drink.name }).then((drinks) => {
            if (drinks.length > 0) {
                return {
                    info: { "message": "Drink already exists" },
                    drink: {},
                }
            }
        });
        const newDrink = new Drink(drink);
        await newDrink.save();
        return newDrink;
    } catch (err) {
        return {
            drink: {},
        }
    }
}



async function deleteDrinkById(id) {
    try {
        await Drink.findByIdAndUpdate({ _id: id }, { isDeleted: true });
        return {
            info: { "message": "Drink deleted" },
            drink: {},
        }
    } catch (err) {
        return {
            drink: {},
        }
    }
}

async function getDeleted() {
    try {
        const drinks = await Drink.find({ isDeleted: true});
        return drinks;
    } catch (err) {
        return {
            drinks: [],
        }
    }
}

async function deletePern(id) {
    try {
        await Drink.findByIdAndDelete(id);
        return {
            info: { "message": "Drink deleted" },
            drink: {},
        }
    } catch (err) {
        return {
            drink: {},
        }
    }
}



module.exports = {
    getDrinks,
    getDrinkById,
    addDrink,
    deleteDrinkById,
    getDeleted,
    deletePern
}