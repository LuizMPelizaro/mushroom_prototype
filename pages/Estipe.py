import streamlit as st

st.markdown("## Estipe do cogumelo")

stalk_shape = st.selectbox(
    'Forma da estipe:',
    ['Ampliação', 'Afunilado']
)

stalk_root = st.selectbox(
    'Raiz da estipe:',
    ['Bulboso', 'Clube', 'Copo', 'Uniforme', 'Rizomorfos', 'Enraizado', 'Faltante']
)

stalk_surface_above_ring = st.selectbox(
    'Superfície da estipe acima do anel:',
    ['Fibroso', 'Escamoso', 'Sedoso', 'Liso']
)

stalk_surface_below_ring = st.selectbox(
    'Superfície da estipe abaixo do anel:',
    ['Fibroso', 'Escamoso', 'Sedoso', 'Liso']
)

stalk_color_above_ring = st.selectbox(
    'Cor da estipe acima do anel:',
    ['Marrom', 'Bege', 'Canela', 'Cinza', 'Laranja', 'Rosa', 'Vermelho', 'Branco', 'Amarelo']
)

stalk_color_below_ring = st.selectbox(
    'Cor da estipe abaixo do anel:',
    ['Marrom', 'Bege', 'Canela', 'Cinza', 'Laranja', 'Rosa', 'Vermelho', 'Branco', 'Amarelo']
)
