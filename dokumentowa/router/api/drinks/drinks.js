const express = require('express');
const router = express.Router();
const Drink = require('../../../controller/drink');


//get all drinks
router.get('/', async (req, res) => {
    try {
        const drinks = await Drink.getDrinks();
        res.status(200).json({
            route: "Drinks",
            drinks: drinks
        });
    } catch (err) {
        res.status(400).json({
            route: "Drinks",
            error: err
        });
    }
});

router.get('/:id', async (req, res) => {
    try {
        const drink = await Drink.getDrink(req.params.id);
        res.status(200).json({
            route: "Drinks",
            drinks: drink
        });
    } catch (err) {
        res.status(400).json({
            route: "Drinks",
            error: err
        });
    }
});



//crates a new drink
router.post('/', async (req, res) => {
    try {
        const drink = await Drink.addDrink(req.body);
        res.status(200).json({
            route: "Drinks",
            drinks: drink
        });
    } catch (err) {
        res.status(400).json({
            route: "Drinks",
            error: err
        });
    }
});

router.delete('/:id', async (req, res) => {
    try {
        const drink = await Drink.deleteDrinkById(req.params.id);
        res.status(200).json({
            route: "Drinks",
            drinks: drink
        });
    } catch (err) {
        res.status(400).json({
            route: "Drinks",
            error: err
        });
    }
});

module.exports = router;