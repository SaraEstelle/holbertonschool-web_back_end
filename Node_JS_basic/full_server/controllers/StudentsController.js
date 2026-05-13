const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    const dataPath = process.argv[2];

    readDatabase(dataPath)
      .then((fields) => {
        const responseParts = ['This is the list of our students'];

        const sortedFields = Object.keys(fields)
          .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        for (const field of sortedFields) {
          const students = fields[field];
          responseParts.push(
            `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`,
          );
        }

        res.status(200).send(responseParts.join('\n'));
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    const dataPath = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(dataPath)
      .then((fields) => {
        const students = fields[major] || [];
        res.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}
export default StudentsController;
