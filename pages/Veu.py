import streamlit as st

st.markdown("## Véu do cogumelo ")

veil_type = st.selectbox(
    'Tipo de véu:',
    ['Parcial', 'Total']
)

veil_color = st.selectbox(
    'Cor do véu:',
    ['Marrom', 'Laranja', 'Branco', 'Amarelo']
)
