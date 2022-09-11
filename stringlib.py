#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
#
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
#
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
#
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
#

def reverseStr(s):
    rev = ''
    for i in range(len(s) - 1, -1, -1):
        rev += s[i]
    return rev

def containsWord(containingStr, containedStr):
    found = containingStr.find(containedStr)
    if found < 0:
        return "No"
    return "Yes"

#Racecar
def isPalindrome(s):
    for i in range(0, len(s)):
        if s[i] != s[(len(s)-1) - i]:
            return "No"
        if i == (len(s)-1) - i:
            return "Yes"

def upperCaseStr(s):
    return s.upper()