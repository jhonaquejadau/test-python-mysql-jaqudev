"""
  3) ordenar los terceros que se tienen en el archivo data.py 
  por nombre, para obtener el nombre correcto se debe tener en 
  cuenta la siguiente validación:
  
  si el tercero tiene un (tradename != '') entonces se muestra este valor, 
  en caso contrario se debe obtener concatenando los siguientes 
  campos: (firstname, lastname, maidenname) en el orden dado
"""
from data import get_thirds

thirds = get_thirds()
def order_thirds(arr):
    new_thirds = list(map(lambda item: {**item} if item["tradename"] != '' else {**item, "tradename": " ".join([item["firstname"], item["lastname"], item["maidenname"]])}, arr))
    return new_thirds

order_thirds(thirds)
print(order_thirds(thirds))