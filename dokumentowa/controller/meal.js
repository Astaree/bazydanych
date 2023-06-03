const Meal = require('../models/meal');

async function getMeals() {
    try {
        const meals = await Meal.find();
        return meals;
    } catch (err) {
        return {
            meals: [],
        }
    }
}

exports.default = {
    getMeals,
}