var evalRPN = function(tokens) {
    var stack = [];
    var operator;
    var a;
    var b;


    var operate = [];
    for(let i = 0; i < tokens.length; i++){
        var curr = parseInt(tokens[i]);
        if(isNaN(curr)) {
            operate.push(tokens[i]);
        } else {
            operate.push(curr);
        }
    }

    for(let i = 0; i < operate.length; i++){
        if(!Number.isInteger(operate[i])){
            operator = operate[i];
            a = stack.pop();
            b = stack.pop();

            switch(operator){
                case '+': 
                    stack.push((a + b));
                    break;
                case '-':
                    stack.push(Math.abs(a - b));
                    break;
                case '*':
                    stack.push((a * b));
                    break;
                case '/':
                    stack.push(Math.trunc(b / a));
                    break;
            }
        } else {
            stack.push(operate[i]);
        }
    }
    return stack[0];
};

console.log(evalRPN(["4","3","-"]))
console.log(evalRPN(["4", "13", "5", "/", "+"]))
console.log(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]));