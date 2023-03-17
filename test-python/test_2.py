"""
  2) teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""

from test_1 import get_new_companies

def get_all_branches(arr):
    return list(map(lambda item: {"id": item["id"], "name": item["name"], "branches": item["branches"]}, arr))

print(get_all_branches(get_new_companies()))