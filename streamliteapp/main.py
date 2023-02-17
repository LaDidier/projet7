import time
import datetime
import json
import requests

import streamlit as st
import numpy as np
import streamlit.components.v1 as components
#from lime.lime_tabular import LimeTabularExplainer

#Onglet
tab1,tab2 = st.tabs(["Donnees client","Explain"])
with tab1:
    #st.image('PAD.png')
    tab1.subheader("Client")
    add_selectbox1 = st.selectbox(
        'Genre',
     ('Mr', 'Mme', 'Autre'))  
    title = st.text_input('Nom', 'Nom')
    title = st.text_input('Prenom', 'Prenom')
    title = st.text_input('Adresse', 'Adresse')
    title = st.text_input('CP', 'Code Postal')
    title = st.text_input('Ville', 'Ville')
    date_naissance = st.date_input(
    "Date de naissance",
    datetime.date(2001, 11, 9))

    data1 = st.number_input('data1')
    data2 = st.number_input('data2')
    data3 = st.number_input('data3')
    data4 = st.number_input('data4')
    data5 = st.number_input('data5')
    data6 = st.number_input('data6')
    data7 = st.number_input('data7')
    data8 = st.number_input('data8')
    data9 = st.number_input('data9')
    data10 = st.number_input('data10')
    data11 = st.number_input('data11')
    data12 = st.number_input('data12')
    data13 = st.number_input('data13')
    data14 = st.number_input('data14')
    data15 = st.number_input('data15')
    data16 = st.number_input('data16')
    data17 = st.number_input('data17')
    data18 = st.number_input('data18')
    data19 = st.number_input('data19')
    data20 = st.number_input('data20')

with st.form("my_form"):
    st.write("Soumettre le dossier")
   
   # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # st.write("slider", slider_val, "checkbox", checkbox_val)
        valeuratester = {
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,
        'data5': data5,
        'data6': data6,
        'data7': data7,
        'data8': data8,
        'data9': data9,
        'data10': data10,
        'data11': data11,
        'data12': data12,
        'data13': data13,
        'data14': data14,
        'data15': data15,
        'data16': data16,
        'data17': data17,
        'data18': data18,
        'data19': data19,
        'data20': data20,
        }
        r = requests.get('http://127.0.0.1:5002/solvabilite', json = valeuratester)
        solvable = r.json()
        print(r)
        if r.text != 'ok':
            print('sovlvable')
        else:
            print('non solvable')
with tab2:
    st.image('PAD.png')