import os

def function_b():
    return "b"

if __name__ == "__main__":
    import module_path_manager
    module_path_manager.set(current_file=__file__, target_file='main.py', depth=3, syspath=True, chdir=True)
    
    import main
    from module1 import a
    from module2 import b
    from module3.test import c
    print(main.function_main())
    print(a.function_a())
    print(b.function_b())
    print(c.function_c())

    print(__file__)
    print(os.getcwd())