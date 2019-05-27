# -*- coding:utf-8 -*-

#QUESTION DESCRIPTION
'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, 
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. 
For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). 
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.
Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Note:
The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.

'''

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        noRepeatMorseList = self.rmRepeatMorseList(self.LettersListToMorseList(self.wordsToLetterList(words)))
        return len(noRepeatMorseList)

    def wordsToLetterList(self,wordList):
        """
        把列表里每个单词变成字母列表
        """
        lettersList = []
        for word in wordList:
            lettersList.append(list(word))
        return lettersList

    def LettersListToMorseList(self,lettersList):
        """
        把字母列表的列表变成摩尔斯列表
        """
        morseList = []
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabatList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        for word in lettersList:
            temString = ''
            for letter in word:
                temString += morseCode[alphabatList.index(letter)]
            morseList.append(temString)
        
        return morseList


    def rmRepeatMorseList(self,morseList):
        """
        给得到的摩尔斯码的列表去重
        """
        noRepeatMorseList = []
        for morse in morseList:
            if morse not in noRepeatMorseList:
                noRepeatMorseList.append(morse)
            else:
                continue
        return noRepeatMorseList

