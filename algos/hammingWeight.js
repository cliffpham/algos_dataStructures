// Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

var hammingWeight = function(n) {
    n = n.toString(2)
    var count = 0;

    for(let i = 0; i < n.length; i++) {
        if(n[i] === '1'){
            count++
        }
    }

    return count;
};

console.log(hammingWeight(128));