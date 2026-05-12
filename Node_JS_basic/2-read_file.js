const fs = require('fs');

function countStudents(path) {
  let fileContent;

  try {
    fileContent = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = fileContent.split('\n');

  const students = lines
    .filter((line) => line.trim() !== '')
    .slice(1);

  console.log(`Number of students:${students.length}`);

  const groups = {};
  students.forEach((line) => {
    const fields = line.split(',');
    const firstname = fields[0];
    const field = fields[3];

    if (!groups[fields]) {
      groups[field] = [];
    }
    groups[field].push(firstname);
  });

  const sortedFields = Object.keys(groups).sort((a, b) =>
    a.toLowerCase().localeCompare(b.toLowerCase())
  );

  sortedFields.forEach((field) => {
    const names = groups[field].join(', ');
    console.log(
      `Number of students in${field}:${groups[field].length}. list:${names}`
    );
  });
}
module.exports = countStudents;
