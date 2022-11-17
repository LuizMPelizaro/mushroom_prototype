import pickle

import numpy as np
import streamlit as st


def call_model() -> pickle:
    with open(r"./model/model.pickle", "rb") as input_file:
        model = pickle.load(input_file)

    return model


def return_proba(proba):
    if proba > 0.5:
        st.success(f"Não Toxico: {np.round(proba, 2)}")
    else:
        st.error(f"Toxico: {np.round(proba, 2)}")
