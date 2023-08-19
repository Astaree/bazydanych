const express = require('express');
const router = express.Router();


// Define routes
router.get("/", (req, res) => {
  res.render("index", { title: "Home", message: "Hello there!" });
});

//drinks, clients, meals, orders, 

// Example route that interacts with the database

router.use("/api/drinks", require("./api/drinks/drinks"));
router.use("/api/meals", require("./api/meals/meals"));
router.use("/api/orders", require("./api/orders/orders"));
router.use("/api/clients", require("./api/clients/clients.js"));

// router.use("/api/deliveries", require("./api/deliveries/deliveries"));

router.use("/api/new_drink", require("./api/drinks/new_drink"));
router.use("/api/new_meal", require("./api/meals/new_meal"));
router.use("/api/new_order", require("./api/orders/new_order"));

// router.use("/api/new_delivery", require("./api/deliveries/new_delivery"));

router.use("/api/edit_drink", require("./api/drinks/update_drink"));
router.use("/api/edit_meal", require("./api/meals/update_meal"));
router.use("/api/edit_order", require("./api/orders/update_order"));

// router.use("/api/edit_delivery", require("./api/deliveries/update_delivery"));


router.use("/api/delete_drink", require("./api/drinks/delete_drink"));
router.use("/api/delete_meal", require("./api/meals/delete_meal"));
router.use("/api/delete_order", require("./api/orders/delete_order"));

// router.use("/api/delete_delivery", require("./api/deliveries/delete_delivery"));


// router.use("/api/ingredients", require("./ingredients"));
// router.use("/api/meal", require("./meal"));
// router.use("/api/picture", require("./picture"));


module.exports = router;

