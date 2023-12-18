class Solution {
    func maxProductDifference(_ nums: [Int]) -> Int {
        let sorted = nums.sorted();
        print(sorted);

        let len = nums.count;
        let firstBig = sorted[len-1];
        let secondBig = sorted[len-2];
        let firstSmall = sorted[0];
        let secondSmall = sorted[1];
        return firstBig*secondBig-firstSmall*secondSmall;
    }
}
