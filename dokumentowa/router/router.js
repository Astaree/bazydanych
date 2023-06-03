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
        url: 'http://localhost:3000/drinks',
      },
      {
        name: 'ingredients',
        url: 'http://localhost:3000/ingredients',
      },
      {
        name: 'pictures',
        url: 'http://localhost:3000/pictures',
      },
      {
        name:"client",
        url:"http://localhost:3000/client",
      },
      {
        name:"meal",
        url:"http://localhost:3000/meal",
      },
      {
        name:"order",
        url:"http://localhost:3000/order",
      }
    ],
  });
});

// Example route that interacts with the database

router.use("/client", require("./client"));
router.use("/drinks", require("./drinks"));
router.use("/ingredients", require("./ingredients"));
router.use("/meal", require("./meal"));
router.use("/order", require("./order"));
router.use("/picture", require("./picture"));


module.exports = router;

