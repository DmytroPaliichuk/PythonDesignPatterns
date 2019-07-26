"""
Your module description
"""

class FirstObject:
    
    def __init__(self, name):
        self._name = name
        
    def raise_func(self):
        return "This is FirstObject"

        
class SecondObject:
    
    def __init__(self, name):
        self._name = name
        
    def raise_func(self):
        return "This is SecondObject"
        

def factory_method(obj="first"):
    """This is factory method"""
    
    objs = dict(first=FirstObject("name_1"), 
                second=SecondObject("name_2"))
    
    return objs[obj]


fm = factory_method('first')
print("func: ", fm.raise_func())

fm = factory_method('second')
print("func: ", fm.raise_func())
