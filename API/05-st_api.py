import requests
import pandas as pd
import streamlit as st

def obter_request(url, params=None):
    # Faz uma requisição GET  e retorna a resposta em JSON
    try:
        # Aplica uma requisição GET de uma URL, recebendo como parâmetro um dicionário de parâmetros
        response = requests.get(url, params=params)
        # Verifica se houve algum erro na requisição 
        response.raise_for_status()
        # Analisa o corpo da resposta da requisição como JSON, se for um JSON válido, convrete-o geralmente para um dicionpário ou uma lista de dicionários, se não, levantará uma exceção json.JSONDecodeError
        return response.json()
    # Aplica uma exceção em caso de erro
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")
        return None
    

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

# __name__ é uma variável que armazena o nome do script atual
# Quando outro script importa o código como um módulo, o Python define __name__ como o nome do arquivo 
# O if verifica se o código não está sendo importado por outro
    # Execute o código da main somente se este arquivo for o programa principal que esta sendo rodado
if __name__ == "__main__":
    main()