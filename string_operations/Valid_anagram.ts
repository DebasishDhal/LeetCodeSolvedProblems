/*
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Beats 52% of users.
*/

function isAnagram(s: string, t: string): boolean {
  if (s.length != t.length){
      return false
  }

  let counter = {}

  for (let string of s){
      if (string in counter){
          counter[string] += 1
      }
      else{
          counter[string] = 1
      }
  }

  for (let string of t){
      if (!(string in counter) || counter[string]==0){
          return false
      }

      else{
          counter[string] -= 1
      }
  }
  
return true
};
