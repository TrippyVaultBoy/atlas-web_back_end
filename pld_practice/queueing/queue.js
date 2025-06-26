import { Queue } from 'bullmq';

const mealQueue = new Queue('mealQueue', {
    connection: { host: 'localhost', port: 6379 }
});

console.log('Meal queue is ready!');

export default mealQueue;