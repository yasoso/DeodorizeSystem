var http = require("http");
var fs = require('fs');
var settings = require('./settings')

const express = require('express');
const bodyParser = require('body-parser');


const app = express();

// app.engine('.html', require('jade').renderFile);

// urlencodedとjsonは別々に初期化する
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

app.use(express.static('public'));


app.listen(settings.port,settings.host);
console.log('Server is online.');

app.get('/', function(req, res){
    // res.render('index.html');
//htmlの表示
var url = "public" + (req.url.endsWith("/") ? req.url + "index.html" : req.url);
  if (fs.existsSync(url)) {
    fs.readFile(url, (err, data) => {
      if (!err) {
        res.writeHead(200, {"Content-Type": getType(url)});
        res.end(data);
      } else {
        res.statusCode = 500;
        res.end();
      }
    });
  } else {
    res.statusCode = 404;
    res.end();
  }
});

var count_ = 0;
var smell_ = -99;

app.post('/', function(req, res) {
    // リクエストボディを出力
    console.log(req.body);
    // パラメータ名、nameを出力
    //単一objのbodyを参照する場合
    // console.log(req.body.smell);
    // console.log(req.body.IP);
    // console.log(req.body.Button);

    //jsonファイル内の複数bodyを参照する場合
    console.log(req.body[0].smell);
    console.log(req.body[0].IP);
    console.log(req.body[0].Button);

    smell_ = req.body[0].smell;
    count_ = res.body[0].count;
    res.send('POST request to the homepage');
})
//
// function smellupdate(){
//   var txt = "臭い：" + smell_;
//   document.getElementById("smellTxt").innerHTML = txt;
// }

app.get('/smellUpdate', function(req, res){
  console.log(smell_);
  //res.send(smell_);
  res.writeHead(200, {"Content-Type": "application/json"});
  res.end(JSON.stringify({ "smell": smell_ }));

});
app.get('/countUpdate', function(req, res){
  console.log(count_);
  //res.send(smell_);
  res.writeHead(200, {"Content-Type": "application/json"});
  res.end(JSON.stringify({ "count": count_ }));

});
function getType(_url) {
    var types = {
      ".html": "text/html",
      ".css": "text/css",
      ".js": "text/javascript",
      ".png": "image/png",
      ".gif": "image/gif",
      ".svg": "svg+xml"
    }
    for (var key in types) {
      if (_url.endsWith(key)) {
        return types[key];
      }
    }
    return "text/plain";
  }

// server.listen(settings.port,settings.host)
