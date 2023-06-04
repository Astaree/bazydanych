const express = require('express');
const router = express.Router();
const Meal = require('../controller/meal');

router.get('/', async (req, res) => {
    if (req.query.name) {
        await Meal.getMealByName(req.query.name).then((meal) => {
            res.status(200).json({
                route: "Meals",
                meal: meal
            });
        }).catch((err) => {
            res.status(400).json({
                route: "Meals",
                error: err
            });
        });
        return;
    }
    await Meal.getMeals().then((meal) => {
        res.status(200).json({
            route: "Meals",
            meals: meal
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Meals",
            error: err
        });
    });
});

router.post('/', async (req, res) => {
    await Meal.addMeal(req.body).then((meal) => {
        res.status(201).json({
            route: "Meals",
            meal: meal
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Meals",
            error: err
        });
    });
});

router.delete('/', async (req, res) => {
    await Meal.deleteMeals().then(() => {
        res.status(200).json({
            route: "Meals",
            meals: []
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Meals",
            error: err
        });
    }
    );
});

router.get('/:id', async (req, res) => {
    await Meal.getMealById(req.params.id).then((meal) => {
        res.status(200).json({
            route: "Meals",
            meal: meal
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Meals",
            error: err
        });
    });
});

router.delete('/:id', async (req, res) => {
    await Meal.deleteMealById(req.params.id).then((meal) => {
        res.status(200).json({
            route: "Meals",
            meal: meal
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Meals",
            error: err
        });
    });
});

router.put('/:id', async (req, res) => {
    await Meal.updateMeal(req.params.id, req.body).then((meal) => {
        res.status(200).json({
            route: "Meals",
            meal: meal
        });
    }).catch((err) => {
        res.status(400).json({
            route: "Meals",
            error: err
        });
    });
});

module.exports = router;