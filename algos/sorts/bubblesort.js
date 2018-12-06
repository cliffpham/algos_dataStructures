function bubbleSort (arr) {
    function swap(arr, i, j) {
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

        return arr
    }


    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if(arr[j] > arr[i]){
                swap(arr, i, j);
            }
        }
    }

    return arr
}

console.log(bubbleSort([4,3,8,2,5]));
console.log(bubbleSort([4,2,3,8,2,5,100,-50]));