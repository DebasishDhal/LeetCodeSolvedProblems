'''
You are given an array of strings words (0-indexed).
In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].
Return true if you can make every string in words equal using any number of operations, and false otherwise.

Example 1: Input: words = ["abc","aabc","bc"]
Output: true. Explanation: Move the first 'a' in words[1] to the front of words[2], to make words[1] = "abc" and words[2] = "abc". All the strings are now equal to "abc", so return true.
'''

#We can do all the operations, but if there are not enough strings to be redistributed among the words, then it won't be possible. In other words, every single character found int the array
#should be divisible by the total number of words in the array.

#Not an optimal solution, the counter is eating a lot of time.
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        #The obvious method is looping through every word and every char and add count them in a dictionary.
        #But the words don't need to be counted separately. It makes us eliminate one for loop.
        from collections import Counter
        combined = ''.join(words)
        counter_dict = dict(Counter(combined))
        print(counter_dict)
        return all(i%n == 0 for i in counter_dict.values())
