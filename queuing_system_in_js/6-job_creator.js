import kue from 'kue';

const push_notification_code = kue.createQueue();
const job = push_notification_code.create('push_notification_code', {
    phoneNumber: '12345',
    message: 'test job',
})
.save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    }
});

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', (err) => {
    console.log('Notification job failed');
});