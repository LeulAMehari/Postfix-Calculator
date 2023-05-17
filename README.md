# Postfix-Calculator
This program reads the postfix form of an arithmetic expression, evaluates it, and outputs the result.
For instance if the user input was 34+52/*
The numbers 3 and 4 are pushed onto the stack. The addition operator "+" is encountered, so the top two values, 4 and 3, are popped from the stack, and 
their sum 7, is pushed back onto the stack. Next, the numbers 5 and 2 are pushed onto the stack. The division operator "/" is encountered,
so the top two values, 2 and 5, are popped from the stack, and their quotient, 2.5, is pushed back onto the stack. 
Finally, the multiplication operator "" is encountered, so the top two values, 2.5 and 7, are popped from the stack,
and their product, 17.5, is pushed back onto the stack. The final result of the expression "34+52/*" is determined to be 17.5.
