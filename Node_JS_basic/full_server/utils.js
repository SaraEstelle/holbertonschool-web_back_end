const fs = require('fs');

function readDatabase(filePath) {
  return fs.promises.readFile(filePath, 'utf8').then((data) => {
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    const result = {};

    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');
      if (!result[field]) {
        result[field] = [];
      }
      result[field].push(firstname);
    });

    return result;
  });
}

module.exports = readDatabase;
