### Local and Global Variables ###

def namespace_demo():
    a = 1
    b = 2
    print ("\nLocal namespace: ")
    print (locals())
    print ("\nGlobal namespace: ")
    print (globals())

namespace_demo()
'''
Output:

Local namespace: 
{'a': 1, 'b': 2}

Global namespace: 
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/riyah/Desktop/Namespaces.py', 'namespace_demo': <function namespace_demo at 0x10ea9aac0>}
'''
