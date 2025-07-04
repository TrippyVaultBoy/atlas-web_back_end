// Using the database database.csv (provided in project description),
// create a function countStudents in the file 2-read_file.js

const fs = require('fs');
const csv = require('csv-parser');
const { error } = require('console');

function countStudents(path) {
    
    const studentsByField = {};
    let total = 0;

    const stream = fs.createReadStream(path)
        .pipe(csv())
        .on('data', (row) => {
            const field = row.field
            const firstname = row.firstname;

            if (field && firstname) {
                if (!studentsByField[field]) {
                    studentsByField[field] = [];
                }
                studentsByField[field].push(firstname);
                total += 1;
            }
        })
        .on('end', () => {
            console.log(`Number of students: ${total}`);
            for (const [field, students] of Object.entries(studentsByField)) {
                console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
            }
        })
        .on('error', () => {
            throw new error("Cannot load the database");
        });
}

module.exports = countStudents;