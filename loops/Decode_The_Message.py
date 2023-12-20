'''
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.
'''

# Constraints:

# 26 <= key.length <= 2000
# key consists of lowercase English letters and ' '.
# key contains every letter in the English alphabet ('a' to 'z') at least once.
# 1 <= message.length <= 2000
# message consists of lowercase English letters and ' '.

# Simple solution, Beats 83% of users. First I thought of putting a try except in decoding loop, but that makes the program slow. Try-except could be removed by adding the ' ' to the mapping dictionary.
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapDict = {' ': ' '}
        fill_list = [' ']
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        pos = 0
        for char in key:
            if char in fill_list:
                continue
            mapDict[char] = alphabet[pos]
            pos += 1
            fill_list.append(char)
        print(mapDict)

        decoded = ''
        for char in message:
            decoded += mapDict[char]
        return decoded
