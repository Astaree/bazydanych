const express = require('express');
const router = express.Router();
const Client = require('../controller/client');


//get all ingredients
router.get('/', async (req, res) => {
  await Client.getDeleted().then((clients) => {
    res.status(200).json({
      route: "Clients",
      clients: clients
    });
  }
  ).catch((err) => {
    res.status(400).json({
      route: "Clients",
      error: err
    });
  }
  );
});

module.exports = router;