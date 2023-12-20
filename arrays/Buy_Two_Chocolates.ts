function buyChoco(prices: number[], money: number): number {
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
//   console.log(first,second)

  if (first+second > money){
    return money
  }
  
  else{
    return money - first - second
  }
};
