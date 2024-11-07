from dataclasses import dataclass


class Rate:

    def __init__(self, currency, code, mid):
        self.currency = currency
        self.code = code
        self.mid = mid



@dataclass
class Rate:
    currency: str
    code: str
    mid: float


r = Rate("A", "B", 1.1)
print(r)