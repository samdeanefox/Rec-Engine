var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('home', { title: 'Express' });
});

router.get('/index', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/sample_data', function(req, res, next) {
  res.render('sample_data', { title: 'Express' });
});

module.exports = router;
