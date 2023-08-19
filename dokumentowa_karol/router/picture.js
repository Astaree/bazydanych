const express = require('express');
const router = express.Router();

router.get('/:id', async (req, res) => {
  await Picture.getPictureById(req.params.id).then((picture) => {
    res.status(200).json({
      route: "Pictures",
      picture: picture
    });
  }
  ).catch((err) => {
    res.status(400).json({
      route: "Pictures",
      error: err
    });
  }
  );
});

module.exports = router;
