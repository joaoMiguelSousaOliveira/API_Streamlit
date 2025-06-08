import requests

#url = "https://httpbin.org/get"

url = "https://httpbin.org/post"

data = {
    "pessoa":{
        "nome":"Rodrigo",
        "profissao":"professor"
    }
}

params = {
    "dataIni": "2025-01-01",
    "dataFim": "2025-12-31"
}

response = requests.post(url, json=data, params=params)

print(response.request,url)
print(response.text)

#https://httpbin.org/post?#dataIni=2025-01-01# Primeiro parametro utiliza "?" #&dataFim=2025-12-31# Segundo parâmetro em diante utiliza "&"