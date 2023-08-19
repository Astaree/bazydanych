const express = require('express');
const router = express.Router();
const Drink = require('../../../models/drink');


//get all drinks
router.get('/', async (req, res) => {
    try {
        const drinks = await Drink.find();
        res.render('drinks', { drinks });
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


module.exports = router;