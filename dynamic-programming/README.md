It's hard to express how much I hate dynamic programming, especially that notation ```dp```. I can't call it garbage, because it solves so many problems. It just takes time to adopt it.

_To understand dynamic programming, you'll require dynamic programming._

I created a very nice solution to a daily problem (hard). It goes like this. Question [Link](https://leetcode.com/problems/string-compression-ii/?envType=daily-question&envId=2023-12-28). It worked for 66 test cases. But it was my mistake, I forgot that ```aaabaaccc``` is compressed as ```a3ba2c3```, and not as ```a5bc3```. Then, I looked at the hint, it said **USE DYNAMIC PROGRAMING**. I'm keeping this code, as a sort of memory 🥲.
```
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        from collections import Counter
        count_dict = dict(Counter(s))

        print(count_dict)
        red_dict = {i[0]: min(item for item in [ i[1] - 99, i[1] - 9, i[1] ] if item > 0) for i in count_dict.items()} #Reduction distance
        print(red_dict, end = '\n\n')
        loop = 0
        while k>0:
            print(f"loop = {loop}")
            loop += 1
            min_item, count = min(red_dict.items(), key = lambda x:x[1])
            # k = max(k-count,0)
            k = k - count
            print(f"min_item = {min_item}, count = {count}, k ={k}")
            actual_count = count_dict[min_item]

            if actual_count == count:
                if k > 0:
                    del red_dict[min_item]
                    del count_dict[min_item]    
                    print(f"key = {min_item} deleted")
                else:
                    count_dict[min_item] -= k+count
                    red_dict[min_item] -= k+count
            else:
                red_dict[min_item] = min(item for item in [ actual_count - count - 99, actual_count - count - 9, actual_count - count ] if item > 0)
                count_dict[min_item] -= count

        print(count_dict)

        new_string = ""
        for i in count_dict.items():
            if i[1] > 1:
                new_string += i[0]+str(i[1])
            if i[1] == 1:
                new_string += i[0]
        print(new_string)
        return len(new_string)
```
