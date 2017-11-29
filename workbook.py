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