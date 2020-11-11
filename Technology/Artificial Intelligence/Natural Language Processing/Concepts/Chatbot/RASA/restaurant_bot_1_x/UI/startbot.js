const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();

app.use("/static", express.static(__dirname + '/static'));
router.get('/',function(req,res){
  res.sendFile(__dirname+ '/index.html');
  //__dirname : It will resolve to your project folder.
});

//add the router
app.use('/', router);
app.listen(process.env.port || 3000);

console.log('Running at Port 3000');