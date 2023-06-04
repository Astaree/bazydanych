const Meal = require('../models/meal');

async function getMeals() {
    try {
        const meals = await Meal.find();
        return meals;
    }
    catch (err) {
        return { message: err };
    }
}

async function addMeal(meal) {
    let pictures = [];
    let picturesB64 = [];
    if (meal.pictures) {
        pictures = meal.pictures;
    }
    pictures.forEach(picture => {
        picturesB64.push(picture.toString('base64'));
    });

    const newMeal = new Meal({
        name: meal.name,
        description: meal.description,
        averageTimeToCook: meal.averageTimeToCook,
        price: meal.price,
        ingredients: meal.ingredients,
    });

    try {
        await newMeal.save((err, meal) => {
            if (err) {
                return { message: err };
            }
            else {
                return meal;
            }
        });
    }
    catch (err) {
        return { message: err };
    }
}

async function deleteMeals() {
    try {
        const meals = await Meal.deleteMany();
        return meals;
    }
    catch (err) {
        return { message: err };
    }
}

async function getMealById(id) {
    try {
        const meal = await Meal.findById(id).populate('ingredients').populate('picture').exec();
        return meal;
    }
    catch (err) {
        return { message: err };
    }
}

async function getMealByName(name) {
    try {
        const meal = await Meal.findOne({ name: name }).populate('ingredients').populate('picture').exec();
        return meal;
    }
    catch (err) {
        return { message: err };
    }
}

async function updateMeal(id, meal) {
    try {
        const updatedMeal = await Meal.updateOne({ _id: id }, {
            $set: {
                name: meal.name,
                description: meal.description,
                averageTimeToCook: meal.averageTimeToCook,
                price: meal.price,
                ingredients: meal.ingredients,
            }
        });
        return updatedMeal;
    }
    catch (err) {
        return { message: err };
    }
}

async function deleteMealById(id) {
    try {
        const meal = await Meal.deleteOne({ _id: id });
        return meal;
    }
    catch (err) {
        return { message: err };
    }
}

module.exports = {
    getMeals,
    getMealById,
    getMealByName,
    
    addMeal,
    updateMeal,
    deleteMeals,
    deleteMealById
};

