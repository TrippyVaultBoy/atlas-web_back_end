//In a file named 5-http.js, create a small HTTP server using the http module:
//  It should be assigned to the variable app and this one must be exported
//  HTTP server should listen on port 1245
//  It should return plain text
//  When the URL path is /, it should display Hello Holberton School! in the page body
//  When the URL path is /students, it should display This is the list of our students followed by the same content as the file 3-read_file_async.js (with and without the database) - the name of the database must be passed as argument of the file
//  CSV file can contain empty lines (at the end) - and they are not a valid student!

const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello Holberton School!')
    } else if (req.url === '/students') {
        const database = process.argv[2]
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        
        countStudents(database)
            .then((data) => {
                res.end(`This is the list of our students\n${data}`);
            })
            .catch((err) => {
                res.end(`This is the list of our students\n${err.message}`)
            })
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 Not Found')
    }
});

app.listen(1245);

module.exports = app;