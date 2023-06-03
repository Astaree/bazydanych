const express = require('express');
const router = express.Router();
const Meal = require('../controller/meal');

router.get('/', async (req, res) => {
    mongoose.connection.useDb('Meal');
    let meals = Meal.getMeals();
    res.status(200).json({
        route: "meal",
        meals: meals
    });
});

router.post('/', async (req, res) => {

});

router.put('/', async (req, res) => {

});

router.delete('/', async (req, res) => {

});

router.get('/:id', async (req, res) => {

});

router.post('/:id', async (req, res) => {

});

router.put('/:id', async (req, res) => {

});

router.delete('/:id', async (req, res) => {

});

module.exports = router;
