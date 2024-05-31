# Processamento de bibliotecas usadas no código, uso de cada no comentário ao lado da importação
import pandas as pd #Biblioteca para processamento de dados
import plotly.express as px #Biblioteca para criação de gráficos
import plotly.graph_objects as go # Biblioteca para criação de gráficos
import streamlit as st #Biblioteca para criação de servidor web

# Configurações gerais da aplicação
st.set_page_config(
    page_title="Emissão de Gas Carbônico na Atmosfera",
    page_icon="💨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Carregamento de estilização CSS vinda da pasta Gases.css
with open("Gases.css", "r") as fp:
    css = fp.read()  # Lê o conteúdo do arquivo CSS
    st.write(f"<style>{css}</style>", unsafe_allow_html=True)

# DataFrames feitos com Pandas das informações que serão usadas nos gráficos, para ver qual arquivo será qual gráfico, ver comentário a cima de cada função

# Dicionário usado para fazer o DataFrame dos países com maior taxa de emissão de gás carbono
emissao_paises = pd.read_csv ('Países.csv')
paises_df = pd.DataFrame(emissao_paises)


# Dicionário usado para fazer o DataFrame com a quantidade de gás carbono emitido em bilhões ao longo dos anos
emissao_ano = pd.read_csv('Emissão.csv')
emissao_df = pd.DataFrame(emissao_ano)

# Dicionário usado para fazer o DataFrame com os setores que mais emitem gás carbono atualmente
setores = pd.read_csv('Setores.csv') 
setores_df = pd.DataFrame(setores)

# Funções usadas para montar os gráficos para melhor organização de código, para descrições específicas de cada função, ver comentário ao lado da def


# Função para criação dos gráficos usados para visualização dos países que mais produzem gás carbono
def paises():
    fig = px.scatter(
        x = paises_df ['Países'], # Utilize a variável correta ou verifique o nome da coluna
        y = paises_df ['Porcentagem'],
        color = paises_df ['Toneladas'], 
        size = paises_df ['Porcentagem'],
        labels={"x": "Países", "y": "Porcentagem", "color": "Toneladas"},
        title="Dez Países que Mais Emitem Gás Carbono",
    )
    st.plotly_chart(fig)

# Função para carregar o gráfico de barra representando toneladas de gás carbono emitido
def emissao_gas (): 
    fig = px.line(
        emissao_df, 
        x = 'Anos', 
        y = 'Toneladas', 
        title = 'Emissão de Gás Carbono por Anos em Toneladas'
    )
    st.plotly_chart(fig)

# Função para carregar o gráfico de pizza representando os setores que mais emitem gás carbono
def setores_emissao (): 
    fig = px.bar(
        setores_df,
        x="Setores",
        y="Porcentagem",
        title="Emissão de Gás de Diversos Setores",
    )
    st.plotly_chart(fig)

# Área para criação de colunas para botões de navegações entre os gráficos
# Criação de colunas para separação de dois gráficos ao apertar o botão
paises1, paises2 = st.columns(2)

# Side bar com navegação entre gráficos e informações sobre o desenvolvedor da aplicação
with st.sidebar:
    # Select box apresentação individual dos gráficos que aparecerão na tela, para ver qual botão é referente à qual gráfico, ver nome de cada botão
    st.title('Navegação')
    option = st.selectbox(
        'Navegue entre gráficos para encontrar informações específicas sobre cada um deles',
        ('Emissão por Setor', 'Emissão de Tonelada por Ano', 'Emissão por País', 'Fechar Gráficos'),
        index = None,
        placeholder = 'Selecione um Gráfico'
    )

    # Botões para exibição do que se trata esse dashboard
    sobre = st.radio(
        'Deseja saber sobre o que se trata esse dashboard e o pensamento para sua criação?',
        ['Sim!', 'Não!'],
        index = None
    )

    # Botões para exibição e exclusão de informações sobre o que é o Gás Carbono]
    info = st.radio(
        "Você sabe o que é o gás ou o que ele causa?",
        ["O que é?", "O que Causa?", "Fechar Informações"],
        index=None,
    )

    # Navegação para a alteração do país que será exibido a emissão de gás carbono
    nav_pais = st.select_slider(
        'Navegue por esta barra para alterar a exibição da emissão de gás de países específicos',
        ['China', 'Estados Unidos', 'União Europeia', 'Índia', 'Rússia', 'Japão', 'Brasil', 'Indonésia', 'Iran', 'Coreia do Sul']
    )

    # Informações sobre o desenvolvedor da aplicação
    # Colocar o robozinho do desenvolve aqui como marcação
    st.title('Quem sou eu?')
    st.write('Programador: Luke Malaquias Lage')
    st.write('PDITA: 172')

# Código usado para renderização dos dados para a segunda métrica do dashboard

pais_selecionado = nav_pais.lower()  # Converte o país para minúscula
pais_df = paises_df.loc[paises_df["Países"].str.lower() == pais_selecionado]

emissao_pais = pais_df['Toneladas'].values[0]  # Assume que há apenas um valor de emissão


# Container de métricas sobre emissão de gás carbono, para ver qual métrica representa o que, ver comentário ao lado da métrica


metric1, metric2, metric3 = st.columns(3)
metric1.metric(
    label="Produção de Gás Carbono por Ano", 
    value="52240.86 Toneladas"
)  # Métrica de produção de gás carbono anualmente

metric2.metric (
    label = 'Emissão de Gás Carbono por País em Toneladas',
    value = emissao_pais
)

metric3.metric (
    label = 'Primeira Medição de Gás Registrada',
    value = "6 Toneladas"
)

# Funções para a criação de interatividade de um gráfico que irá aparecer ao selecionar a emissão por ano

def comparacao_ano():
    year = st.select_slider(
        'Selecione o ano que você deseja ver a comparação com a primeira medição',
        [1949, 1950, 1989, 2000, 2019, 2021]
    )
    emissao_ano_filtro = emissao_df [emissao_df['Anos'] == year] # Filtra o dataframe por ano 
    emissao_ano = emissao_ano_filtro['Toneladas'].iloc[0]
    
    primeira_emissao = emissao_df ['Toneladas'].min() # Pega o menor número do arquivo csv e transforma na primeira emissão

    fig = go.Figure(  # Exibição do gráfico
        go.Indicator(
            mode="gauge + number + delta",
            value = emissao_ano,
            title = {"text": "Comparação Anual Desde a Primeira Mediação"},
            delta = {"reference": primeira_emissao},
        )
    )
    st.plotly_chart(fig)

if option == "Emissão por Setor":
    st.header('Emissão Anual de Gases por Setor Industrial')
    st.write('Esse gráfico remete à média emissão de gases por ano por diversos setores industriais.')
    st.write('No gráfico houve uma pequena simplificação em algumas partes para melhor observação visual, as repartições serão melhores explicadas.')
    st.write('Energia remete à elétrica, petróleo e carvão;')
    st.write('Terra remete ao uso, mudança de uso da terra e silvicultura;')
    st.write('Resíduos remete à praticamente todo resíduo humano, incluindo aterros e águas residuais.')
    setores_emissao()
elif option == "Emissão de Tonelada por Ano":
    st.header('Emissão de Anual de Gases desde 1950')
    st.write('Esse gráfico remete à emissão de gás carbono por toneladas emitidos por ano desde os primeiros registros feitos com precisão, em 1950.')
    comparacao_ano()
elif option == 'Emissão por País':
    st.header('Emissão de Gases por País')
    st.write('Esse gráfico remete à emissão de gás carbono por país, principalmente os dez principais que mais causam a emissão deste gás anualmente, os dados expõe tanto a porcentagem quanto a quantidade em toneladas desses dados.',)
    st.write('Juntos esses países emitem em média, 68,5% e 37702,16 de toda a emissão mundial em um ano')
    st.write('As cores do gráfico ficam cada vez mais escuras a medida que a quantidade em porcentagem de emissão de gases aumenta.')
    paises()
else:
    st.empty()

# Sobre o que é o Dashboard

if sobre == 'Sim!':
    st.header ('Emissão de Gás Carbono na Atmosfera')
    
    st.write ('Essa aplicação revolve em torno da exposição da emissão de gás carbônico na atmosfera desde a era da revolução industrial e quais, nesse momento, são os maiores emissores')
    st.write ('O objetivo da criação desse dashboard foi para a existência de uma discussão sobre o aumento da nossa poluição, como humanidade e como, com o passar dos anos, mesmo com os acordos entre países para a diminuição da emissão de gases, eles apenas crescem cada vez mais na atmosfera')
else:
    st.empty()

# Página de informações sobre o que é e o que o Gás Carbono causa
if info == 'O que é?':
    st.title ('O que é o Gás Carbono?')
    st.write ('Também é conhecido como dióxido de carbono, sua formula química é a a CO₂, é encontrado em temperatura ambiente, transparente, mas absorve radiação infravermelha, dessa forma, agindo como um gás do efeito estuda, uma das consequências disso é que o gás carbono é um dos principais causadores de mudanças climáticas atualmente.')
    st.write ('A principal causa da emissão desse gás é a queima de combustíveis fósseis, mas também pode ser liberado por respiração e decomposição de seres vivos, erupção vulcânica, queimadas e desmatamentos, processamentos industriais, além de também refinaria de petróleo, produção de aço e cimento.')
elif info == "O que Causa?":
    st.title ('O que o Gás Carbono Causa?')
    st.write ('Principalmente, o aumento de gás carbono na atmosfera altera condições climáticas mundiais, dentro disso, o aquecimento do oceano que é responsável pela regulação do clima, também causa chuva ácida.')
    st.write ('Mas uma das principais consequências é o desequilíbrio do efeito estufa, assim, consequentemente elevando a temperatura da terra causando um efeito dominó com catástrofes climáticas, o que, por sua vez, já causou a extinção de diversas espécies da fauna e da')
else:
    st.empty()

# Dashboard da página inicial

paises()

# Separação das colunas dos gráficos
graphic1, graphic2 = st.columns(2)

# Exibição das colunas
with graphic1:
    emissao_gas()
with graphic2:
    setores_emissao()
