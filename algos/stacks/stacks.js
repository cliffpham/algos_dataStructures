// Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid

var isValid = function(s) {
    var arr = s.split('');

    function checkParantheses(s,arr) {
        var stack = [];
        
        if(s === ""){
            return true;
        }
    
        if(arr.length < 2) {
            return false;
        }

        for(let i = 0; i<arr.length; i++){
            
            if(arr[i] === '(' || arr[i] === '[' || arr[i] === '{'){
                stack.push(arr[i])
            } 

            if(arr[i] === ')'){
                if(stack[stack.length - 1] === '(') {
                    stack.pop();
                } else {
                    return false;
                }
            }

            if(arr[i] === ']'){
                if(stack[stack.length - 1] === '[') {
                    stack.pop();
                } else {
                    return false;
                }
            }

            if(arr[i] === '}'){
                if(stack[stack.length - 1] === '{') {
                    stack.pop();
                } else {
                    return false;
                }
            }
   
            }

            return stack.length === 0;            
        }
    
    return checkParantheses(s,arr);
};


// Tests
console.log(isValid('()'));
console.log(isValid('()[]{}'));
console.log(isValid('(]'));
console.log(isValid('(])'));
console.log(isValid('({[]})'));
console.log(isValid(""));