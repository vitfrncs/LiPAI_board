"""Aula 03 - Entendendo o uso de *args e **kwargs em funções e métodos"""

# ---------------------------------------------------------

def world_cup_titles(country, *args):
    print('Country:', country)
    for title in args:
        print('Year:', title)

# Chamada com 5 itens no *args
world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')

# Chamada com 1 item no *args
world_cup_titles('Espanha', '2010')


# ---------------------------------------------------------
# **kwargs

def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

# calculo sem desconto ou imposto
final_price = calculate_price(100.0)
print(final_price)

# calculo com desconto
final_price = calculate_price(100.0, discount=5.0)
print(final_price)

# calculo com imposto
final_price = calculate_price(100.0, tax_percentage=7)
print(final_price)

# calculo com imposto e desconto
final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
print(final_price)
