/*
Beats 26% users only
*/
function totalMoney(n: number): number {
        let dayno = 1
        let weekbase = 1
        
        let total = 1

        while (dayno != n){
            if (dayno%7 == 0){
                weekbase = weekbase + 1
            }
            let dailyamount = weekbase + (dayno)%7
            total += dailyamount
            dayno += 1
        }

        return total
};
