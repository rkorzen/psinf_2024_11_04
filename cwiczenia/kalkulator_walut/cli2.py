import argparse

from kalkulator import exchange, get_codes


def main():

    parser = argparse.ArgumentParser(description='Kalkulator walut')
    parser.add_argument('code', choices=get_codes(), help="Kod waluty")
    parser.add_argument("amount", type=float, help="ile chcesz kupic")

    args = parser.parse_args()

    code = args.code
    amount = args.amount

    print(exchange(code, float(amount)))

if __name__ == '__main__':
    main()