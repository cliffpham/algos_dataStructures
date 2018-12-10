function quickSort(arr){    
    function main(arr, start, end){  
        if(start >= end){
            return;
        }
        
        var pIndex = partition(arr,start,end);
        main(arr, start, pIndex - 1);
        main(arr, pIndex + 1, end);

        return arr;
    }

    function partition(arr,start,end){
        var randomNum = Math.floor(Math.random() * (end - start + 1) + start);
        swap(arr, randomNum, end);
        var pivot = arr[end];
        var pIndex = start;
        // var pivot = arr[end];

        for(let i = start; i < end; i++){
            if(arr[i] < pivot){
                swap(arr,i, pIndex);
                pIndex++;
            }
        }

        swap(arr, pIndex, end);

        return pIndex
    }

    function swap(arr, a, b){
        var temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    
    return main(arr, start = 0, end = arr.length - 1);
}


console.log(quickSort([7,2,1,6,8,5,3,4]));
console.log(quickSort([4,2,3,8,2,5,100,-50]));
console.log(quickSort(createRandomArray(500,10)));
console.log(quickSort(createRandomArray(500,10)));
console.log(quickSort(createRandomArray(500,10)));


function createRandomArray(range, size) {
    var arr = [];
    for(let i = 0; i < size; i++){
        arr[i] = Math.floor(Math.random() * range);
        arr.push(arr[i]);
    }

    return arr
}
