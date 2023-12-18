//Not many users of php at leetcode. Pointless to mention the performance. 
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxProductDifference($nums) {
        $length = count($nums);
        sort($nums);
        
        $firstBig = end($nums);
        $secondBig = prev($nums);
        $secondLast = reset($nums);
        $firstLast = next($nums);

        return $firstBig*$secondBig - $firstLast*$secondLast;
    }
}
