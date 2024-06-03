# Estátisticas de Emissão de Gás Carbono na Atmosfera

## Visão Geral:
Este projeto faz parte do desafio de Python do Projeto Desenvolve Itabira. O objetivo principal é analisar e expor o aumento das emissões de dióxido de carbono (CO₂) na atmosfera desde 1949, a data mais antiga para a qual os dados estavam disponíveis, além dos países e setores da indústria que mais emitem o gás.
Os dados utilizados neste estudo incluem:
* Quantidade de CO₂ emitida anualmente por país em toneladas e sua comparação estátistica com porcentagem;
* Aumento das emissões ao longo dos anos;
* Percentual de emissões por setor econômico;

## Objetivo:

O objetivo desta pesquisa é alertar sobre o aumento significativo das emissões de CO₂ e como esse fenômeno pode impactar o planeta. Ao fornecer uma análise detalhada e baseada em dados históricos, esperamos conscientizar sobre a importância de adotar práticas sustentáveis e políticas ambientais eficazes.

## Instruções de Uso
#### 1 - Clone este repositório em seu computador local.

#### 2 - Baixe o VS Code em seu computador e o abra.

#### 3 - Instale as bibliotecas necessárias da seguinte maneira no terminal de seu VS Code:

    pip install streamlit pandas plotly

#### 4 - Execute o código Python da seguinte maneira em seu terminal VS Code:

    streamlit run gases.py

#### 5 - Clique no link que seu terminal oferecerá, assim abrindo o programa com a biblioteca streamlit.


## Tecnologias Utilizadas 
### Linguagem de Programação:
    Python
### Frameworks/Bibliotecas:
      Streamlit: Criação de interface de aplicação web interativa
      Pandas: Manipulação e análise de dados
      Plotly Express: Criação de gráficos interativos
      Plotly Graph Objects: Criação de gráficos interativos
    

## Dados:

### Arquivos .csv
* "Emissão.csv" remete à quantidade de gás carbono por tonelada emitidos na atmosfera em seus respectivos anos:
    - "Anos" remete aos anos que houveram emissãoo de gás carbono;
    - "Toneladas" à quantidade de toneladas de gás carbono emitidas naquele ano;
* "Países.csv" possuí dados dos dez países que mais emitem gás carbono com sua quantidade em toneladas e em porcentagem, em comparação com os demais países:
    - "Países" remetem aos países ao qual foram feitos as medições de porcentagem e toneladas emitidos, "demais países" são os outros países não inclusos no top 10;
    - "Porcentagem" se dá à porcentagem de quanto do gás carbono emitido na atmosfera em um ano, aquele país colaborou;
    - "Toneladas" é a quantidade do gás emitido na atmosfera em um ano por aquele país;
* "Setores.csv" compara quanto gás carbono cada uma das maiores indústrias do mundo emitem:
    - "Setores" são os setores econômigos da indústria ao qual entraram nessa pesquisa para comparação de emissão de gás;
    - "Porcentagem" é com quanto da emissão total aquele setor colaborou.

### Arquivo docs
[Dados brutos com fontes e gráficos](https://docs.google.com/document/d/1J262HJvC8yMbw2kXbW4e1Yxf2-N2ifQlEYi5bC1h6bc/edit?usp=sharing
)

## Projeto

|Arquivo|Função|
| :-------- | :------- |
|Gases.py| Arquivo contendo o código do projeto|
|Gases.css| Arquivo contendo a estilização do projeto|
|Países.csv| Dados sobre emissão de gás dos dez países mais emissores|
|Emissão.csv| Dados sobre a emissão de gás carbono de acordo com anos de medissão|
|Setores.csv| Dados sobre emissão de gás carbono pelos setores da indústria|




## Resultados:
### Emissões por País:
* Identificação dos países com maiores emissões de CO₂ e análise de suas contribuições percentuais ao total global.
### Tendências Anuais: 
* Avaliação do aumento das emissões ano a ano, destacando períodos de crescimento mais acentuado.
### Setores Econômicos: 
* Determinação dos setores econômicos que mais contribuem para as emissões de CO₂, permitindo direcionar esforços de mitigação de forma mais eficaz.



## Conclusão: 

A pesquisa demonstra um aumento abrupto das emissões de CO₂ desde 1949, com impactos potencialmente devastadores para o meio ambiente e a saúde global. A conscientização sobre esses dados é fundamental para promover mudanças e adotar estratégias que visem à redução das emissões, protegendo assim o futuro do nosso planeta.

Este projeto reflete a importância de abordar questões ambientais com seriedade e dedicação. Ao compartilhar esses insights, espero contribuir para um futuro mais sustentável e consciente.



## Contato: 

### Programador: Luke Malaquias Lage
[LinkedIn](https://www.linkedin.com/in/luke-malaquias-lage-04022a232/) 
