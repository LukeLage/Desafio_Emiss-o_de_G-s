# Processamento de bibliotecas usadas no código, uso de cada no comentário ao lado da importação
import pandas as pd #Biblioteca para processamento de dados
import plotly.express as px #Biblioteca para criação de gráficos
import streamlit as st #Biblioteca para criação de servidor web

# Configurações gerais da aplicação
st.set_page_config(
    page_title="Emissão de Gas Carbônico na Atmosfera",
    page_icon="💨",
    layout="wide",
    initial_sidebar_state="expanded",
)

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
def paises_emissao_porcentagem (): #Porcentagem dos países que mais emitem
    fig = px.pie(paises_df, values = 'Porcentagem', names = 'Países', title = 'Porcentagem Top 10 Países que mais Emitem Gás Carbono') #Relação país/porcentagem
    st.plotly_chart(fig)
def paises_emissao_toneladas(): #Toneladas de emissão
    fig = px.pie(paises_df, values= 'Toneladas', names = 'Países', title = 'Toneladas Emitidas por Ano pelos Top 10') #Relação país/toneladas
    st.plotly_chart(fig)

# Função para carregar o gráfico de barra representando toneladas de gás carbono emitido
def emissao_gas (): 
    fig = px.line(emissao_df, x = 'Anos', y = 'Toneladas em Bilhões', title = 'Emissão de Gás Carbono por Anos em Toneladas')
    st.plotly_chart(fig)

# Função para carregar o gráfico de pizza representando os setores que mais emitem gás carbono
def setores_emissao (): 
    fig = px.pie(setores_df, values = 'Porcentagem', names = 'Setores', title='Emissão de Toneladas de Gás Carbono (por bilhão) por Setor')
    st.plotly_chart(fig)

# Carregamento de estilização CSS vinda da pasta Gases.css
with open ('Gases.css', 'r') as fp: 
    st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)

# Área para criação de colunas para botões de navegações entre os gráficos
# Criação de colunas para separação de dois gráficos ao apertar o botão
paises1, paises2 = st.columns(2)

# Side bar com navegação entre gráficos e informações sobre o desenvolvedor da aplicação
with st.sidebar:
    # Botões para apresentação dos gráficos que aparecerão na tela, para ver qual botão é referente à qual gráfico, ver nome de cada botão
    st.title('Navegação pelos Gráficos')
    st.write('Para navegação entre gráficos, por favor selecione o desejado nos botões a seguir:')
    button1 = st.button('Emissão por Setor')
    button2 = st.button('Emissão por de Toneladas por Ano')
    button3 = st.button('Emissão por País')
    button4 = st.button('Emissão por País em Toneladas')
    button5 = st.button('Emissão por por País em Porcentagem')
    button6 = st.button('Fechar Gráficos')
    # Informações sobre o desenvolvedor da aplicação
    # Colocar o robozinho do desenvolve aqui como marcação
    st.title('Quem sou eu?')
    #st.write('Programador: Luke Malaquias Lage')
    st.write('PDITA: 172')
    st.write('Especialidade: programador backend e frontend')
    st.write("Contato: linkedin.com/in/luke-malaquias-lage-04022a232/")

# Funções para a exibição de gráficos durante as navegações

if button1:
    st.header('Emissão Anual de Gases por Setor Industrial')
    st.write('Esse gráfico remete à média emissão de gases por ano por diversos setores industriais.')
    st.write('No gráfico houve uma pequena simplificação em algumas partes para melhor observação visual, as repartições serão melhores explicadas.')
    st.write('Energia remete à elétrica, petróleo e carvão;')
    st.write('Terra remete ao uso, mudança de uso da terra e silvicultura;')
    st.write('Resíduos remete à praticamente todo resíduo humano, incluindo aterros e águas residuais.')
    setores_emissao()
if button2: 
    st.header('Emissão de Anual de Gases desde 1950')
    st.write('Esse gráfico remete à emissão de gás carbono por toneladas emitidos por ano desde os primeiros registros feitos com precisão, em 1950.')
    emissao_gas()
if button3: 
    st.header('Emissão de Gases por País, em Toneladas e em Porcentagem')
    st.write('Esses dois gráficos remetem à emissão de gás carbono por país, principalmente os dez principais que mais emitem esse gás anualmente. Juntos, esses países emitem em média 68,5% e 37702,16 de toneladas do gás carbono produzido por todo o mundo, anualmente.')
    st.title ('Emissão em Toneladas')
    paises_emissao_toneladas()
    st.title('Emissão em Porcentagem')
    paises_emissao_porcentagem()
if button4: 
    st.header('Emissão de Gases em Toneladas por País')
    st.write('Esse gráfico, em específico, remete à emissão de gases por toneladas emitida pelos top 10 países com maior taxa de produção de gases mundialmente')
    paises_emissao_toneladas()
