const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    const filePath = process.argv[2];

    readDatabase(filePath)
      .then((groups) => {
        let body = 'This is the list of our students\n';

        const fields = Object.keys(groups);

        const total = fields.reduce(
            (acc, field) => acc +groups[field].length,
            0
        );
        body += `Number of students: ${total}\n`;

        fields.forEach((field) => {
          const list = groups[field].join(', ');
          body += `Number of students in ${field}: ${groups[field].length}. List: ${list}\n`;
        });

        res.status(200).type('text').send(body.trimEnd());
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    const filePath = process.argv[2];

    readDatabase(filePath)
      .then((groups) => {
        const list = groups[major] ? groups[major].join(', ') : '';
        res.status(200).type('text').send(`List: ${list}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}
module.exports = StudentsController;
