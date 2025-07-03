// 1-redis_client.js

import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server', err);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        redis.print(err, reply);
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, value) => {
        if (err) {
            console.error('Error getting value:', err);
        } else {
            console.log(value);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');