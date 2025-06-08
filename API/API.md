# API

## Como criar um arquivo com o HTML de um site via API

```python
import requests  # Biblioteca para consultar API

url = "https://www.google.com.br"  # URL da API
response = requests.get(url)  # Utiliza o método get na API (Extrai informações)

print(response)  # Printa a resposta do método
print(response.text)  # Printa a informação extraída

# Abre um arquivo html na pasta files e insere as informações extraídas via API
with open("files/page.html", "w") as page:
    page.write(response.text)
```

## Aplicar o método POST (Envio de dados)

```python
import requests

# Configuração da requisição
url = "https://httpbin.org/post"

# Dados a serem enviados no corpo da requisição (formato JSON)
data = {
    "pessoa": {
        "nome": "Rodrigo",
        "profissao": "professor"
    }
}

# Parâmetros de consulta (query parameters)
params = {
    "dataIni": "2025-01-01",
    "dataFim": "2025-12-31"
}

# Executa a requisição POST
response = requests.post(
    url,
    json=data,      # Envia dados no corpo como JSON
    params=params   # Adiciona parâmetros na URL
)

print(response.request.url)  # Exibe a URL completa com parâmetros
print(response.text)        # Exibe o corpo da resposta do servidor
```

## Parâmetros de Consulta (Query Parameters)

**Definição:**
Pares **chave-valor** adicionados diretamente na URL de uma requisição HTTP após o caractere `?`.

**Estrutura:**
- **Chave**: Identificador único (ex: `pagina`, `limite`)
- **Valor**: Dado associado à chave (ex: `1`, `10`)

**Formato na URL:**
https://api.exemplo.com/recurso?chave1=valor1&chave2=valor2

**Funções principais:**
- 🔍 Filtrar resultados
- 📑 Paginar dados (`?page=2&per_page=10`)
- ⚙️ Especificar configurações de resposta
- ➕ Passar parâmetros opcionais para a API

🔧 Regras de Formatação de Query Parameters

**Regras detalhadas:**

1. **Primeiro parâmetro**  
   - Prefixado com `?` no início da query string  

2. **Parâmetros subsequentes**  
   - Separados por `&`  

3. **Codificação automática**  
   - Valores especiais são *automaticamente convertidos*
   - O requests cuida *automaticamente da codificação correta*

### Como construir um dicionário tendo como base uma requisição GET

```python
import requests
import pandas as pd

def frequencia_nome(name):
    #Obtem um dicionário de frequencia de um nome pro década no formato {década: quantidade}

    # o f é utilizado para atribuir a variável name ao fim da url
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
    
    # Aplica a requisição GET e converte do JSON para um dionário ou lista de dicionários ou cria uma lista vazia
    dados_nome = obter_request(url) or []


    dados_dict  = {
        # O valor associado à chave "periodo" dentro do dicionário 'dados' será a chave no novo 'dados_dict' e o valor associaod à chave "frequencia" dentro de 'dados' será o valor no novo dicionário
        dados["periodo"]: dados["frequencia"] 

                   # Percorre todos os elementos de dados_nome[0] e atribui à dados

                   for dados in dados_nome[0].get("res", [])} # Obtem o valor associadao à chave "res", se existir, retorna o valor correspondente, se não, uma lista vazia
    # DataFrame cria estrutura de tabela tendo para dados. .from_dict() permite criar um dataframe diretamente de um dicionário. Recebe como parâmetro o dicionário e orient. Orient recebe "index", utilizado quando os rótulos das linhas servirem como rótulos (ID, datas), e "columns" quando deseja nomes específicos para colunas ou deseja selecionar/ordenar colunas de um dicionpario (orient="index")
    df = pd.DataFrame.from_dict(dados_dict, orient="index")
    return df
```

### Como construir uma interface web com streamlit

```python
import streamlit as st

def main():
    # Adiciona um titulo ao web page do streamlist
    st.title("Web App API")
    # Adiciona um header ao web page do streamlist
    st.header("Dados da API IBGE")
    # Atribui a uma variável o valor inserido no input do streamlit
    in_name = st.text_input("Digite um nome:")
    if not in_name:
        st.stop()
    # Atribui as frequenicas do nome inserido no input à df
    df = frequencia_nome(in_name)
    # Cria duas colunas no streamlit (Ocuparão 30 e 70% da alrgura disponível)
    col1, col2 = st.columns([0.3, 0.7])
    
    # O with direciona todo o contéudo do bloco para ser renderizado na col1
    with col1:
        # Exibe textos/números
        st.write("Frequencia por década")
        # Tabela de dados
        st.dataframe(df)
    with col2:
        st.write("Série temporal")
        # Grafico de linha
        st.line_chart(df)
```

### Como exceutar um código com streamlit
Execute o comando no terminal
```
streamlit run.\nome_do_arquivo
```

### Uso do __main__

**`__name__ armazena o nome do script atual`**

Quando outro script importa o código como um módulo, o Python **`define __name__ como o nome do arquivo`**

```python
# O if verifica se o código não está sendo importado por outro
# Execute o código da main somente se este arquivo for o programa principal que esta sendo rodado
if __name__ == "__main__":
    main()
```