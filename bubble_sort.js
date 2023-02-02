'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function countSwaps(a) {
    // Write your code here
    let swapCount = 0
    
    for(let _ of a){
        for(let i = 0; i < a.length - 1; i++){
            if(a[i] > a[i + 1]){
                [a[i], a[i + 1]] = [a[i + 1], a[i]]
                swapCount++
            }
        }
    }
    
    console.log(`Array is sorted in ${swapCount} swaps.`)
    console.log(`First Element: ${a[0]}`)
    console.log(`Last Element: ${a[a.length - 1]}`)

}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const a = readLine().replace(/\s+$/g, '').split(' ').map(aTemp => parseInt(aTemp, 10));

    countSwaps(a);
}
