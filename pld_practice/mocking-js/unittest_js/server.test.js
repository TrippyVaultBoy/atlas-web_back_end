// test server.js

const server = require('./server');
const db = require('./db');

jest.mock('./db');

test('Mocking of database', async () => {
    db.serialize.mockReturnValue(
        [
            {
                "id": 1,
                "name": "ALICE",
                "email": "alice@example.com",
                "nameLength": 5
            },
            {
                "id": 2,
                "name": "BOB",
                "email": "bob@example.com",
                "nameLength": 3
            }
        ]
    );
});