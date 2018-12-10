function mergeSort(array){
    var leftIndex = 0;
    var rightIndex = 0;

    //base case
    if(array.length < 2){
        return array
    }

    var left = array.slice(0, array.length / 2);
    var right = array.slice(array.length / 2, array.length);

    left = mergeSort(left);
    right = mergeSort(right);

    return merge(left, right, leftIndex, rightIndex);
}

function merge(leftArray, rightArray, leftIndex, rightIndex){
    var results = [];

    while(leftArray.length > leftIndex && rightArray.length > rightIndex) {
        if(leftArray[leftIndex] > rightArray[rightIndex]){
            results.push(rightArray[rightIndex]);
            rightIndex++;
        } else {
            results.push(leftArray[leftIndex]);
            leftIndex++;
        }
    }

    while(leftArray.length > leftIndex){
        results.push(leftArray[leftIndex]);
        leftIndex++;
    }

    while(rightArray.length > rightIndex){
        results.push(rightArray[rightIndex]);
        rightIndex++;
    }

    return results;
}

function createRandomArray(range, size) {
    var arr = [];
    for(let i = 0; i < size; i++){
        arr[i] = Math.floor(Math.random() * range);
        arr.push(arr[i]);
    }

    return arr
}


console.log(mergeSort([4,3,8,2,5]));
console.log(mergeSort(createRandomArray(500,10)));
console.log(mergeSort(createRandomArray(500,10)));
console.log(mergeSort(createRandomArray(500,10)));
