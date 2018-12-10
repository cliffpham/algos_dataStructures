function cocktailSort(arr){
    rightSwapIndex = 0;
    rightCounter = 1;
    leftCounter = 1;
    reset = 1;
    start = 0;

    while(rightCounter !== 0 || leftCounter !== 0){
        for(let i = start; i < arr.length; i++) {
            // console.log(i);
            if(arr[i] > arr[i+1]){
                // console.log('front swap: ' + arr[i] + ' | ' + arr[i+1]);
                swap(arr,i, i+1);
                rightSwapIndex = i;
                rightCounter++;
                // console.log(arr);
                // console.log('///////////////////////////////////////////////')
            } else {
                // console.log(arr);
            }
        }
    
        if(rightCounter > 1){
            rightCounter = reset;
        } else {
            rightCounter = 0;
        }
        // console.log('rightSwapIndex: ' + rightSwapIndex);
    
        for(let j = rightSwapIndex; j > 0; j--){
            // console.log(j);
            if(arr[j] < arr[j-1]){
                // console.log('back swap: ' + arr[j] + ' | ' + arr[j-1]);
                swap(arr,j, j-1);
                leftCounter++;
                // console.log(arr);
                // console.log('///////////////////////////////////////////////')
            } else {
                // console.log(arr);
            }
        }
    
        if(leftCounter > 1){
            leftCounter = reset;
        } else {
            leftCounter = 0;
        }

        start++;
        rightSwapIndex = 0;
    }

    function swap(arr, a ,b){
        temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    return arr;
}


// console.log(cocktailSort([5,1,4,2,8,0,2]));
// console.log(cocktailSort([399, 21, 400, 326, 260, 78, 440, 312, 435, 470, 470 ]));
// console.log(cocktailSort([88, 160, 433, 196, 457, 302, 6, 213, 128, 73, 73]));
// console.log('////////////////////////////////////////////////')
console.log(cocktailSort([ 29, 316, 309, 370, 242, 8, 406, 114, 73, 158, 158 ]));
// console.log('////////////////////////////////////////////////')
console.log(cocktailSort(createRandomArray(450, 12)));
console.log(cocktailSort(createRandomArray(450, 12)));
console.log(cocktailSort(createRandomArray(450, 12)));





// console.log(createRandomArray(500,10));


function createRandomArray(range, size) {
    var arr = [];
    for(let i = 0; i < size; i++){
        arr[i] = Math.floor(Math.random() * range);
        arr.push(arr[i]);
    }

    return arr
}

