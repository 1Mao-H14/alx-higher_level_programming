#!/usr/bin/python3

def print_last_digit(number):

    absolute_number = abs(number)
    last_digit = absolute_number % 10
    print(last_digit)
    return(last_digit)
