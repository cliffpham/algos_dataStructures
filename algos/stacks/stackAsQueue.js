class Stack 
{ 
	// Array is used to implement a Queue 
	constructor() 
	{ 
        this.items = []; 
	} 
				
	// Functions to be implemented 
    // enqueue(item) 
    addToStack(el) {
        this.items.push(el);
    }
    // dequeue() 
    removeFromStack() {
        if(this.isEmpty()){
            throw Error('no items in stack');
        }
        return this.items.pop();
    }
    // isEmpty() 
    // isEmpty function 
    isEmpty() { 
	// return true if the queue is empty. 
	    return this.items.length === 0; 
    } 

    // printStack function 
    printStack() { 
	    var str = ""; 
	    for(var i = 0; i < this.items.length; i++) 
		str += this.items[i] +" "; 
	    return str; 
    } 

    stackAsQueue(stack1, stack2){
        
        if(stack2.isEmpty()){
            while(stack1.items.length > 0){
                stack2.items.push(stack1.items.pop());
            }

        // } else {
        //     while(stack2.items.length > 0){
        //         stack1.items.push(stack2.items.pop());
        //     }

        //     console.log(stack1)

        //     while(stack1.items.length > 0){
        //         stack2.items.push(stack1.items.pop());
        //     }
        //     console.log(stack2)
        // }
    
         return stack2.items.pop();     
    }

    if(stack1.isEmpty()){
        while(stack2.items.length > 0){
            stack1.items.push(stack2.items.pop());
        }
        return stack1.items.pop();
    }
} 

// function stackAsQueue(){
//     var stack1 = ['a','b','c']
//     var stack2 = [];

//     function isEmpty(stack){
//         return stack.length === 0
//     }

//     if(isEmpty(stack2)){
//         while(stack1.length > 0){
//             stack2.push(stack1.pop());
//         }
//     } else {
//         while(stack2 > 0){
//             stack1.push(stack2.pop());
//         }
//     }

//     return stack2;
}

//test case

// var stack1 = new Stack();
// var stack2 = new Stack();
// stack1.addToStack('a');
// stack1.addToStack('b');
// stack1.addToStack('c'); 
// stack2.addToStack('1');
// stack2.addToStack('2');
// stack2.addToStack('3');
// console.log(stack1.printStack());
// console.log(stack1.stackAsQueue(stack1, stack2));