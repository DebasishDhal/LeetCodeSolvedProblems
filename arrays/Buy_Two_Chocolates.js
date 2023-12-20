/**
 * @param {number[]} prices
 * @param {number} money
 * @return {number}

 You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.
Constraints:

2 <= prices.length <= 50
1 <= prices[i] <= 100
1 <= money <= 100
 */

//Unoptimized solution
var buyChoco = function(prices, money) {
    prices = prices.sort((a,b)=>(a-b))
    // console.log(prices)
    if (prices[0]+prices[1]>money){
        return money
    }

    else {
        return money-prices[0]-prices[1]
    }

};

//Optimized solution
var buyChoco = function(prices,money){
  let first = 101
  let second = 101

  for (let item of prices){

    if (item < second){
      [first, second] = [second, item]
    }

    else if (item < first){
      first = item
    }

}

  if (first+second > money){
    return money
  }
  
  else{
    return money - first - second
  }
};
