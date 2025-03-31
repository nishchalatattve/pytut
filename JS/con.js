// For loop equivalent
for (let i = 0; i < 9; i++) {
    console.log(i);
}

// While loop equivalent
let count = 0;
while (count < 9) {
    console.log(count);
    count += 1;
}
count = 0;

// // Random number generation and conditional statements
// // JavaScript doesn't have NumPy, but we can use Math.random()
// // Generate random number between -10 and 10
let a = Math.random() * 20 - 10;

if (a < 5) {
    console.log(`${a} is less than 5`);
} else if (a === 5) {
    console.log(`${a} is equal to 5`);
} else {
    console.log(`${a} is greater than 5`);
}