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
// console.log(isValid('()'));
// console.log(isValid('()[]{}'));
// console.log(isValid('(]'));
// console.log(isValid('(])'));
// console.log(isValid('({[]})'));
// console.log(isValid(""));

// Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

// Any left parenthesis '(' must have a corresponding right parenthesis ')'.
// Any right parenthesis ')' must have a corresponding left parenthesis '('.
// Left parenthesis '(' must go before the corresponding right parenthesis ')'.
// '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
// An empty string is also valid.

var checkValidString = function(s) {
    var arr = s.split('');

    function checkString(s, arr){
        if(s === ""){
            return true;
        }

        if(arr.length < 2 && s !== '*') {
            return false;
        }
    
        var stack = [];

        for(let i = 0; i < arr.length; i++){
            if(arr[i]==='('){
                if(arr[i+1] === '*' && arr[i+2] === ')') {
                    continue;
                }
                stack.push(arr[i]);
            }

            if(arr[i] === ')'){
                if(arr[i-1] === ')' && arr[i-2] === '*' && arr[i-3] === '('){
                    continue;
                }

                if(stack.length > 0){
                    if(stack[stack.length - 1] === '(' || stack[stack.length - 1] === '*' ){
                        stack.pop();
                    } else {
                        return false;
                    }
                }

            }

            if(arr[i] === '*'){
                if(arr[i-1] === '(' && arr[i+1] ===')'){
                    continue;
                }

                if(stack.length > 0) {
                    if(stack[stack.length - 1] === '(' || stack[stack.length - 1] === '*'){
                        stack.pop();
                    }
                }

                stack.push(arr[i]);
            }
        }

        if(stack.length === 0){
            return true;
        } else {
            if(stack.length === 1 && stack[0] === '*'){
                return true;
            }
            return false;
        }
    }

    return checkString(s,arr);
};

console.log(checkValidString('(*))'));
console.log(checkValidString('((*)'));
// console.log(checkValidString('()'));
// console.log(checkValidString('*'));
// console.log(checkValidString('(*'));
// console.log(checkValidString('((*))'));
// console.log(checkValidString(')*'));
// console.log(checkValidString('(*('));
// console.log(checkValidString('()(*('));
// console.log(checkValidString('(****)'));
// console.log(checkValidString('***'));
// console.log(checkValidString('(*)'));
console.log(checkValidString("(*(()))((())())*(**(()))((*)()(()))*(())()(())(()"));



