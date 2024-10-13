#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize an empty list to store Fibonacci numbers
    fib_sequence = []
    
    # Edge case: length 0 should print an empty list
    if length == 0:
        print(fib_sequence)
        return
    
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0] * length
    if length > 0:
        fib_sequence[0] = 0
    if length > 1:
        fib_sequence[1] = 1
    
    # Generate Fibonacci numbers and store them in the list
    for i in range(2, length):
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]
    
    # Print the final Fibonacci sequence list
    print(fib_sequence)
