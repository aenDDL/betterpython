from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class VehicleInfo:
    brand: str
    electric: bool
    price: int

    def compute_tax(self, tax_exception_amount: int = 0) -> float:
        if tax_exception_amount < 0:
            raise ValueError(f"tax_exception_amount should be positive number, received {tax_exception_amount} instead.")
        final_price = max(self.price - tax_exception_amount, 0)
        return final_price * 0.02 if self.electric else final_price * 0.05
    
    def can_lease(self, year_income: int) -> bool:
        if year_income < 0:
            raise ValueError(f"tax_exception_amount should be positive number, received {year_income} instead.")
        return True if self.price <= year_income * 0.7 else False

