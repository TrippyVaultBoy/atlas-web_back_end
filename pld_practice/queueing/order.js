import mealQueue from './queue.js';
import { menu } from './menu.js'; // Import cooking times

const customers = ["Alice", "Bob", "Charlie", "David", "Emma"];

async function placeOrder() {
    const customer = customers[Math.floor(Math.random() * customers.length)];
    
    const meal = [
        menu.starters[Math.floor(Math.random() * menu.starters.length)],
        menu.mainCourses[Math.floor(Math.random() * menu.mainCourses.length)],
        menu.desserts[Math.floor(Math.random() * menu.desserts.length)]
    ];

    const order = { customer, meal, currentStep: 0 };

    console.log(`📌 New Order: ${customer} ordered a 3-course meal`);

    // Queue each course separately to allow overlapping cooking
    for (const course of meal) {
        await mealQueue.add('prepareCourse', { customer, course });
        console.log(`📝 Added ${course.name} to queue for ${customer}`);
    }
}

// Customers place orders every 4-8 seconds
// setInterval(placeOrder, Math.random() * 4000 + 4000);
placeOrder();
placeOrder();
