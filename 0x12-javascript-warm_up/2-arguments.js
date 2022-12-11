#!/usr/bin/node

// Get the number of arguments passed to the script
const argCount = process.argv.length - 2;

// Print the appropriate message based on the number of arguments
if (argCount === 0) {
  console.log('No argument');
} else if (argCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
