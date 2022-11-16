import streamlit as st

st.set_page_config(
    page_title="Outras informações",
    page_icon='🍄'
)
st.markdown("## Outras informações")

bruises = st.selectbox(
    'Hematomas:',
    ['Sim', 'Não']
)

odor = st.selectbox(
    'Cheiro :',
    ['Amêndoa', 'Anis', 'Creosote', 'Peixe', 'Fétido', 'Mofo', 'Nenhum', 'Pungente', 'Picante']
)

spore_print_color = st.selectbox(
    'Cor de impressão dos esporos :',
    ['Preto', 'Marrom', 'Bege', "Chocolate", 'Verde', 'Laranja', 'Roxo', 'Branco', 'Amarelo']
)

population = st.selectbox(
    'População :',
    ['Abundante', 'Agrupado', 'Numeroso', 'Disperso', 'Varios', 'Solitario']
)

habitat = st.selectbox(
    'Habitate :',
    ['Grama', 'Folhas', 'Prados', 'Caminho', 'Urbano', 'Lixo', 'Bosques']
)