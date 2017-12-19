'''
Notebook to try out various code snippets.
'''

class Foo(object):
    def __init__(self):
        pass
    def show(self):
        return 'Whoop!'

class Bar(object):
    def __init__(self, obj=Foo()):
        self.obj = obj
    
    def show(self):
        print(self.obj.show())

b = Bar()

b.show()

# How to Dynamically Load Modules or Classes

# 1. Using the __import__ Magic Method


# module = __import__(module_name)
# my_class = getattr(module, class_name)
# instance = my_class() 
# 
# Both module_name and class_name have to be strings in the above code.
# 
# 2. using sys.modules
# import sys
# 
# my_class = getattr(sys.modules[__name__], class_name)
# instance = my_class() 