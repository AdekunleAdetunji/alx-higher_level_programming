#!/usr/bin/node
/*
A script that computes the number of tasks completed by user id
*/

const request = require('request');
const url = `${process.argv[2]}?completed=true`;
const result = {};
function reqCallback (err, response, body) {
  if (!err) {
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      const key = `${task.userId}`;
      if (result[key]) {
        result[key]++;
      } else {
        result[key] = 1;
      }
    }
    console.log(result);
  }
}

request.get(url, reqCallback);
