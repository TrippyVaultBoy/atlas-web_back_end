// Using the database database.csv (provided in project description),
// create a function countStudents in the file 3-read_file_async.js

const fs = require('fs');
const csv = require('csv-parser');
const { error } = require('console');

function countStudents(path) {
    return new Promise((resolve, reject) => {
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
                let output = `Number of students: ${total}\n`;
                for (const [field, students] of Object.entries(studentsByField)) {
                    output += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
                }
                resolve(output);
            })
            .on('error', () => {
                reject(new Error("Cannot load the database"))
            });
    });
}

module.exports = countStudents;