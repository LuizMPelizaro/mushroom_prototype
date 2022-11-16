import streamlit as st

st.markdown("## Anel do cogumelo ")

ring_number = st.selectbox(
    'Número de aneis:',
    ['Nenhum', 'Um', 'Dois']
)

ring_type = st.selectbox(
    'Tipo de anel:',
    ['Teia', 'Evanescente', 'Vistoso', 'Grande', 'Nenhum', 'Pingente', 'Revestimento', 'Zona']
)