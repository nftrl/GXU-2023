# Programmeringshold GXU 2023

## [Fra elever](https://github.com/nftrl/GXU-2023/tree/main/fra%20elever)
### Tactical Gardening
Styr med piletasterne, skyd med musen. Lavet af Martin.

# Projects

## Simple calculator
A simple calculator for simple expressions. First it takes a binary operator like +, -, * or / and then the two operands (x and y) to calculate simple expressions like x + y and x / y.

Follow the steps to create the program and afterwards implement the extensions. Feel free to change or add anything you like :)

The program (without extensions) might look something like this:

	This is a simple calculator.
	First you input the operator, then the operands one at a time.
	
	Input operator [+-*/]
	> +
	Input x in (x + y)
	> 19
	Input y in (19 + y)
	> 3.4
	Result:
	19 + 3.4 = 22.4

### Steps
These are steps you can follow to create the program. Also they work as a structure for the program.

1. get operator [+-*/] from user
2. get operands (x and y) from user
3. calculate result
4. print result

### Extensions
These are ideas for extending the program. If you have any ideas of your own feel free to go ahead with those.

- Handle errors, for example invalid input and division by zero.
- Implement a loop to allow for multiple calculations after the first one is done.
- Save the result from the last calculation in a variable. Now make this previous result accessible with a special symbol in the operand input stage. This way you can chain together calculations.
- Implement support for more operators, for example exponentation (^) and square root (√).
- Implement support for functions, for example sin() or log().
