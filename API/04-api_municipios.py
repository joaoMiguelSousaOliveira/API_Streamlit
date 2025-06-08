import requests
from pprint import pprint


url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados"
params = {
    "view":"nivelado"
}
#puxa os dados da api (url) 
response = requests.get(url, params=params)
try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    resultado = None
else:
    resultado = response.json()
    # Formata o json
    pprint(resultado)