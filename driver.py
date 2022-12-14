#!/bin/python3

#import the code in string1.py

from stringlib import *
from worker import *
import sys

#Function to test the functions in the stringlib module
def testStringLib(inputStr):
    #Add code to call each of the functions and print the results
    print(f"  Input string is {inputStr}")
    rev = reverseStr(inputStr)
    print(f"  Reverse of string is {rev}")
    contains = containsWord(inputStr, "Hello")
    print(f"  Does string contain Hello? {contains}")
    contains = containsWord(inputStr, "apple")
    print(f"  Does string contain apple? {contains}")
    pal = isPalindrome(inputStr)
    print(f"  Is string a palindrome? {pal}")
    upper = upperCaseStr(inputStr)
    print(f"  Uppercase of string is {upper}")
    return

#Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    #Add code to create a Worker object
    #Use the object to call each of the methods in the Worker class
    #Print the result of each call
    w = Worker(inputStr)
    print(f"  Input string is {inputStr}")
    rev = w.reverseStr()
    print(f"  Reverse of string is {rev}")
    contains = w.containsWord("hello")
    print(f"  Does string contain hello? {contains}")
    contains = w.containsWord("apple")
    print(f"  Does string contain apple? {contains}")
    pal = w.isPalindrome()
    print(f"  Is string a palindrome? {pal}")
    upper = w.upperCaseStr()
    print(f"  Uppercase of string is {upper}")
    return

#check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    #call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])




