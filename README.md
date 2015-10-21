# Peryton

###A Python to Swift Transpiler

Peryton, named after the mythological [deer](https://en.wikipedia.org/wiki/Peryton) that has the wings of a bird, is a Python to Swift Transpiler. 
It can accept native Python code, parse it, and translate that code to the equivalent code in swift. The major advantages of using Peryton are:

* You can write IOS/OS X applications use Python.
* You can make use of the Swift language without having to learn it's syntax, rules etc.
* You can convert your favorite Python modules/documents to Swift code to use in your IOS/ OS X applications.

####Compatability

Transpiling Python to Swift does raise a number of issues in the process. The first and foremost one, is the lack of type safe practices in Python, where you do not specify the type being passed into a function and the type being returned. Fortunately, Peryton handles this issue by type-testing the input of functions, as well as object attributes. 

In Swift, you can declare variables and constants:

`var t = 0`

`let thing = "Hello"`

Where changing the let constant causes an error. Python does not have constants. However, one can theoretically infer from the structure of a function or program if a variable has the need for being protected. Peryton will be developed to do this through a process called Flow_Analysis, that determines the connections between functions, classes, objects and other parts of a program.

* See the peryton package for the transpiler code.
