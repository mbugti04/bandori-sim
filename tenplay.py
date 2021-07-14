import pydori

bapi = pydori.bandori_api()
cards = bapi.get_cards(id=[511])

card = cards[0]
print(card.name)