# CS4450_5450_PA-1
ASU CS 4450/5450 Networking Class Programming Assignment 1 

This semester you will be required to write several distributed applications in Python 3.  Since some of you will not have any prior experience programming in Python, this assignment is designed to provide an introduction.  In particular, much of the work of later assignments will require manipulating strings and this assignment provides some experience with that.  In addition, this assignment will expose you to both functions and classes in Python.

This website provides an overview of topics in Python 3: https://docs.python.org/3/tutorial/index.html  Since I already have programming skills, when I learn a new language, I'm mostly interested in just figuring how to do in this new language what I already know how to do in another language.  So for me, it is a matter of looking things up by using the reference indicated above.

However, if you would rather complete a short Python course, those resources are available too.  Simply use Google to find a "Python 3 course".  Some courses are free or of nominal cost.  

Be aware that we will be using Python 3 this semester.  There are some significant differences between Python 3 and Python 2.

Getting Started

We will be using git and GitHub this semester for handing outcode and collecting programming assignments.  If you don't already have a GitHub account, you need to use a browser to visit github.com and create one.

You can grab the starting code by:

1) Use a browser to visit github.com and log in.
2) Visit the link: https://classroom.github.com/a/2R2hPr33. This will display a page where you will accept the assignment and then create a repository at GitHub that contains the starting code for this programming assignment. If you then click on the link that takes you to the repository, you can grab the URL to be used in the clone command on the student2 machine.

Now, log into the student2 machine.

If you have never used git on the student2 machine, you need to execute the following commands:

git config --global user.name "Firstname LastName"
git config --global user.email "your email address"

Use the same email address that you used when you created your github account.

Get into your 4450 or 5450 directory and clone the repository that was created by typing this: 

git clone https://<use URL specified by github>

Your repository will consist of three files that you will work on: driver.py, stringlib.py, and worker.py

The Work

Your task is to implement the string functions described in stringlib.py.  You will add calls to the testStringLib function in driver.py to test those string functions.

After you get those working, you will define a Worker class as described in worker.py.  You will add calls to the testWorkerClass function in driver.py to test the methods in the Worker class. 

At the top of the driver.py is the line:

#! /usr/bin/python3

The #! sequence is a "shebang".  It is used to indicate to the shell that the path that follows is the path to the executable that will be used to interpret the python script.

In order for this to work, the file needs to be executable.   Notice that the file listed below can be executed by the owner (indicated by the first "x") and the group (indicated by the second "x").  

student2.cs.appstate.edu> ls -l driver.py
-rwxrwx---. 1 can can 855 Aug 21 12:59 driver.py

If your file is not executable, you need to make it so by typing:

chmod a+x driver.py

The driver.py expects a string as a command line argument and displays usage information if you don't give it a string:

student2.cs.appstate.edu> ./driver.py 
usage: driver1.py <string>

After you get your program working, it should produce output like this:

student2.cs.appstate.edu> ./driver.py "hello there"

Test stringlib:
    Input string is hello there
    Reverse of string is ereht olleh
    Does string contain apple? No
    Does string contain banana? No
    Is string a palindrome? No
    Uppercase of string is HELLO THERE

Test Worker class:
    Input string is hello there
    Reverse of string is ereht olleh
    Does string contain apple? No
    Does string contain banana? No
    Is string a palindrome? No
    Uppercase of string is HELLO THERE

Notice that my program tests the containsWord function and method with the strings "apple" and "banana".   You should also add tests similar to that.

student2.cs.appstate.edu> ./driver.py "helloappleslice"

Test stringlib:
    Input string is helloappleslice
    Reverse of string is ecilselppaolleh
    Does string contain apple? Yes
    Does string contain banana? No
    Is string a palindrome? No
    Uppercase of string is HELLOAPPLESLICE

Test Worker class:
    Input string is helloappleslice
    Reverse of string is ecilselppaolleh
    Does string contain apple? Yes
    Does string contain banana? No
    Is string a palindrome? No
    Uppercase of string is HELLOAPPLESLICE

Be sure push your code to github before the due date for grading.  First, add the files you changed.  You can add them all at once by typing:

git add .

or instead of the ., you can add them individually:

git add driver.py

Then, you need to commit the changes by typing:

git commit -m "Completed programming assignment"

Finally, you'll push the committed code to the repository on GitHub:

git push origin master

The push will require you to enter your GitHub username and password.
