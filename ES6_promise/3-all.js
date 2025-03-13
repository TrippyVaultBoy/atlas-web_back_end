import uploadPhoto from 'utils.js'
import createUser from 'utils.js'

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([uploadPhoto, user]) => {
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`)
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
