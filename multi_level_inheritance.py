class Parent():
    
    def __init__(self):
        print("This is parents property")

class child(Parent):
    
    def __init__(self):
        super().__init__()
        print("This is childs property")

    
class GrandChild(child):
    
    def __init__(self):
        super().__init__()
        print("This is grandchilds property.")

Property = GrandChild()
