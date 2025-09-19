class car:
    def __init__(self,Brand,Color,Year):
        self.Brand = Brand
        self.Color = Color
        self.Year = Year

    def display(self):
        print(f"Brand: {self.Brand}, Color: {self.Color}, Year: {self.Year}")

a1 = car("Honda","Red",2025)
a1.display()

