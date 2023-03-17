"""
  6) ordernar las compañias por nombre y dentro de cada compañia, crear un objecto 
  llamado thirds el cual va a tener todos los terceros que pertenezcan a esa compañia
"""

from data import get_thirds, get_companies

companies = get_companies()
thirds = get_thirds()

def get_company_thirds(id):
    return list(filter(lambda item: item["companyid"] == id, thirds))

def get_new_companies(arr):
    return list(map(lambda item: {**item, "thirds": get_company_thirds(item["id"])}, arr))

print(get_new_companies(companies))