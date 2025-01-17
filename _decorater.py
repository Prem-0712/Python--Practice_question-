def shop(gift):
    def wrap():
        print("Red colour")
        gift()
    return wrap

@shop
def gift ():
    print("Watch")

# gift = shop(gift)

gift()