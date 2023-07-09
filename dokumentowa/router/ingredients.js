const express = require('express');
const router = express.Router();


//get all ingredients
router.get('/', async (req, res) => {
    await Ingredient.getIngredients().then((ing) => {
        res.status(200).json({
            route: "Ingredients",
            ingredients: ing
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Ingredients",
            error: err
        });
    });
});

//crates a new ingredient
router.post('/', async (req, res) => {
    await Ingredient.addIngredient(req.body).then((ing) => {
        res.status(201).json({
            route: "Ingredients",
            ingredient: ing
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Ingredients",
            error: err
        });
    });
});

//delete all ingredients
router.delete('/', async (req, res) => {
    await Ingredient.deleteIngredients().then(() => {
        res.status(200).json({
            route: "Ingredients",
            ingredients: []
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Ingredients",
            error: err
        });
    }
    );
});

//get ingredient by id
router.get('/:id', async (req, res) => {
    await Ingredient.getIngredientById(req.params.id).then((ing) => {
        res.status(200).json({
            route: "Ingredients",
            ingredient: ing
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Ingredients",
            error: err
        });
    });
});

//delete an ingredient by id
router.put('/:id', async (req, res) => {
    await Ingredient.updateIngredientById(req.params.id, req.body).then((ing) => {
        res.status(200).json({
            route: "Ingredients",
            ingredient: ing
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Ingredients",
            error: err
        });
    });
});

//delete an ingredient by id
router.delete('/:id', async (req, res) => {
    await Ingredient.deleteIngredientById(req.params.id).then((ing) => {
        res.status(200).json({
            route: "Ingredients",
            ingredient: ing
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Ingredients",
            error: err
        });
    });
});

module.exports = router;
