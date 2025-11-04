class Kendaraan:
    def __init__(self, merk, kecepatan):
        self.merk = merk
        self.kecepatan = kecepatan

class Mobil(Kendaraan):
    def info(self):
        print(f"Mobil {self.merk} melaju {self.kecepatan} km/jam.")

class Motor(Kendaraan):
    def info(self):
        print(f"Motor {self.merk} melaju {self.kecepatan} km/jam.")

mobil1 = Mobil("Toyota", 120)
motor1 = Motor("Honda", 90)

mobil1.info()
motor1.info()