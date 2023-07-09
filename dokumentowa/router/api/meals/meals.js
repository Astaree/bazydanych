const express = require('express');
const router = express.Router();
const meal = require('../../../models/meal');

router.get('/', async (req, res) => {
    try {
        const meals = await meal.find();
        console.log(meals);
        res.render('meals', { meals: meals });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

module.exports = router;