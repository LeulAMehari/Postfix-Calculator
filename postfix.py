#Author:        Leul Adane
#Purpose:       It reads the postfix form from of an arithmetic expression, evalutes it and outputs the result.
#Date:          Februray 15, 2023
import sys

class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_after(self, current_node):
        # Special case, remove head
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node  
            if succeeding_node == None: # Remove last item
                self.tail = None
        elif current_node.next != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None: # Remove tail
                self.tail = current_node

class Stack:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)
        
        # Insert the node as the list head (top of stack)
        self.list.prepend(new_node)
    
    def pop(self):
        # Copy data from list's head node (stack's top node)
        popped_item = self.list.head.data
        
        # Remove list head
        self.list.remove_after(None)
        return popped_item
    
def do_operation(num, num2, operant):
    if operant == "+":
        result = num + num2 
        return result
    elif operant == "-":
        result = num - num2 
        return result
    elif operant == "*":
        result = num * num2
        return result
    elif operant == "^":
        result = num ** num2
        return result
    elif operant == "/":
        if num2 == 0:
            sys.exit("The operation couldn't be performed because the divisor is 0, which will result in a NaN")        
        result = num / num2
        return result
    elif operant == "%":
        result = num % num2
        return result

sentinel = "s"
opp=["+","-","*","/","^", "%"]
num_stack = Stack()
result = 0
expression = input("Enter the expression:    ")
expression = expression.replace(" ", "")  #Removes all the white space
i=0

while i <  len(expression):
    if expression[i].isnumeric():
        num_stack.push(expression[i])
    elif expression[i] in opp:
        first_num = num_stack.pop()
        second_num = num_stack.pop()
        result = do_operation(float(second_num), float(first_num), expression[i])
        num_stack.push(result)
    else:
        sys.exit(f"The character {expression[i]} is not a number nor a valid operator")
        
    i+=1
    if i == len(expression):
        print(f"The result of the expression is {result}")
        sentinel = input("Enter Q to quit or any other character to continue ").upper()
        if sentinel == "Q":
            sys.exit("You have exited the program")
        expression = input("Enter the expression:    ")
        expression = expression.replace(" ", "")
        i=0

    






















