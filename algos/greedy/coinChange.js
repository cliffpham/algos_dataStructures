function coinChange (coins, target, i = 0, results = []){
    //first sort the coins from largest to smallest
    coins = coins.sort((a,b) => b - a);

    while(target >= coins[i]){
        target -= coins[i]

        if(target >= 0){
            results.push(coins[i]);
        }
        while(target < coins[i]){
            i++
        }
    }
    return results;
}

console.log(coinChange([10,5,1], 48));
console.log(coinChange([200,10,1,100,50], 526));
