const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    
    // for(let s of str) {
    //     console.log(`${s}`)
    // }
    
    [...str].forEach((s) => console.log(s))
});