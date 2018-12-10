var isPalindrome = function(s) {
  var hist = {};

  for (char of s) {
    char = char.toLowerCase();
    char = char.charCodeAt(char);

    if (char > 96 && char < 123) {
      if (!hist[char]) {
        hist[char] = 1;
      } else {
        hist[char]--;
        if (hist[char] === 0) {
          delete hist[char];
        }
      }
    }
  }

  if (Object.keys(hist).length > 1) {
    return false;
  } else {
    return true;
  }
};

console.log(isPalindrome("Radar"));
console.log(isPalindrome("A man, a plan, a canal: Panama"));
console.log(isPalindrome("race a car"));
console.log(isPalindrome("OP"));
console.log(isPalindrome(""));
console.log(isPalindrome(""));
console.log(isPalindrome("."));
