import pandas as pd
import plotly.express as px
import streamlit as st



@st.cache_data
def carregar_dados():
    df = pd.read_csv('cursos-prouni.csv')
    return df

dados = carregar_dados()


def intro():
    st.title('Análise do PROUNI 2018')
    st.markdown(f"""
    ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
    ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
    ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
    [![Plotly](https://img.shields.io/badge/Plotly-v5.0-blue?logo=plotly&logoColor=white)](https://plotly.com/)


    --- 
    ### Objetivo
    O objetivo deste projeto é analisar os dados do **PROUNI 2018**, um programa do governo federal que oferece bolsas de estudo em instituições privadas para estudantes de baixa renda. Através dessa análise, busco entender as **tendências** do programa e avaliar seu **impacto** nas universidades participantes.
    
    ### Tecnologias Utilizadas
    - Python
    - Pandas
    - Streamlit
                
    ### Metodologia
    - **Carregamento e Limpeza de Dados**: Primeiramente, os dados serão carregados e limpos para garantir que não há valores faltantes ou inconsistências.
    - **Análise Exploratória**: Em seguida, será realizada uma análise exploratória para entender melhor a distribuição dos dados, identificando padrões e tendências.
    - **Visualizações**: Para facilitar a compreensão, serão gerados gráficos interativos, como distribuições de cursos por estado e por área de estudo.

    ### Resultados Esperados
    Espera-se que a análise revele as principais características do programa PROUNI em 2018, como:
    - Quais estados possuem o maior número de bolsas.
    - Quais áreas de estudo têm maior procura.
    - Quais universidades o povo está escolhendo.
    - Encontrar estados que tem mais pessoas passando.

    ### Conclusão
    Com base nos resultados obtidos, será possível entender o alcance e os impactos do **PROUNI** em 2018, o que pode fornecer informações valiosas para futuras políticas públicas de educação.

""")
    
def ver_df():
    st.title('DataFrame PROUNI 2018')
    st.markdown('---')
    st.dataframe(dados)
    st.markdown("""
    """)
    st.markdown('---')
    st.write('cursos-prouni-2018.csv')
    st.download_button(
        label="Baixar CSV",
        data=dados.to_csv(index=False),
        file_name='cursos-prouni-2018.csv',
        mime="text/csv"
    )
    
def analise():
    st.title('Análise dos Dados')
    st.markdown('---')
    st.markdown('#### Ver as primeiras 5 linhas')
    st.write(dados.head())
    st.markdown('#### Limpeza de dados')
    dados_limpos = dados.dropna()
    st.write(dados_limpos.head())
    st.markdown('#### Áreas de estudo com maior procura')
    curso_contagem = dados_limpos['nome'].value_counts()
    st.write(curso_contagem.head(50))
    col, col2 = st.columns(2)
    with col:
        st.markdown('#### Top 10 Estados que mais passaram')
        curso_contagem = dados_limpos['uf_busca'].value_counts()
        st.write(curso_contagem.head(10))
    with col2:
        st.markdown('#### Top 10 Estados que menos passavam')
        curso_contagem = dados_limpos['uf_busca'].value_counts().sort_values(ascending=True)
        st.write(curso_contagem.head(10))
    st.markdown('#### Universidade que mais entraram')
    curso_contagem = dados_limpos['universidade_nome'].value_counts()
    st.write(curso_contagem.head(10))
    st.markdown('---')

dados_limpos = dados.dropna()
curso_contagem = dados_limpos['nome'].value_counts()

def conclusao():
    st.title('Insights da Análise')
    st.markdown('---')
    
    # Áreas de estudos mais procuradas
    st.markdown('#### Áreas de Estudos Mais Procuradas')
    fig1 = px.bar(
        curso_contagem,
        x=curso_contagem.index,
        y=curso_contagem.values,
        labels={'x': 'Área de Estudo', 'y': 'Quantidade de Aprovação'},
        title='Áreas de Estudo mais Procuradas no PROUNI 2018',
        color=curso_contagem.values,
        color_continuous_scale='Viridis'
    )
    st.plotly_chart(fig1)

    st.markdown('---')

    # Gráfico de estados com maior taxa de aprovação
    st.markdown('#### Top 10 Estados com Maior Taxa de Aprovação')
    estado_contagem = dados_limpos['uf_busca'].value_counts()
    fig2 = px.bar(
        estado_contagem.head(10),
        x=estado_contagem.head(10).index,
        y=estado_contagem.head(10).values,
        labels={'x': 'Estado', 'y': 'Número de Aprovações'},
        title='Top 10 Estados com Maior Número de Aprovações no PROUNI 2018',
        color=estado_contagem.head(10).values,
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig2)

    st.markdown('---')

    # Gráfico de universidades mais escolhidas
    st.markdown('#### Top 10 Universidades Mais Escolhidas')
    universidade_contagem = dados_limpos['universidade_nome'].value_counts()
    fig3 = px.bar(
        universidade_contagem.head(10),
        x=universidade_contagem.head(10).index,
        y=universidade_contagem.head(10).values,
        labels={'x': 'Universidade', 'y': 'Número de Aprovações'},
        title='Top 10 Universidades Mais Escolhidas no PROUNI 2018',
        color=universidade_contagem.head(10).values,
        color_continuous_scale='Cividis'
    )
    st.plotly_chart(fig3)

    st.markdown('---')

    # Gráfico de estados com menos aprovação
    st.markdown('#### Top 10 Estados com Menor Taxa de Aprovação')
    fig4 = px.bar(
        estado_contagem.tail(10),
        x=estado_contagem.tail(10).index,
        y=estado_contagem.tail(10).values,
        labels={'x': 'Estado', 'y': 'Número de Aprovações'},
        title='Top 10 Estados com Menor Número de Aprovações no PROUNI 2018',
        color=estado_contagem.tail(10).values,
        color_continuous_scale='Reds'
    )
    st.plotly_chart(fig4)

    st.markdown('---')

    st.markdown('### Conclusões Importantes')
    st.write("""
    - **Áreas de Estudo**: Cursos como **Pedagogia**, **Administração**, e **Direito** se destacam pela alta demanda de bolsas no PROUNI 2018.
    - **Estados**: Estados como **São Paulo** e **Paraná** lideram a lista de aprovações, enquanto estados como **Roraima** e **Amazonas** possuem taxas de aprovação mais baixas.
    - **Universidades**: **Universidade UNINTER** e **Universidade UNICSUL** são as mais procuradas pelos candidatos do PROUNI.
    
    Essas informações ajudam a entender a distribuição e as tendências do programa PROUNI 2018, permitindo insights valiosos para a melhoria da política de bolsas e educação no Brasil.
    """)



st.sidebar.header('Menu')

aba_selecionada = st.sidebar.selectbox(
    'Escolha uma aba:',
    ('Introdução', 'Ver DataFrame', 'Análise', 'Conclusão')
)

if aba_selecionada == 'Introdução':
    intro()
elif aba_selecionada == 'Ver DataFrame':
    ver_df()
elif aba_selecionada == 'Análise':
    analise()
elif aba_selecionada == 'Conclusão':
    conclusao()