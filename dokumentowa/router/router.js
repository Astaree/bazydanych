const express = require('express');
const { default: mongoose } = require('mongoose');
const router = express.Router();


// Define routes
router.get("/", (req, res) => {

  res.render("index", { title: "Home", message: "Hello there!" });
});

// Example route that interacts with the database

router.use("/api/clients", require("./api/client/clients"));
router.use("/api/drinks", require("./api/drinks/drinks"));
router.use("/api/orders", require("./api/order/orders"));
router.use("/api/meals", require("./api/meals/meals"));

router.use("/api/del/clients", require("./api/client/del_client"));
router.use("/api/del/drinks", require("./api/drinks/del_drinks"));

router.use("/api/new_order", require("./api/order/new_order"));

// router.use("/api/ingredients", require("./ingredients"));
// router.use("/api/meal", require("./meal"));
// router.use("/api/delivery", require("./delivery"));
// router.use("/api/picture", require("./picture"));


module.exports = router;

