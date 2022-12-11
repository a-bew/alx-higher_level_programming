#!/usr/bin/node

// Get the first and second arguments passed to the script
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Check if both arguments were provided
if (arg1 === undefined || arg2 === undefined) {
  console.log('Two arguments are required');
} else {
  // Print the arguments in the specified format
  console.log(`${arg1} is ${arg2}`);
}
