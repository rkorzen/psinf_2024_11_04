from dataclasses import dataclass
import requests


@dataclass
class Rate:
    currency: str
    code: str
    mid: float


url = "https://api.nbp.pl/api/exchangerates/tables/A/"


def get_rates() -> list[Rate]:
    response = requests.get(url)

    raw_rates = response.json()[0]["rates"]

    rates = [Rate(**d) for d in raw_rates]  # {"a":1, "b":2} **=> a=1, b=2
    return rates


def get_rate(code: str) -> Rate:
    rates = get_rates()
    for rate in rates:
        if rate.code == code:
            return rate


def get_codes():
    rates = get_rates()
    return [r.code for r in rates]


def exchange(code: str, amount: float) -> float:
    rate = get_rate(code)
    return round(rate.mid * amount, 2)

# print(exchange("USD", 100))
#
# d = {"currency":"bat (Tajlandia)","code":"THB","mid":0.1178}
# # **d:    currency="bat (Tajlandia)", code="THB", mid=0.1178
#
# d2 = dict(currency="bat (Tajlandia)",code="THB", mid=0.1178)
# print(d)
# print(d2)
#
#
# print(Rate(**d))
# print(Rate(**d2))
