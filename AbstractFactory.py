"""
Your module description
"""

class ObjectA1:
    
    def raise_func(self):
        return "This is ObjectA1"

class ObjectA2:
    
    def raise_func(self):
        return "This is ObjectA2"


class ObjectB1:
    
    def raise_func(self):
        return "This is ObjectB1"

class ObjectB2:
    
    def raise_func(self):
        return "This is ObjectB2"

        

class AaFactory:
    """ Concret AA Factory"""
    def make_func_1(self):
        return ObjectA1()

    def make_func_2(self):
        return ObjectA2()        

    def get_info(self):
        return "AA Factory"


class BbFactory:
    """ Concret BB Factory"""
    def make_func_1(self):
        return ObjectB1()

    def make_func_2(self):
        return ObjectB2() 
    
    def get_info(self):
        return "BB Factory"

class NewClassAbstractFactory():
    """ This is Abstract Factory"""
    
    def __init__(self, factory):
        self._factory = factory

        self._class_1 = factory.make_func_1()
        self._class_2 = factory.make_func_2()

    def get_class_1(self):
        class_1 = self._factory.make_func_1()
        return class_1.raise_func()

    def get_class_2(self):
        class_2 = self._factory.make_func_2()
        return class_2.raise_func()
        
        
    def raise_func_1(self):
        return self._class_1.raise_func()
        
    def raise_func_2(self):    
        return self._class_2.raise_func()
        
    
    def who_am_i(self):
        return self._factory.get_info()
        
        
obj = AaFactory() if 1==2 else BbFactory()

inst = NewClassAbstractFactory(obj)

print(inst.raise_func_1())
print(inst.raise_func_2())

print(inst.who_am_i())
