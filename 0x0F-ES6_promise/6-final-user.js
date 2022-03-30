#!/usr/bin/node
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const promi1 = {
    status: 'pending ',
  };
  const promi2 = {
    status: 'pending ',
  };

  try {
    const signup = await signUpUser(firstName, lastName);
    promi1.status = 'fulfilled';
    promi1.value = signup;
  } catch (err) {
    promi1.status = 'rejected';
    promi1.value = err.toString();
  }

  try {
    const upload = await uploadPhoto(fileName);
    promi2.status = 'fulfilled';
    promi2.value = upload;
  } catch (err) {
    promi2.status = 'rejected';
    promi2.value = err.toString();
  }

  return [promi1, promi2];
}

export default handleProfileSignup;
