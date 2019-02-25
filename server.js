const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// support parsing of application/json type post data
app.use(bodyParser.json());

//support parsing of application/x-www-form-urlencoded post data
app.use(bodyParser.urlencoded({ extended: true }));

// set the view engine to ejs
app.set('view engine', 'ejs');

// app.use(express.static(path.join(__dirname, 'public')));
// app.use(urlencoded({ extended: false }));

// load the files that are in the public directory from the /static path prefix
app.use('/static', express.static('public'));

// app.get('/', (req, res) => {

//     res.write('welcome\n');

//     runPy.then(function(fromRunpy) {
//         console.log(fromRunpy.toString());
//         res.end(fromRunpy);
//     });
// })

app.post('/diagnosis', function (req, res) {
    console.log("POST");
    console.log(req.body);
    var firstName = req.body.firstName;
    var lastName = req.body.lastName;
    var gender = req.body.gender;
    var birthday = req.body.birthday;
    var exam1 = req.body.exam1;
    var exam2 = req.body.exam2;
    var exam3 = req.body.exam3;
    var pacsFile = req.body.pacsFile;

    let runPy = new Promise(function(success, nosuccess) {

        const { spawn } = require('child_process');
        const pyprog = spawn('python', ['./ml_scripts/classifier.py', firstName, lastName, gender, birthday, exam1, exam2, exam3, pacsFile]);
    
        pyprog.stdout.on('data', function(data) {
            success(data);
        });
    
        pyprog.stderr.on('data', (data) => {
            nosuccess(data);
        });
        
    });

    runPy.then(function(fromRunpy) {
        console.log(fromRunpy.toString());
        res.render('result', {result: fromRunpy.toString()});
        // res.end(fromRunpy);
    });

});

// use res.render to load up an ejs view file of index page
app.get('/', function (req, res) {
    res.render('index');
    
    // antigo index tinha:
    // <% students.forEach(function(student){ %>
    //     <%- include('partials/student', {student: student}) %>
    // <% }); %>

});

// the same for about page 
app.get('/about', function (req, res) {
    res.render('about');
});

app.get('/data', function (req, res) {
    res.render('datasource');
});

app.listen(4000, () => console.log('Application listening on port 4000!'));


// var spawn = require('child_process').spawn,
//     py = spawn('python', ['compute_input.py']),
//     data = [1, 2, 3, 4, 5, 6, 7, 8, 9],
//     dataString = '';

// /*Here we are saying that every time our node application receives data from 
// the python process output stream(on 'data'), we want to convert that received 
// data into a string and append it to the overall dataString.*/
// py.stdout.on('data', function (data) {
//     dataString += data.toString();
// });

// /*Once the stream is done (on 'end') we want to simply log the received data to the console.*/
// py.stdout.on('end', function () {
//     console.log('Sum of numbers=', dataString);
// });


// app.get('/', (req, res) => {

//     /*We have to stringify the data first otherwise our python process wont recognize it*/
//     py.stdin.write(JSON.stringify(data));

//     py.stdin.end();

// });
