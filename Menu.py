import pandas as pd
from PIL import Image

from pages.Anel import *
from pages.Chapeu import *
from pages.Estipe import *
from pages.Guelras import *
from pages.Outros import *
from pages.Veu import *
from utils import regex
from utils.utils import call_model, return_proba

esquema_cogumelo = Image.open('img/esquema_cogumelo.jpg')

st.set_page_config(
    page_title="Classificador de cogumelos",
    page_icon='🍄',
    initial_sidebar_state='auto',
    layout='centered'
)

st.markdown("# Classificador de cogumelos")
st.image(esquema_cogumelo)

st.sidebar.title("Selecione a parte do cogumelo")

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

model = call_model()

r = model.predict_proba(df)

proba = r[:, 1][0]

st.markdown(f"### Resultado do cogumelo pesquisado:")

return_proba(proba)

st.markdown(
    '### Projeto com o intuido de estudos de machine learning ,'
    ' NÃO SE ARRICAR COMENDO COGUMELOS !!!')
