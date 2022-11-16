import streamlit as st

st.markdown("## Chapéu da cogumelo")
cap_shape = st.selectbox(
    'Forma do chapéu:',
    ['Sino', 'Cone', 'Convexo', 'Plano', ' Arredondada', 'Fundo']
)

cap_surface = st.selectbox(
    'Superfície do chapéu:',
    ['Fibroso', 'Sulcos', 'Escamoso', 'Liso']
)

cap_color = st.selectbox(
    'Cor do chapéu:',
    ['Marrom', 'Bege', 'Canela', 'Cinza', 'Verde', 'Rosa', 'Roxo', 'Vermelho', 'Branco', 'Amarelo']
)
