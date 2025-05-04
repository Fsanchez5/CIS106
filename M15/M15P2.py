class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = self._validate_price(sticker_price)

    def _validate_price(self, price):
        if price < 0:
            raise ValueError("Price must be non-negative.")
        return round(price, 2)

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_sticker_price(self):
        return round(self.sticker_price, 2)

    def get_discount_price(self):
        return round(self.sticker_price * 0.9, 2)

    def __str__(self):
        return (
            f"{self.make} {self.model} - "
            f"Sticker Price: ${self.get_sticker_price():.2f}, "
            f"Discount Price: ${self.get_discount_price():.2f}"
        )


class SportCar(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = False
        self.sport_engine = False
        self.sport_interior = False

    def set_sport_wheels(self, option):
        self.sport_wheels = option.upper() == "Y"

    def set_sport_engine(self, option):
        self.sport_engine = option.upper() == "Y"

    def set_sport_interior(self, option):
        self.sport_interior = option.upper() == "Y"

    def updated_price(self):
        base_price = self.get_discount_price()
        if self.sport_wheels:
            base_price += 1000.00
        if self.sport_engine:
            base_price += 3000.00
        if self.sport_interior:
            base_price += 2000.00
        return round(base_price, 2)

    def __str__(self):
        options = []
        if self.sport_wheels:
            options.append("SportWheels")
        if self.sport_engine:
            options.append("SportEngine")
        if self.sport_interior:
            options.append("SportInterior")
        options_str = ", ".join(options) if options else "No Options"
        return (
            f"{self.make} {self.model} - "
            f"Options: {options_str} - "
            f"Final Price: ${self.updated_price():.2f}"
        )


car1 = Car("Nissan", "Altima", 25000)
car2 = Car("Ford", "Fusion", 28000)

print("=== Regular Cars ===")
print(car1)
print(car2)

sport1 = SportCar("Lamborghini", "Huracan", 35000)
sport1.set_sport_wheels("Y")
sport1.set_sport_engine("Y")
sport1.set_sport_interior("Y")

sport2 = SportCar("Porsche", "Taycan", 36000)
sport2.set_sport_wheels("N")
sport2.set_sport_engine("Y")
sport2.set_sport_interior("N")

print("\n=== Sport Cars ===")
print(sport1)
print(sport2)