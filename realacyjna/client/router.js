const router = express.Router();


app.use(express.static(path.join(__dirname, 'build'))); //static files from build folder

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, 'build', 'index.html'));
    }
);