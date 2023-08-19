const express = require('express');
const router = express.Router();
const client = require('../../../models/client');

router.get('/', async (req, res) => {
  try {
    const clients = await client.find();
    res.render('clients', { clients });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.post('/', async (req, res) => {
  const { name, address, phoneNumber, email } = req.body;
  const new_client = new client({
    name,
    address,
    phoneNumber,
    email,
  });

  try{
    //find client with the same  email or phone number
    let exists = await client.find({ $or: [{ email }, {phoneNumber}] });
    if(exists.length > 0){

    }else{
      const newClient = await new_client.save();
      res.status(201).json(newClient);
    }
  }catch(err){
    res.status(400).json({ message: err.message });
  }
});

module.exports = router;