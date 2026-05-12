const http = require('http');
const countStudents = require('./3-read_file_async');

const databasePath = process.argv[2];

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const responseParts = ['This is the list of our students'];
    const originalLog = console.log;

    console.log = (msg) => responseParts.push(msg);

    try {
      await countStudents(databasePath);

      console.log = originalLog;

      res.end(responseParts.join('\n'));
    } catch (error) {
      console.log = originalLog;
      res.end(`${responseParts[0]}\n${error.message}`);
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