if button5:
    st.header('Emissão de Gases em Porcentagem por País')
    st.write('Este gráfico exibe a emissão de gases por porcentagem com foco nos principais dez países com maior taxa de produção.')
    paises_emissao_porcentagem()
else:
    st.empty()

# Página inicial da aplicação, apresentação do que se trata
st.title ('Emissão de Gás Carbono na Atmosfera')

st.write ('Essa aplicação revolve em torno da exposição da emissão de gás carbônico na atmosfera desde a era da revolução industrial e quais, nesse momento, são os maiores emissores')
st.write ('O objetivo da criação desse dashboard foi para a existência de uma discussão sobre o aumento da nossa poluição, como humanidade e como, com o passar dos anos, mesmo com os acordos entre países para a diminuição da emissão de gases, eles apenas crescem cada vez mais na atmosfera')

st.header('Mas afinal!')

with st.container():
    # Função com a explicação sobre o que é gás carbono e o que causa para separar em duas colunas
    def gas_carbono():
        st.title ('O que é o Gás Carbono?')
        st.write ('Também é conhecido como dióxido de carbono, sua formula química é a a CO₂, é encontrado em temperatura ambiente, transparente, mas absorve radiação infravermelha, dessa forma, agindo como um gás do efeito estuda, uma das consequências disso é que o gás carbono é um dos principais causadores de mudanças climáticas atualmente.')
        st.write ('A principal causa da emissão desse gás é a queima de combustíveis fósseis, mas também pode ser liberado por respiração e decomposição de seres vivos, erupção vulcânica, queimadas e desmatamentos, processamentos industriais, além de também refinaria de petróleo, produção de aço e cimento.')
    def consequencias(): 
        st.title ('O que o Gás Carbono Causa?')
        st.write ('Principalmente, o aumento de gás carbono na atmosfera altera condições climáticas mundiais, dentro disso, o aquecimento do oceano que é responsável pela regulação do clima, também causa chuva ácida.')
        st.write ('Mas uma das principais consequências é o desequilíbrio do efeito estufa, assim, consequentemente elevando a temperatura da terra causando um efeito dominó com catástrofes climáticas, o que, por sua vez, já causou a extinção de diversas espécies da fauna e da')


# Separação do texto de apresentação em colunas
col1, col2 = st.columns(2)
# Exibição do texto em duas colunas
with col1:  # O que é o gás carbono
    gas_carbono()
with col2:  # COnsequências do gás carbono
    consequencias()

# Dashboard da página inicial
st.header("Dashboard")
st.write('Apresentação de todos os gráficos disponíveis para informação nesse banco de dados.')
st.write('Para informações mais específicas, selecione o gráfico desejado na barra lateral.')

# Repetição de exibição de gráficos vindos da navegação por botões, para que apareça também no dashboard
if button1:
    st.header('Emissão Anual de Gases por Setor Industrial')
    st.write('Esse gráfico remete à média emissão de gases por ano por diversos setores industriais.')
    st.write('No gráfico houve uma pequena simplificação em algumas partes para melhor observação visual, as repartições serão melhores explicadas.')
    st.write('Energia remete à elétrica, petróleo e carvão;')
    st.write('Terra remete ao uso, mudança de uso da terra e silvicultura;')
    st.write('Resíduos remete à praticamente todo resíduo humano, incluindo aterros e águas residuais.')
    setores_emissao()
if button2: 
    st.header('Emissão de Anual de Gases desde 1950')
    st.write('Esse gráfico remete à emissão de gás carbono por toneladas emitidos por ano desde os primeiros registros feitos com precisão, em 1950.')
    emissao_gas()
if button3: 
    st.header('Emissão de Gases por País, em Toneladas e em Porcentagem')
    st.write('Esses dois gráficos remetem à emissão de gás carbono por país, principalmente os dez principais que mais emitem esse gás anualmente. Juntos, esses países emitem em média 68,5% e 37702,16 de toneladas do gás carbono produzido por todo o mundo, anualmente.')
    st.title ('Emissão em Toneladas')
    paises_emissao_toneladas()
    st.title('Emissão em Porcentagem')
    paises_emissao_porcentagem()
if button4: 
    st.header('Emissão de Gases em Toneladas por País')
    st.write('Esse gráfico, em específico, remete à emissão de gases por toneladas emitida pelos top 10 países com maior taxa de produção de gases mundialmente')
    paises_emissao_toneladas()
if button5:
    st.header('Emissão de Gases em Porcentagem por País')
    st.write('Este gráfico exibe a emissão de gases por porcentagem com foco nos principais dez países com maior taxa de produção.')
    paises_emissao_porcentagem()
else:
    st.empty()


# Separação das colunas dos gráficos
graphic1, graphic2 = st.columns(2)
graphic3, graphic4 = st.columns(2)

# Exibição das colunas
with graphic1:
    paises_emissao_porcentagem()
with graphic2:
    paises_emissao_toneladas()
with graphic3:
    emissao_gas()
with graphic4:
    setores_emissao()
