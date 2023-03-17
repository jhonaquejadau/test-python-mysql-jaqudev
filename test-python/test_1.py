""" 
  1) consulte la información del archivo data.py
  cree un objeto que contenga las empresas y dentro 
  las sucursales que corresponden para cada empresa
"""
from data import get_companies, get_branches

companies = get_companies()
branches = get_branches()
def get_company_branches(id):
  return list(filter(lambda item: item["id"] == id, branches))

def get_new_companies():
  new_companies = list(map(lambda company: {**company, "branches": [get_company_branches(id) for id in company["branches"]][0] }, companies))
  return new_companies

print(get_new_companies())