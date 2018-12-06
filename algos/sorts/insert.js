
function insertionSort(array) {
    var length = array.length;
    
    for(var i = 1, j; i < length; i++) {
      var temp = array[i];
      console.log('this is i: ' + i);
      console.log('this is temp: ' + temp);
      console.log('this is array[j]: ' + array[i-1]); 
      for(var j = i - 1; j >= 0 && array[j] > temp; j--) {
        console.log('Hit innner loop. This is j: ' + j);
        console.log('this is array[j+1] before entering the loop: ' + array[j+1]);
        array[j+1] = array[j];
        console.log('this is array[j+1] inside the loop: ' + array[j+1]);
        console.log(array);
      }
      console.log('this is j outside its own loop: ' + j);
      array[j+1] = temp;
      console.log('this is array[j+1] outside the j loop: ' + array[j+1]);
      console.log(array);
    }
    
    return array;
  }

  console.log(insertionSort([4,3,8,2,5]));