import requests
from pprint import pprint

nome = input("Digite o nome para presquisar: \n")
url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
#aplica uma espécide de filtro por localidade
params = {
    "localidade":33 #RJ
}
#puxa os dados da api (url) aplicando os parâmetros
response = requests.get(url, params=params)
try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    resultado = None
else:
    resultado = response.json()
    # Formata o json
    pprint(resultado[0]["res"])