import string
import random
from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class VehicleInfo:
    brand: str
    price: int
    electic: bool

    def tax_to_pay(self) -> int:
        return self.price * 0.02 if self.electic else self.price * 0.05
    
    def __str__(self) -> str:
        return f"Brand: {self.brand}\nTax to pay: {self.tax_to_pay():,}"
    

def generate_uid() -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=12))
 
def generate_licence_plate(uid: str) -> str:
    first_letters = uid[:2]
    numbers = random.randint(1, 99)
    sec_letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    return f"{first_letters}-{numbers:02d}-{sec_letters}"


@dataclass
class Vehicle:
    info: VehicleInfo = field(repr=False)
    uid: str = field(default_factory=generate_uid)
    license_plate: str = field(init=False)

    def __post_init__(self) -> None:
        self.license_plate = generate_licence_plate(self.uid)

    def __str__(self) -> str:
        return f"{self.info}\nUnique ID: {self.uid}\nLicense_plate: {self.license_plate}"
    

@dataclass
class VehicleRegistry:
    vehicles: dict[str, VehicleInfo] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self._register_vehicle("BMW", 35_000, False)
        self._register_vehicle("TESLA", 140_000, True)

    def _register_vehicle(self, brand: str, price: int, electic: bool) -> None:
        self.vehicles[brand] = VehicleInfo(brand, price, electic)

    def create_vehicle(self, brand: str) -> Vehicle:
        if brand not in self.vehicles:
            raise ValueError("Car not register.")
        return Vehicle(info=self.vehicles[brand])
    

def main() -> None:
    v = VehicleRegistry()
    rv = v.create_vehicle("TESLA")
    print(rv)
    

if __name__ == "__main__":
    main()