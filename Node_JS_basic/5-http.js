const http = require('http');
const fs = require('fs');

const databasePath = process.argv[2];

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .filter((line) => line.trim() !== '')
        .slice(1);

      const groups = {};

      lines.forEach((line) => {
        const fields = line.split(',');
        const firstname = fields[0];
        const field = fields[3];

        if (!groups[field]) {
          groups[field] = [];
        }
        groups[field].push(firstname);
      });
      resolve({ total: lines.length, groups });
    });
  });
}

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {

    readDatabase(databasePath)
      .then(({ total, groups }) => {
        let body = 'This is the list of our students\n';
        body += `Number of students: ${total}\n`;

        const sortedFields = Object.keys(groups).sort((a, b) =>
          a.toLowerCase().localeCompare(b.toLowerCase())
        );
        sortedFields.forEach((field) => {
          const names = groups[field].join(', ');
          body += `Number of students in ${field}: ${groups[field].length}. List: ${names}\n`;
        });

        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(body);
      })
      .catch((err) => {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end(err.message);
      });
  }
});
app.listen(1245);
module.exports = app;
