// sampleData.js
const db = require('./db');

function insertSampleData() {
  const stmt = db.prepare('INSERT INTO users (name, email) VALUES (?, ?)');
  stmt.run('Alice', 'alice@example.com');
  stmt.run('Bob', 'bob@example.com');
  stmt.finalize();
}

module.exports = insertSampleData;
