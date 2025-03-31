// Variable types

// ---------------- Simple ----------------
// JavaScript doesn't have type annotations like Python
// but we can use similar variables
let a = 99;
console.log(a); // 99

let b = 99.99;
console.log(b); // 99.99

let c = true;
console.log(c); // true

let d = 'h';
console.log(d); // 'h'

// In JavaScript, variables can be reassigned to different types
a = "hi";
console.log(a); // "hi"

// ---------------- Composite ----------------
let myNameArray = ["Chris", "Bob", "Jim", c];
console.log(myNameArray); // ["Chris", "Bob", "Jim"]

let dog = { name: "Spot", breed: "Dalmatian" };
console.log(dog); // { name: "Spot", breed: "Dalmatian" }