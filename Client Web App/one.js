var express = require('express');
var app = express();
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var bodyParser = require('body-parser'); 
var urlencodedParser = bodyParser.urlencoded({ extended: false })
var MongoClient = require('mongodb').MongoClient;
MongoClient.connect("mongodb://127.0.0.1/mydb",function(err,db){
    if(!err)
        console.log("connected !");

        app.use(express.static('public'));

    app.get('/index.html',function(req,res){
        res.send(__dirname+"/"+"index.html");
    
    });
    app.get('/register.html',function(req,res){
        res.send(__dirname+"/"+"register.html");
    
    });
    app.get('/survey.html',function(req,res){
        res.send(__dirname+"/"+"survey.html");
    
    });
    

    
    
    app.get('/process_get1',function(req,res){
        console.log("hiiii");
        var newperson = req.query;
        
        var email = req.query['email'];
        var name = req.query['name'];
        var contact = req.query['contact'];
       

      
        console.log("name : "+name+" phone : "+contact+" email id : "+email);
       var obj = (JSON.stringify(newperson));
       console.log(JSON.stringify(newperson));


       
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
             if (this.readyState == 4 && this.status == 200) {
                 console.log(this.responseText);
             }
        };
        xhttp.open("POST", "http://52.77.246.79:5000/insert", true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(obj);
    

    });



    app.get('/process_get',function(req,res){
        var newperson2 = req.query;
        console.log(newperson2);
        var email = req.query['email'];
        var locationname = req.query['locationname'];
        var budget = req.query['budget'];
        var area = req.query['area'];
        var number_of_students = req.query['number_of_students'];
        var smokeProne = req.query['smokeProne'];
        var generalPublic = req.query['generalPublic'];
        var highways = req.query['highways'];
        var disability = req.query['disability'];
       

      
        console.log("location name :"+locationname+" email : "+email+" budget : "+budget+" area : "+area+" num of studs :"+number_of_students+" smoke prone : "+smokeProne+" general public ?"+generalPublic+" disability: "+disability+" highways : "+highways);
       var obj2 = (JSON.stringify(newperson2));
       console.log(JSON.stringify(newperson2));


       
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
             if (this.readyState == 4 && this.status == 200) {
                 console.log(this.responseText);
             }
        };
        xhttp.open("POST", "http://52.77.246.79:5000/insert", true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(obj2);
    

    });
   
        


    });
   
        


   
    app.listen(5000);
