//Intial solution for leetcode lemonade change

function lemonadeChange(bills){
    var register = [];
    var index = 0;

    function change(register, amount){
        register = register.sort((z,y) => y - z);

        while(register.length >= 1){
            amount -= register[register.length - 1]
            register.pop();

            if(amount === 15 && register[0] == 10){
                amount -= register[0]
                register.shift();
            }

            if(amount === 5){
                return true;
            }        
        }

        return false;
    }

    while(index < bills.length){
        if(bills[index] === 5){
            register.push(bills[index]);
            index++;

        } else {
            if(change(register, bills[index])){
                if(bills[index] != 20){
                register.push(bills[index]);
                }
                index++;

            } else {
                return false;
            }
        }
    }
    return true;
}

// console.log(lemonadeChange([5,5,5,10]));
// console.log(lemonadeChange([5,5,5,10,5,20,5,10,5,20]));
// console.log(lemonadeChange([5,5,5,10,20]));
// console.log(lemonadeChange([5,5,10,20]));
// console.log(lemonadeChange([5,5,10,10,20]));
// console.log(lemonadeChange([10,10]));
// console.log(lemonadeChange([5,20]));


