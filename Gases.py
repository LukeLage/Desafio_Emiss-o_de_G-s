# Processamento de bibliotecas usadas no código, uso de cada no comentário ao lado da importação
import pandas as pd #Biblioteca para processamento de dados
import plotly.express as px #Biblioteca para criação de gráficos
import streamlit as st #Biblioteca para criação de servidor web


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

# Função com a explicação sobre o que é gás carbono
def gas_carbono():
    st.title ('O que é o Gás Carbono?')
    st.write ('Também é conhecido como dióxido de carbono, sua formula química é a a CO₂, é encontrado em temperatura ambiente, transparente, mas absorve radiação infravermelha, dessa forma, agindo como um gás do efeito estuda, uma das consequências disso é que o gás carbono é um dos principais causadores de mudanças climáticas atualmente.')
    st.write ('A principal causa da emissão desse gás é a queima de combustíveis fósseis, mas também pode ser liberado por respiração e decomposição de seres vivos, erupção vulcânica, queimadas e desmatamentos, processamentos industriais, além de também refinaria de petróleo, produção de aço e cimento.')
    st.title ('O que o Gás Carbono Causa?')
    st.write ('Principalmente, o aumento de gás carbono na atmosfera altera condições climáticas mundiais, dentro disso, o aquecimento do oceano que é responsável pela regulação do clima, também causa chuva ácida.')
    st.write ('Mas uma das principais consequências é o desequilíbrio do efeito estufa, assim, consequentemente elevando a temperatura da terra causando um efeito dominó com catástrofes climáticas, o que, por sua vez, já causou a extinção de diversas espécies da fauna e da')

# Funções usadas para montar os gráficos para melhor organização de código, para descrições específicas de cada função, ver comentário ao lado da def

# Função para criação dos gráficos usados para visualização dos países que mais produzem gás carbono
def paises_emissao_porcentagem (): #Porcentagem dos países que mais emitem
    fig = px.pie(paises_df, values = 'Porcentagem', names = 'Países', title = 'Porcentagem Top 10 Países que mais Emitem Gás Carbono') #Relação país/porcentagem

def paises_emissao_toneladas(): #Toneladas de emissão
    fig = px.pie(paises_df, values= 'Toneladas', names = 'Países', title = 'Toneladas Emitidas por Ano pelos Top 10') #Relação país/toneladas


# Função para carregar o gráfico de barra representando toneladas de gás carbono emitido
def emissao_gas (): 
    fig = px.bar(emissao_df, x = 'Anos', y = 'Toneladas em Bilhões', title = 'Emissão de Gás Carbono por Anos em Toneladas')

# Função para carregar o gráfico de pizza representando os setores que mais emitem gás carbono
def setores_emissao (): 
    fig = px.pie(setores_df, values = 'Porcentagem', names = 'Setores', title='Emissão de Toneladas de Gás Carbono (por bilhão) por Setor' , color_discrete_sequence = px.colors.qualitative.bold)

# Botões para apresentação dos gráficos que aparecerão na tela, para ver qual botão é referente à qual gráfico, ver comentário ao lado de cada função
