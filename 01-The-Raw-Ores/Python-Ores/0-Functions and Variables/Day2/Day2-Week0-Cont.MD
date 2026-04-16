
# 🐍 Python Concept: [Day 02 - Functions and Variables Part 2]
  
*This note is written with the help of [StackEdit](stackedit.io) and [EmojiCopy](emojicopy.com)*
**Date:**  April 2nd, 2026 - [09:31-13:40]
**Tags:**  `#python`, `#primitive-ai`, `#self-study`, `#cs50_2026`, `#harvard_university` `#edX` `#VSCode`
**Time spent**:  *`2 hours, 52 minutes and 29 seconds`*
**Course infos**: [Course | CS50's Introduction to Programming with Python | edX](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/home?audit_mode=)
**Track:** 
- From: [01 - Functions and Variables in Python at 31:10](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@744dad66fcce478a92fb1073b3d373fa/block-v1:HarvardX+CS50P+Python+type@vertical+block@50897469e09545f29c4535c6ffb2c704)
- To: [Functions and Variables in Python](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@744dad66fcce478a92fb1073b3d373fa/block-v1:HarvardX+CS50P+Python+type@vertical+block@50897469e09545f29c4535c6ffb2c704)
## 🎯 Objective

* Get used to with Python programming languages, installing and first set up for python
* Functions and Variables

  
## 📝 Core Notes

-  **1.  str - String:**
* When printing string on python there are serverals way to do it but one of the most common and new feature have been adding to python for `print()` is.
***Instead:***
```python
name ="David Malan";
print("What is your", name);
```

***You can use it like this:***

```python
print(f"What is your {name}?");
```
String has different features, methods and build-in functions in python
*Some commons methods for string:* 
`str.strip()`: remove whitespace from str from the left or from to the right if there are abundant blank space on the string
`str.capitalize()`: capitalize just the very first letter.
`str.title()`: capitalize the first letter of each word.
`str.split(sep?)`:  split the string based on the sep (separator that have been indicating on the string)
```python
first, name = name.split(" "),
# It then will split into
first = "David";
last = "Malan";
```

* Note that: You can also use multiple methods in just a single line of one string:*
```python
	name = input().strip().tittle();
	#OR
	name.strip().title();
	# Remember that you need to use it carefully and prioritize which methods you gonna use first.
```  

-  **2. Docs Explaining**
`print(*objects, sep=" ", end="\n")`
-  **3. Parameters**
> *Basically, parameters and arguments are the same, but it has some different characteristic*

* `Positional parameters` Passing values to functions it will prioritize which value gonna pass in first, second, and so forth.
* `Named parameters` is the user-defined/ built-in parameters that have been set for its function.
	
-  **4. int - Integer**
> *In python, whatever you type it always consider it as text even if it's **number** so when working with python you will need a special function to indicating python that the number user type was not a text.*
> And `int` is not a type in python it's a function.

**Convert a number text into and `int` type function by**
```python
	x = input();
	y = input();
	z= int(x) + (int)y; # Convert x and y into number using (int)variable function.
```

**Some common operators you can use to works with `int`**
| Operators | Meaning | Usage | Explaining|
|---|---|---|---|
|+| Addition| 1+2=3 |Adding from left to right|
|-| Substraction| 1-2=3 |Adding from left to right|
|*| Multiplication| 1*2=2 |Adding from left to right|
|/| Divide| 4/2=2 |Adding from left to right|
|%| Modular| 4/3=1 |Adding from left to right|

-  **5. float - Decimal number**
> In python, there is a bound on showing just how precise a floating point value can be.

`round(number[, ndigits])`: Rounding a float number by decimal digits as wanted(optional).
You can using `f string` method to round a float with ndigits.
```python
x = 3/2;
print(f{x:.2f};
```

- brackets `[]` meaning optional when reading a document for coding/ programming language.
-  **6. Interactive mode**
- You can use python on `bash` or terminal by typing `python`. When it's indicating with `>>>` that's mean you are in the python's interactive mode.
-   **7. def - User-defined function**

**Syntax**
```python
def function([parameters]):
	# Block of codes
```
*Note that: Remember to Tab to write the block of code of its function because in python instead of using `{}` like in C or others. It use Tab as `{}` for the code that long to its function.*
*And also remembe

You can set the default value of parameters if the user doesn't pass an argument into the `def` function.
**For eg**
```py
def hello(to="Deafault value here"):
	print("Hello", to);
```
-   **8. Side Effect**
- So basically, the side effect of a function means it doesn't return back the value of the its function but just print an vice versa? 
-   **8. Return Values**
- Hand back the value of its function after the function doing its job.
-   **9. scope**
> Basically, python are like sequential execution (from top to bottom) so you must define it before run the next lines of codes that related to its functions, variables, etc.

- Scope refers to a variable only exist in the context in which you defined it
***Usually there is a coding convention for every programming language from C to Python which is separated by two spaces. For `main` and `user-defined` function to prevent scoping when coding.*** --> Which is kinda optional but recommended if you follow this convention.
**Syntax for main convention**
```py
#----------------For main space--------------
def main ():
	codes here
	...

#----------------For user-defined function----------------
def urFunction():
	codes here

main();
```

## Bonus, notes and teacher/ audience's questions:
- How to print a quotation mark?
> You can put quotation mark inside a `print()` by using single quote if you want adding double quotes to a string or on the other hands.
> There is also a usage of backlash `\` to print quotation marks or any special characters 
- Remove the spaces that might have been accidently added between each word when typing `input()`?
- **It's better if when using `strip()` and `title()` on the same line on or after the `input()` function?* 
- Is there are any limitation of decimal points on float?
> Floats can't represent the number infinitely precisely, in facts, because of the computers only have so much memory. They only have a finite amount of memory or hardware inside of the computer.

--> 
--> You can create a python file in terminal by `code pythonCode.py` and it will create a `pythonCode.py` in your current folder.
--> You can nest functions with parentheses, and it's working like in mathematics. It will look and working from the inside first then working their ways out to the outermost. 
--> We can format number like putting commas or periods in a long number like `1,000,000` or `1.000.000`. To do so we need to go back and using string and inside python it can be used like this:
```python
	print(f"{z:,}"); 
``` 
## New Major Keywords
chime(verb):
cryptic(n):
excerpt(n):

## ⏱️ Stopwatch Images

![Day 2 - Lecture 01-Cont. Stopwatch Image](../../assets/stopwatch/Python_day2-week0-stopwatch.png)

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