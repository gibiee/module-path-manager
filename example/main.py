import os
from module1 import a
from module2 import b
from module3.test import c

def function_main():
    return "main"

if __name__ == "__main__":
    print(function_main())
    print(a.function_a())
    print(b.function_b())
    print(c.function_c())

    print(__file__)
    print(os.getcwd())