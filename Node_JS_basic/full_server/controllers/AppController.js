class AppController {
  static getHomepage(req, res) {
    res.status(200).type('text/plain').send('Hello Holberton School!\n');
  }
}
module.exports = AppController;
