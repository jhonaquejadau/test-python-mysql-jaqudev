"""
  4) Mostrar de los terceros que se tienen en el archivo data.py 
  los cuales no poseen ni email o no tengan cellPhone.
"""

from data import get_thirds

print(get_thirds())

thirds = get_thirds()
def filter_thirds(arr):
  return list(filter(lambda item: item["email"] == "" or item["cellPhone"] == None, arr))


print(filter_thirds(thirds))
print(len(thirds))
print(len(filter_thirds(thirds)))