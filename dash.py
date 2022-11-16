import pickle

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

from utils import regex

image = Image.open('img/cogumelo.jpg')
esquema_cogumelo = Image.open('img/esquema_cogumelo.jpg')

st.set_page_config(
    page_title="Classificador de cogumelos",
    page_icon='🍄'
)

st.markdown("# Classificador de cogumelos")
st.image(image)

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

st.markdown("## Véu do cogumelo ")

veil_type = st.selectbox(
    'Tipo de véu:',
    ['Parcial', 'Total']
)

veil_color = st.selectbox(
    'Cor do véu:',
    ['Marrom', 'Laranja', 'Branco', 'Amarelo']
)

st.markdown("## Anel do cogumelo ")

ring_number = st.selectbox(
    'Número de aneis:',
    ['Nenhum', 'Um', 'Dois']
)

ring_type = st.selectbox(
    'Tipo de anel:',
    ['Teia', 'Evanescente', 'Vistoso', 'Grande', 'Nenhum', 'Pingente', 'Revestimento', 'Zona']
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

data = {
    'cap-shape': [cap_shape],
    'cap-surface': [cap_surface],
    'cap-color': [cap_color],
    'bruises': [bruises],
    'odor': [odor],
    'gill-attachment': [gill_attachment],
    'gill-spacing': [gill_spacing],
    'gill-size': [gill_size],
    'gill-color': [gill_color],
    'stalk-shape': [stalk_shape],
    'stalk-root': [stalk_root],
    'stalk-surface-above-ring': [stalk_surface_above_ring],
    'stalk-surface-below-ring': [stalk_surface_below_ring],
    'stalk-color-above-ring': [stalk_color_above_ring],
    'stalk-color-below-ring': [stalk_color_below_ring],
    'veil-type': [veil_type],
    'veil-color': [veil_color],
    'ring-number': [ring_number],
    'ring-type': [ring_type],
    'spore-print-color': [spore_print_color],
    'population': [population],
    'habitat': [habitat]
}

data = regex.RegexMush(data)
data.regex()

df = pd.DataFrame(data.dict_mush)

with open(r"./model/model.pickle", "rb") as input_file:
    model = pickle.load(input_file)

r = model.predict_proba(df)

proba = r[:, 1][0]
if proba > 0.5:
    st.success(f"Não Toxico: {np.round(proba, 2)}")
else:
    st.error(f"Toxico: {np.round(proba, 2)}")