function mergeSort(array){
    //base case
    if(array.length < 2){
        return array
    }

    var left = array.slice(0, array.length / 2);
    var right = array.slice(array.length / 2, array.length)

    left = mergeSort(left);
    right = mergeSort(right);

    return merge(left, right);
}

function merge(leftArray, rightArray){
    var results = [];

    while(leftArray.length > 0 && rightArray.length > 0) {
        if(leftArray[0] > rightArray[0]){
            results.push(rightArray[0]);
            rightArray.shift();
        } else {
            results.push(leftArray[0]);
            leftArray.shift();
        }
    }

    while(leftArray.length > 0){
        results.push(leftArray[0]);
        leftArray.shift();
    }

    while(rightArray.length > 0){
        results.push(rightArray[0]);
        rightArray.shift();
    }

    return results;
}

console.log(mergeSort([4,3,8,2,5]));
