#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
  console.log('0');
} else {
  let first = 0;
  let sec = 0;

  for (let a = 0; a < args.length; a++) {
    if (args[a] > first) {
      sec = first;
      first = args[a];
    } else if (args[a] > sec && args[a] < first) {
      sec = args[a];
    }
  }

  console.log(sec);
}
