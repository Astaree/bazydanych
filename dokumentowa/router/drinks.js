const express = require('express');
const router = express.Router();
const Drink = require('../controller/drink');


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

//delete all drinks
router.delete('/', async (req, res) => {
    try {
        const drink = await Drink.deleteDrinks();
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

//get drink by id
router.get('/:id', async (req, res) => {
    try {
        const drink = await Drink.getDrinkById(req.params.id);
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

//delete an drink by id
router.put('/:id', async (req, res) => {
    try {
        const drink = await Drink.updateDrinkById(req.params.id, req.body);
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

//delete an drink by id
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