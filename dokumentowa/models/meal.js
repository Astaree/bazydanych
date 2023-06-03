const mongoose = require('mongoose');
const ingredients = require('./ingredient');
const Picture = require('./picture');

const mealSchema = new mongoose.Schema({
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
        type: ingredients.schema,
        required: true,
    }],
    picture: [{
        type: Picture.schema,
        required: true,
    }],
});

module.exports = mongoose.model('Meal', mealSchema);