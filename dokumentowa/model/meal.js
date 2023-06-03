const mongoose = require('mongoose');
const ingredientSchema = require('./ingredient');
const Picture = require('./picture');

const mealSchema = new mongoose.Schema({
    _id: mongoose.Schema.Types.ObjectId,
    name: {
        type: String,
        required: true,
    },
    description: {
        type: String,
    },
    averageTimeToCook: {
        type: Number,
        required: true,
    },
    price: {
        type: Number,
        required: true,
    },
    ingredients: [{
        type: ingredientSchema.Schema,
        required: true,
    }],
    picture: [{
        type: Picture.Schema,
        required: true,
    }],
});

module.exports = mongoose.model('Meal', mealSchema);