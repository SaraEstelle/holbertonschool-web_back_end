const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .trim()
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1);

      console.log(`Number of students: ${students.length}`);

      const groups = {};

      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');

        if (!groups[field]) {
          groups[field] = [];
        }
        groups[field].push(firstname);
      });

      Object.keys(groups).forEach((field) => {
        const list = groups[field].join(', ');
        console.log(`Number of students in ${field}: ${groups[field].length}. List: ${list}`);
      });

      resolve();
    });
  });
}
module.exports = countStudents;
