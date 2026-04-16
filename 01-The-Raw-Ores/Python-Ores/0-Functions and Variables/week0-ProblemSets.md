
# 🐍 Python Concept: [Week 0 - Problem Set 0]

*This note is written with the help of [StackEdit](stackedit.io) and [EmojiCopy](emojicopy.com)*

**Date:** April 16th, 2026 - [7:25 - 8:15]

**Tags:**  `#python`, `#primitive-ai`, `#self-study`, `#cs50_2026`, `#harvard_university`  `#edX`  `#VSCode`

**Time spent**: *`1 hours, 15 minutes and 48 seconds`*

**Course infos**: [Course | CS50's Introduction to Programming with Python | edX](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/home?audit_mode=)

**Track:**
[CS50 Harvard - Python Problem Sets 0](https://cs50.harvard.edu/python/psets/0/)

## 🎯 Objective

## 🪧 Problem Sets 0
>Before starting to solve the problem make sure to log into [cs50.dev](https://cs50.dev/), which is a cloud-based version of Visual Studio Code (VS Code) that provides you with your very own “codespace” with everything that you need for the course pre-installed. No need to download and install VS Code or Python on your own Mac or PC! If not already familiar, be sure to watch the [Visual Studio Code for CS50 Short](https://cs50.harvard.edu/python/shorts/visual_studio_code_for_cs50/) for a full overview.

### [Indoor Voice](https://cs50.harvard.edu/python/psets/0/indoor/#indoor-voice)

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called  `indoor.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a  `str`  of your own as an argument to  `input`.

### [Playback Speed](https://cs50.harvard.edu/python/psets/0/playback/#playback-speed)

Some people have a habit of  lecturing  speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called  `playback.py`, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with  `...`  (i.e., three periods).

### [Making Faces](https://cs50.harvard.edu/python/psets/0/faces/#making-faces)

Before there were emoji, there were  [emoticons](https://en.wikipedia.org/wiki/List_of_emoticons), whereby text like  `:)`  was a happy face and text like  `:(`  was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called  `faces.py`, implement a function called  `convert`  that accepts a  `str`  as input and returns that same input with any  `:)`  converted to  ![🙂](https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f642.png)  (otherwise known as a  [slightly smiling face](https://emojipedia.org/slightly-smiling-face/)) and any  `:(`  converted to  ![🙁](https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f641.png)  (otherwise known as a  [slightly frowning face](https://emojipedia.org/slightly-frowning-face/)). All other text should be returned unchanged.

Then, in that same file, implement a function called  `main`  that prompts the user for input, calls  `convert`  on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a  `str`  of your own as an argument to  `input`. Be sure to call  `main`  at the bottom of your file.

### [Einstein](https://cs50.harvard.edu/python/psets/0/einstein/#einstein)

Even if you haven’t studied physics (recently or ever!), you might have heard that  𝐸  =𝑚⁢𝑐2, wherein  𝐸  represents energy (measured in Joules),  𝑚  represents mass (measured in kilograms), and  𝑐  represents the speed of light (measured approximately as 300000000 meters per second), per  [Albert Einstein](https://en.wikipedia.org/wiki/Albert_Einstein)  et al. Essentially, the formula means that mass and energy are equivalent.

In a file called  `einstein.py`, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

### [Tip Calculator](https://cs50.harvard.edu/python/psets/0/tip/#tip-calculator)
>And now for my Wizard tip calculator.
>
>— Morty Seinfeld

In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!
```python
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()

```
Well, we’ve written  _most_  of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

-   `dollars_to_float`, which should accept a  `str`  as input (formatted as  `$##.##`, wherein each  `#`  is a decimal digit), remove the leading  `$`, and return the amount as a  `float`. For instance, given  `$50.00`  as input, it should return  `50.0`.
-   `percent_to_float`, which should accept a  `str`  as input (formatted as  `##%`, wherein each  `#`  is a decimal digit), remove the trailing  `%`, and return the percentage as a  `float`. For instance, given  `15%`  as input, it should return  `0.15`.

Assume that the user will input values in the expected formats.


## Core Notes - Optional
> Written with [StackEdit](https://stackedit.io/).