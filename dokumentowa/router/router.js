const express = require('express');
const { default: mongoose } = require('mongoose');
const router = express.Router();


// Define routes
router.get('/', (req, res) => {
  //list all routes
  res.status(200).json({
    message: 'Welcome to the API',
    routes: [
      {
        name: 'drinks',
        url: 'http://localhost:3000/api/drinks',
      },
      {
        name: 'ingredients',
        url: 'http://localhost:3000/api/ingredients',
      },
      {
        name:"client",
        url:"http://localhost:3000/api/client",
      },
      {
        name:"meal",
        url:"http://localhost:3000/api/meal",
      },
      {
        name:"order",
        url:"http://localhost:3000/api/order",
      },
      {
        name:"delivery",
        url:"http://localhost:3000/api/delivery",
      },
      // {
      //   name: 'picture',
      //   url: 'http://localhost:3000/api/picture',
      // },
    ],
  });
});

// Example route that interacts with the database

router.use("/api/client", require("./client"));
router.use("/api/drinks", require("./drinks"));
router.use("/api/ingredients", require("./ingredients"));
router.use("/api/meal", require("./meal"));
router.use("/api/order", require("./order"));
router.use("/api/delivery", require("./delivery"));
// router.use("/api/picture", require("./picture"));


module.exports = router;

