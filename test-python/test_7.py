"""
  7) realice una consulta al archivo data.py, muestre los items que tienen colores 
  y ordenelos por precio de manera ascendente
"""

from data import get_items

items = get_items()

new_items = [item for item in items if item["color"] != None]
new_items = sorted(new_items, key = lambda item: item["price"])
print(new_items)