#!/usr/bin/node
/*
A script that computes the number of tasks completed by user id
*/

const request = require('request');
const url = `${process.argv[2]}?completed=true`;
function reqCallback (err, response, body) {
  if (!err) {
    const todos = JSON.parse(body);
    const completed = {};
    todos.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });
    console.log(completed);
  }
}

request.get(url, reqCallback);
