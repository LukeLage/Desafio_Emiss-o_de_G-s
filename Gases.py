# Processamento de bibliotecas usadas no código, uso de cada no comentário ao lado da importação
import pandas as pd #Biblioteca para processamento de dados
import plotly.express as px #Biblioteca para criação de gráficos
import streamlit as st #Biblioteca para criação de servidor web
from plotly.subplots import make_subplots #Módulo usado para fazer subplots com diversos gráficos
import plotly.graph_objects as go #Biblioteca usada para fazer subplots


# Configurações gerais da aplicação
st.set_page_config(
    page_title="Emissão de Gas Carbônico na Atmosfera",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Carregamento de estilização CSS vinda da pasta Gases.css
with open ('Gases.css', 'r') as fp: 
    st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)

# Criação da sidebar com informações sobre o criador da aplicação
with st.sidebar:
    st.title('Quem sou eu?')
    st.write('Programador: Luke Malaquias Lage')
    st.write('PDITA: 172')
    st.write('Especialidade: programador backend e frontend')
    #A partir desta linha, sidebar usada para armazenar os botões que serão usados para navegar pelos gráficos
    st.title('Gráficos')

# Página inicial da aplicação, apresentação do que se trata
st.write ('Essa aplicação revolve em torno da exposição da emissão de gás carbônico na atmosfera desde a era da revolução industrial e quais, nesse momento, são os maiores emissores')
st.write ('Use os botões na barra lateral para alterar a visualização de gráficos!')

# DataFrames feitos com Pandas das informações que serão usadas nos gráficos, para ver qual arquivo será qual gráfico, ver comentário a cima de cada função

# Dicionário usado para fazer o DataFrame dos países com maior taxa de emissão de gás carbono
paises = { 
    'Países': ['China', 'Estados Unidos', 'União Europeia', 'Índia', 'Rússia', 'Japão', 'Brasil', 'Indonésia', 'Iran', 'Coreia do Sul', 'Demais países'],
    'Porcentagem': [25.76, 12.8, 7.8, 6.74, 5.26, 2.73, 2.28, 1.88, 1.74, 1.51, 31.51],
    'Toneladas': [11886.76, 5907.3, 3598.1, 3109.3, 2427.2, 1259.4, 5150.3, 866, 800.8, 697, 14538.7]
} 
paises_df = pd.DataFrame(paises)

# Dicionário usado para fazer o DataFrame com a quantidade de gás carbono emitido em bilhões ao longo dos anos
emissao_ano = {
    'Anos': [1949, 1950, 1989, 2000, 2019, 2021],
    'Toneladas em Bilhões': [4, 6, 22, 25, 36.4, 37]
} 
emissao_df = pd.DataFrame(emissao_ano)

# Dicionário usado para fazer o DataFrame com os setores que mais emitem gás carbono atualmente
setores = {
    'Setores': ['Energia', 'Agropecuária', 'Terra', 'Resíduos'],
    'Porcentagem': [73, 12, 6.5, 3.2]
} 
setores_df = pd.DataFrame(setores)


# Funções usadas para montar os gráficos para melhor organização de código, para descrições específicas de cada função, ver comentário ao lado da def

# Função para criação dos gráficos usados para visualização dos países que mais produzem gás carbono
fig = make_subplots(rows=2, cols=1)  # Criação de subplots
fig.add_trace(go.bar)


# Função para carregar o gráfico de barra representando toneladas de gás carbono emitido
def emissao_gas (): 
    fig = px.bar(emissao_df, x = 'Anos', y = 'Toneladas em Bilhões', title = 'Emissão de Gás Carbono por Anos em Toneladas')

# Função para carregar o gráfico de pizza representando os setores que mais emitem gás carbono
def setores_emissao (): 
    fig = px.pie(setores_df, values = 'Porcentagem', names = 'Setores', title='Emissão de Gás Carbono (por bilhão) por Setor' , color_discrete_sequence = px.colors.qualitative.bold)

# Botões para apresentação dos gráficos que aparecerão na tela, para ver qual botão é referente à qual gráfico, ver comentário ao lado de cada função
