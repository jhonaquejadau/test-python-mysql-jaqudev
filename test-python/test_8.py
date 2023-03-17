"""
  8) realice una consulta al archivo data.py, muestre los items donde su codigo sea un número PAR,
  ordenelos por el precio de manera descendente y dentro de cada item 
  agregue el color correspondiente, si lo tiene.
"""

from data import get_items, get_colors

items = get_items()
colors = get_colors()

def get_color():
    return list(filter(lambda item: item, colors))

new_items = list(map(lambda item: {**item, "color": {}}, items))