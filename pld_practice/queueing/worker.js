import { Worker } from 'bullmq';
import mealQueue from './queue.js';

const worker = new Worker('mealQueue', async (job) => {
    const { customer, course } = job.data;

    console.log(`👨‍🍳 Preparing ${course.name} for ${customer}... (⏳ ${course.prepTime} msecs)`);

    // Simulate cooking time
    await new Promise(resolve => setTimeout(resolve, course.prepTime));

    console.log(`🍽️ Served: ${customer}'s ${course.name}`);

    // Simulate eating time (fast simulation)
    const eatingTime = Math.random() * 5000 + 2000;
    console.log(`🍴 ${customer} is eating ${course.name} (⏳ ${eatingTime} msecs)`);
    
    await new Promise(resolve => setTimeout(resolve, eatingTime));

}, {
    connection: { host: 'localhost', port: 6379 },
    concurrency: 3 // Process 3 dishes at once
});

console.log('Worker is ready to process courses!');
