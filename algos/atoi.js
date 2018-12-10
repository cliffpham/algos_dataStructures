// atoi without using parseInt

function atoi (str){
    var int = 0;
    var initval = 1;
    var initvalFlag = false;
    var operationFlag = false;
    var stringIsValid = 0;

    for(let i = 0; i < str.length; i++){
        if(str[i] == ' ' && operationFlag == false) {
            continue;
        }

        else if(str[i] == '-' && initvalFlag == false && operationFlag == false){
            initval = -1;
            initvalFlag = true;
            operationFlag = true;
            continue;
        } 

        else if(str[i] == '+' && initvalFlag == false && operationFlag == false){
            initvalFlag = true;
            operationFlag = true;
            continue;
        } 
        
        else {
            curr = str.charCodeAt(i);
            if(curr > 47 && curr < 58) {
            stringIsValid++;
            operationFlag = true;
            int = int * 10;
            int += str[i] * initval;            
            } else {
                if(stringIsValid == 0) {
                    break;
                }
                if(curr == 46){
                    break;
                }
                if(stringIsValid >= 1 && operationFlag != false){
                    break;
                }
            }
        }
    }

    // check if the integer is in range

    if(int < (Math.pow(-2, 31))){
        return Math.pow(-2,31)
    }

    if(int > (Math.pow(2, 31) - 1)){
        return Math.pow(2,31) - 1
    }

    return int;
}

console.log(atoi('  123'))
console.log(atoi('-123'))
console.log(atoi('4193 with words'))
console.log(atoi('words and 987'))
console.log(atoi('-0012a42'))
console.log(atoi(' +0 123'))
console.log(atoi('-91283472332'))
console.log(atoi('3.14159'))
console.log(atoi('314.159'))
console.log(atoi('-314.159'))
console.log(atoi('-3'))
console.log(atoi('+3.45'))
console.log(atoi('+-2'))
console.log(atoi('-  234'));
console.log(atoi('0-1'));
console.log(atoi(" b11228552307"))

