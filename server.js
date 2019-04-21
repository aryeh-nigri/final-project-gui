const express = require('express');
const bodyParser = require('body-parser');
var fs = require('file-system');

const app = express();

// support parsing of application/json type post data
app.use(bodyParser.json());

//support parsing of application/x-www-form-urlencoded post data
app.use(bodyParser.urlencoded({
    extended: true
}));

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

app.post('/diagnosis', async function (req, res) {
    console.log("POST");
    console.log(req.body);
    // var firstName = req.body.firstName;
    // var lastName = req.body.lastName;
    // var gender = req.body.gender;
    // var birthday = req.body.birthday;
    // var exam1 = req.body.exam1;
    // var exam2 = req.body.exam2;
    // var exam3 = req.body.exam3;
    // var pacsFile = req.body.pacsFile;
    // var pathToData = "ml_scripts/bones.csv";
    var firstName = "joao";
    var content = req.body.content;


    // appendFile function with filename, content and callback function
    await fs.appendFile('data.csv', content, function (err) {
        if (err) throw err;
        console.log('File is created successfully.');
    });

    let runPy = new Promise(function (success, nosuccess) {

        const {
            spawn
        } = require('child_process');
        //const pyprog = spawn('py', ['./ml_scripts/classifier.py', firstName, lastName, gender, birthday, exam1, exam2, exam3, pacsFile]);
        const pyprog = spawn('py', ["./test.py", firstName, "data.csv"]);

        pyprog.stdout.on('data', function (data) {
            success(data);
        });

        pyprog.stderr.on('data', (data) => {
            nosuccess(data);
        });

    });

    runPy.catch(function (error) {
        console.log("o erro eh esse: **\n" + error);
    });

    runPy.then(function (fromRunpy) {
        var array = fromRunpy.toString().split("- ");
        console.log(array);

        const LR = array[0].split(": ");
        const LDA = array[1].split(": ");
        const KNN = array[2].split(": ");
        const CART = array[3].split(": ");
        const NB = array[4].split(": ");
        const SVM = array[5].split(": ");

        let indexOfChar;
        indexOfChar = LDA[0].lastIndexOf("]");
        const matrixConfusionLR = LDA[0].substring(0, indexOfChar + 1);
        indexOfChar = KNN[0].lastIndexOf("]");
        const matrixConfusionLDA = KNN[0].substring(0, indexOfChar + 1);
        indexOfChar = CART[0].lastIndexOf("]");
        const matrixConfusionKNN = CART[0].substring(0, indexOfChar + 1);
        indexOfChar = NB[0].lastIndexOf("]");
        const matrixConfusionCART = NB[0].substring(0, indexOfChar + 1);
        indexOfChar = SVM[0].lastIndexOf("]");
        const matrixConfusionNB = SVM[0].substring(0, indexOfChar + 1);
        const matrixConfusionSVM = array[6];

        const mlResults = {
            LR: LR[1],
            LDA: LDA[1],
            KNN: KNN[1],
            CART: CART[1],
            NB: NB[1],
            SVM: SVM[1],

            LR_matrix: matrixConfusionLR,
            LDA_matrix: matrixConfusionLDA,
            KNN_matrix: matrixConfusionKNN,
            CART_matrix: matrixConfusionCART,
            NB_matrix: matrixConfusionNB,
            SVM_matrix: matrixConfusionSVM,

        }

        console.log(mlResults);

        res.json(mlResults);
        // res.render('result', {
        //     result: fromRunpy.toString()
        // });
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


//TODO
/*
- por uma foto do pacs image ao lado do choose file
- pedir tbm id do paciente
- adicionar uma saida para identificar o ROI e mostrar resultado na tela e esperar ishur
- adicionar uma saida para fazer ibud tmuna a adicionar o resultado e esperar ishur  
- adicionar uma saida para fazer as measurements e esperar ishur


procurar PCA em python    DONE



*/