"""
  5) ordenar los terceros que se tienen en el archivo data.py por nombre y 
  agregar dentro de cada tercero una propiedad que muestre la compañia a la que pertenece
"""

from data import get_thirds, get_companies

thirds = get_thirds()
companies = get_companies()

def get_company(id):
    return list(filter(lambda item: item["id"] == id, companies))

def order_thirds_name(arr):
    return list(map(lambda item: {**item, "company": get_company(item["companyid"])}, arr))

print(order_thirds_name(thirds))