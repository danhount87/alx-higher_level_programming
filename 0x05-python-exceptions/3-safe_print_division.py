#!/usr/bin/python3
def safe_print_division(a, b):
    """function that divides 2 integers and prints the result."""
    try:
        rslt = a / b
    except (TypeError, ZeroDivisionError):
        rslt = None
    finally:
        print("Inside result: {}".format(rslt))
    return (rslt)
