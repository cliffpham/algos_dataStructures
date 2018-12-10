
function insertionSort(array) {
    var length = array.length;
    
    for(var i = 1, j; i < length; i++) {
      var current = array[i];

      for(var j = i - 1; j >= 0 && array[j] > current; j--) {
        array[j+1] = array[j];
      }
      array[j+1] = current;
    }
    
    return array;
  }

console.log(insertionSort([4,3,8,2,5]));
console.log(insertionSort([7,2,1,6,8,5,3,4]));
console.log(insertionSort([4,2,3,8,2,5,100,-50]));