# countries = {'Argentina': 'Buenos Aires',
#              'Spain': 'Madrid',
#              'Colombia': 'Bogota',
#              'Rep. Dominican': 'Santo Domingo'}
# print(countries)
#
# def dic_countries(countries):
#     for capital in countries:
#         print(capital, countries[capital])
# dic_countries(countries)

# Examples
def product_load():
    products = {}
    for f in range(3):
        name = input('Write product name ')
        price = int(input('Write price '))
        products[name] = price
    return products


def printing(products):
    print('Products list ')
    for name in products:
        print(name, products[name])


articles = product_load()
printing(articles)
