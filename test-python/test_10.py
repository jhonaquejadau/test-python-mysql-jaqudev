"""
  10) realice una consulta al archivo data.py, muestre todos los terceros, reduzca la 
  información y solo muestre el nombre, la ciudad y la identificacion, 
  ordenelos por su identificación
"""

from data import get_thirds

thirds = get_thirds()

new_thirds = list(map(lambda item: {"firstname": item["firstname"], "cityName": item["cityName"], "identificationNumber": item["identificationNumber"]}, thirds))
new_thirds = sorted(new_thirds, key = lambda item: item["identificationNumber"])
print(new_thirds)