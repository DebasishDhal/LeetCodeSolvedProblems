/*
Beats 97% of users in runtime.

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
*/
var totalMoney = function(n) {
        let dayno = 1
        let weekbase = 1
        
        let total = 1

        while (dayno != n){
            if (dayno%7 == 0){
                weekbase = weekbase + 1
            }
            dailyamount = weekbase + (dayno)%7
            total += dailyamount
            dayno += 1
        }

        return total

};
