#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    if length >= 1:
        fib.append(0)
    if length >= 2:
        fib.append(1)
    if length >= 3:
        for i in range(length-2):
            fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
            
    print(fib)
