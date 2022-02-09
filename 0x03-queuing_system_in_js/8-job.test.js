import createPushNotificationsJobs from "./8-job";
import kue from 'kue';

const queue = kue.createQueue();


const list = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    }
];

before(function() {
  queue.testMode.enter();
});

afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});

describe('creatPushNotificationsJobs', () => {
    it('does something cool', function() {
        queue.createJob('myJob', { foo: 'bar' }).save();
        queue.createJob('anotherJob', { baz: 'bip' }).save();
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('myJob');
        expect(queue.testMode.jobs[0].data).to.eql({ foo: 'bar' });
      });      

    it('it works if the given is array of jobs', () => {
        const ret = createPushNotificationsJobs(list, queue);
        expect(queue.testMode.jobs.length).to.equal(1);
    })
})

it('')