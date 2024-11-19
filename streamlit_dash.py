import streamlit as st

import streamlit as st


st.set_page_config(
   page_title='Dashboard',
   page_icon='🧮',
   layout='wide',
   initial_sidebar_state='expanded',
)

st.write('Olá, mundo!')
st.sidebar.title('Olá título da sidebar!')
st.sidebar.write('Olá sidebar!')

caixa_selecao = st.sidebar.selectbox(
    label='Olá selectbox! Você gosta de machine learning?',
    options=('Sim', 'Claro', 'Muito'),
    index=2)

if caixa_selecao != 'Sim':
    st.title('Olá título!')
    st.write('Olá mundo!')
    
    st.markdown('Olá, equação! $f(x)=x^{2}$')
    
    st.header('Olá, seção 1!')
    
    codigo = '''
    # Olá, código!
    def x_squared(x):
        return x**2
    '''
    st.code(codigo, language='python')
    
    def click_botao():
        st.write('Botão clicado!')
    botao = st.button('Olá, botão!', on_click=click_botao)
    
    x = st.slider(label='Escolha um número entre 0 e 1', min_value=0.0, max_value=1.0, step=0.0001)
    st.write(f'Número escolhido: {x}')
    
if caixa_selecao == 'Sim':
    
    st.title('Vamos criar um gráfico personalizado!')
    
    import pandas as pd
    import seaborn as sns
    sns.set_theme(rc={'figure.figsize':(8,5)})
    df = pd.read_csv('diabetes_dataset.csv')
    
    col_x = st.selectbox(label='Eixo x', options=df.columns, index=0)
    col_y = st.selectbox(label='Eixo y', options=df.columns, index=1)
    
    cols = st.columns(2)
    with cols[0]:
        plot = sns.displot(x=df[col_x], y=df[col_y])
        st.pyplot(plot.fig)
    with cols[1]:
        plot = sns.displot(x=df[col_y], y=df[col_x])
        st.pyplot(plot.fig)
    