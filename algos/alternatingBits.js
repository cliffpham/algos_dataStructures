// Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

var hasAlternatingBits = function(n) {
    n = n.toString(2);

    for (let i =0; i < n.length; i++) {
        if(n[i] === n[i+1]) {
            return false;
        }
    }
    return true;
};

console.log(hasAlternatingBits(5));
console.log(hasAlternatingBits(7));
console.log(hasAlternatingBits(11));