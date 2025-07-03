import kue from 'kue';

const push_notification_code_3 = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        return (new Error('Jobs is not an array'))
    }
    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', {
            phoneNumber: jobData.phoneNumber,
            message: jobData.message,
        }).save((err) => {
            if (!err) {
                console.log(`Notification job created: ${job.id}`);
            }
        });

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });

        job.on('failed', (err) => {
            console.log(`Notification job ${job.id} failed: ${err}`);
        });

        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });
    });
}

export default createPushNotificationsJobs;