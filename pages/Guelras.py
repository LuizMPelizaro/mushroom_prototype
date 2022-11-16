import streamlit as st

st.markdown("## Guelras do cogumelo")

gill_attachment = st.selectbox(
    'Fixação das guelras',
    ['Anexado', 'Descendente', 'Livre', 'Entalhado']
)

gill_spacing = st.selectbox(
    'Espaçamento entre as guelras:',
    ['Perto', 'Sobrecarregado', 'Afastadas']
)

gill_size = st.selectbox(
    'Tamanho das guelras',
    ['Largo', 'Estreita']
)

gill_color = st.selectbox(
    'Cor das guelras:',
    ['Preto', 'Marrom', 'Bege', 'Chocolate', 'Cinza', 'Verde', 'Laranja', 'Rosa', 'Roxa', 'Vermelho', 'Branco',
     'Amarelo']
)