const express = require('express');
const { default: mongoose } = require('mongoose');
const router = express.Router();


// Define routes
router.get("/", (req, res) => {

  res.status(200).json({
    route: "Home",
    message: "Welcome to the home page!",
  });
});

// Example route that interacts with the database

router.use("/api/client", require("./client"));
router.use("/api/clients", require("./clients"));
router.use("/api/drinks", require("./drinks"));
router.use("/api/order", require("./order"));
// router.use("/api/ingredients", require("./ingredients"));
// router.use("/api/meal", require("./meal"));
// router.use("/api/delivery", require("./delivery"));
// router.use("/api/picture", require("./picture"));


module.exports = router;

