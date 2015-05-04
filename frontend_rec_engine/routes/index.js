var express = require('express');
var router = express.Router();


router.get('/template', function(req, res, next) {
  res.render('template', { title: 'Express' });
});


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('home', { title: 'Express' });
});

router.get('/sample_data', function(req, res, next) {
  res.render('sample_data', { title: 'Express' });
});

router.get('/aboutus', function(req, res, next) {
  res.render('aboutus', { title: 'Express' });
});

router.get('/iframe', function(req, res, next) {
  res.render('frames/iframe', { title: 'Express' });
});
router.get('/iframe_topstar', function(req, res, next) {
  res.render('frames/iframe_topstar', { title: 'Express' });
});
router.get('/iframe_euclidean', function(req, res, next) {
  res.render('frames/iframe_euclidean', { title: 'Express' });
});
router.get('/iframe_pearsons', function(req, res, next) {
  res.render('frames/iframe_pearsons', { title: 'Express' });
});
router.get('/iframe_SVM', function(req, res, next) {
  res.render('frames/iframe_SVM', { title: 'Express' });
});


router.get('/topstar', function(req, res, next) {
  res.render('1topstar', { title: 'Express' });
});
router.get('/euclidean', function(req, res, next) {
  res.render('2euclidean', { title: 'Express' });
});
router.get('/pearsons', function(req, res, next) {
  res.render('3pearsons', { title: 'Express' });
});
router.get('/SVM', function(req, res, next) {
  res.render('4SVM', { title: 'Express' });
});

router.post('/show', function(req, res, next) {
  //need to pull data about a resutatnt and display it
  
  res.render('iframe', { title: 'Express' });
});

module.exports = router;
