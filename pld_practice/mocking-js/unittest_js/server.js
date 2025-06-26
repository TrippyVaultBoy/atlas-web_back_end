// server.js
const express = require('express');
const db = require('./db');
const insertSampleData = require('./sampleData');

const app = express();
app.use(express.json());

insertSampleData();

// GET all users
app.get('/users', (req, res) => {
  db.all('SELECT * FROM users', (err, rows) => {
    const processedUsers = rows.map(user => ({
      ...user,
      name: user.name.toUpperCase(),        // Uppercase name
      nameLength: user.name.length          // Add name length
    }));
    if (err) return res.status(500).json({ error: err.message });
    res.json(processedUsers);
  });
});

// GET user by ID
app.get('/users/:id', (req, res) => {
  const id = req.params.id;
  db.get('SELECT * FROM users WHERE id = ?', [id], (err, row) => {
    if (err) return res.status(500).json({ error: err.message });
    if (!row) return res.status(404).json({ error: 'User not found' });
    res.json(row);
  });
});

// Start server only if not in test mode
if (require.main === module) {
  const PORT = 3000;
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
}

module.exports = app;