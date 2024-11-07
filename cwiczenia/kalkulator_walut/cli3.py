import click

from kalkulator import exchange, get_codes


@click.command()
@click.argument("code", type=click.Choice(get_codes()))
@click.argument("amount", type=float)
def main(code, amount):
    print(exchange(code, float(amount)))

if __name__ == '__main__':
    main()