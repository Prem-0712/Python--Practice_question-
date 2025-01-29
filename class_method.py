class Bike:
    price_hiked = 0

    @classmethod
    def increased_price (self, price):
        self.price_hiked = price * 0.20 + price


splendor = Bike()
fz5 = Bike()

splendor.increased_price(100000)
fz5.increased_price(65000)

print(f'Hiked price of Apcahe: {splendor.price_hiked}')
print(f"Hiked price of FZ5: {fz5.price_hiked}")