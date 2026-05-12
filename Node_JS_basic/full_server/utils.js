const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data
        .trim()
        .split('\n')
        .slice(1);

      const groups = {};

      lines.forEach((line) => {
        const [firstname, , , field] = line.split(',');

        if (!groups[field]) {
          groups[field] = [];
        }
        groups[field].push(firstname);
      });
      resolve(groups);
    });
  });
}
module.exports = readDatabase;
