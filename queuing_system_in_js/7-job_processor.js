import kue from 'kue';

const blacklist = [
    4153518780,
    4153518781,
];

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);

    if (blacklist.includes(Number(phoneNumber))) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
    const phoneNumber = job.data.phoneNumber;
    const message = job.data.message;
    sendNotification(phoneNumber, message, job, done);
})