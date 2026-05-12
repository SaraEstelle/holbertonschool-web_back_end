const fs = require('fs');

function countStudents(path) {
  let fileContent;

  try {
    fileContent = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = fileContent
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
}
module.exports = countStudents;
