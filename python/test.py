from typing_extensions import IntVar


from typing_extensions import IntVar
class TestClass(object):
    _val:IntVar
    def __init__(self,val=0)->None:
        self._val=val
    def print_val(self):
        return self._val
a=TestClass("a")
print(a.print_val())