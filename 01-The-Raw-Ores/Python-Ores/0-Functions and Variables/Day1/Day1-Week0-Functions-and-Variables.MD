
# 🐍 Python Concept: [Day 01 - First Setup and Getting Started]
  
*This note is written with the help of [StackEdit](stackedit.io) and [EmojiCopy](emojicopy.com)*
**Date:**  March 20th, 2026 - [13:10-15:00]
**Tags:**  `#python`, `#primitive-ai`, `#self-study`, `#cs50_2026`, `#harvard_university` `#edX` `#VSCode`
**Time spent**:  *`1 hour and 30 minute`*
**Course infos**: [Course | CS50's Introduction to Programming with Python | edX](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/home?audit_mode=)
**Track:** 
- From: [Introduction to course](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@a1450ed5620843fe9fd548156a385d26)
- To: [Functions and Variables in Python](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@744dad66fcce478a92fb1073b3d373fa/block-v1:HarvardX+CS50P+Python+type@vertical+block@50897469e09545f29c4535c6ffb2c704)
## 🎯 Objective

* Get used to with Python programming languages, installing and first set up for python
* Functions and Variables

  
## 📝 Core Notes

*First of all, you will need to know how to write and run code*
-  **1. Functions & Variables:**
	1. Functions: 
	-	An action or a verb that let you do something in the program.
	-	Some PL (programming languages) have some predetermined set of functions like some very basic acionts or verbs that the computer will already know how to do it
	-	You can determine your own function as well
	```py
	print('Adding text to inform');
	#Input function:
	input() #--> Doesn't need to take any arguments -> it takes its own argument and waiting for the user input
	#or you can just add String with a quotation mark to inform the user whether what they need to do next (it's only accepting String as an arguments)
	#For e.g
	input("What is your name?");
	```

2. Arguments:
	- An input to a function that somehow influences its behaviors
	- In functions there can be more than 2 arguments and it's separated by each comma.
	- *Note that if it's a print function and it's a string then it will automatically add space letter if the argument is not at first argument position.*
	```py
	name = "gei";
	print("Why are you", name); #--> No need to adding space after the first string because in Python when you passing more than two arguments and it's both a String then it will automatically add space after it.
	```
3. Side effects: Generally, are something that we want to happen after a function is called, like display on the screen with the print function ,.. etc.
4. Bugs:
	- It is a mistake in a program, and they can take so many forms.
5. Variables:
	- Just a container to store some value inside of a computer or inside of your own programs.
	- It would be better to works with **return values** to pass value inside an variable for reuseable .
	-  '=' gain a crucial role in programing, it doesn't mean equal per se but in programing it's mean more like an **assignment operator** where you can assign values into a variable.
	##### How to declare a variable?
	```py
	x = 19;  #x is this case is a variable
	```
	
6. Comments: 
	- Note to yourself and others whom working with your project in your code.
	- It's recommended to adding comments on each function or block of code to remind yourself and others to know what they are doing with?
	- In Python to note a code you should put a ```#``` before you start writing a comment or you can add 3 double quote like this """Comment inside """ for serveral line comment.
	```py
	# For single line comment
	"""
	Three double quote for multiple line comments 
	"""
	```
	- You can also use it as an outline for your thought before coding and it's called Pseudocode
7. Pseudocode:
	- Isn't a formal (in code) thing, you can just use a normal text to express your thoughts succinctly, methodically, algorithmically for a code, algorithms, functions, etc. 
-  **2. Operators:**
There are various kind of operators in each programming language and in Python per se.
**For example:** The + operators can be used in both String and Number in Python and it have different meaning.
In Number it is addition
```py
	number = 1 + 2;
	#--> Number = 3
```
In String, it's more like of a join or concatenation from the left String to right.
```py
	name = "gei";
	print("Why are you " + name); #--> Need to adding space after the first string because it's different like the comma operators?
```


## New Major Keywords
* Interpreter(n): software executing ran from top to bottom, left and right on the source code and convert it into binary for the computer to understand.
* Albeit(conjunction): even though, although, etc.
* Aesthetic(adj)
* Succinctly(adv): in a brief or cleanly expressed manner

## 💻 Code Snippets

```py
// Drop your isolated, working examples here to reference later
#include  <iostream>
int  main() {
std::cout << "Forging the Dumb Stack..." << std::endl;
return  0;
}

```
## 📋🎗️ Reminder/ To-do Task

- Learn to read the documentation.

- Updating the operators section?

-

-
#### Learning resources:
[Python Documents](https://docs.python.org)
#### Other resources:
***Extensions usage:***
- LiveServer on VSCode
- Page Ruler on Browser
* This note is written with the help of [StackEdit](stackedit.io) and [EmojiCopy](emojicopy.com)
