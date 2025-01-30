class Parent ():
    
    def parent_property (self):
        print("This is parents property")

    
class child_brother (Parent):

    def brothers_property (self):
        print("This is child brothers property.")

class child_siser (Parent):

    def sisters_property (self):
        print("Ths is child sisters property")

Prem = child_brother()
Prem.brothers_property()
Prem.parent_property()