var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('home', { title: 'Express' });
});

router.get('/index', function(req, res, next) {
  res.render('single_circle', { title: 'Express' });
});

router.get('/sample_data', function(req, res, next) {
  res.render('sample_data', { title: 'Express' });
});

router.get('/template', function(req, res, next) {
  res.render('template', { title: 'Express' });
});

router.get('/iframe', function(req, res, next) {
  res.render('iframe', { title: 'Express' });
});
router.get('/aboutus', function(req, res, next) {
  res.render('aboutus', { title: 'Express' });
});


module.exports = router;
