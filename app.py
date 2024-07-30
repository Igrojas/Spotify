import streamlit as st
import pandas as pd
from utils import *



st.set_page_config(page_title="Top semanal Chile",
                   layout="wide")

paises = {
    "Chile": "cl",
    "Colombia": "co",
    "Brazil": "br",
    "Global": "global"
}

# Crear un selectbox para seleccionar el país
pais_seleccionado = st.selectbox(
    "Selecciona un país",
    options=list(paises.keys())  # Mostrar los nombres de los países en el selectbox
)

codigo_pais = paises[pais_seleccionado]

df = pd.read_csv("data/regional-" + codigo_pais +"-weekly-2024-07-25.csv", sep=",")


first_artist = []
for row, data in df.iterrows():
    # print(row, data['artist_names'].split(',')[0])
    first_artist.append(data['artist_names'].split(',')[0])

df["first_artist"] = first_artist

st.title("Top semanal en" + " " + pais_seleccionado)
st.header("25 de julio de 2024")

st.write("-----")

with st.container():

    col1, col2, col3= st.columns(3)
    chart_top_track = top_tracks(df)
    primer_artista_nombre, primer_artista_streams =  mas_escuchado(df)
    chart_top_streamed = Top_streamed(df)

    with col1:
        st.altair_chart(chart_top_track, use_container_width=True)
        
    with col2:
        st.markdown(f"""

                <div style="text-align: center;">
                    <h2 style="font-weight: bold; color: #b3b3b3;font-family: sans-serif;">Artista más escuchado</h2>
                    <span style="font-size: 35px; color: #1DB954; font-weight: bold;">
                    {primer_artista_nombre}
                    </span>
                </div>
                    """, unsafe_allow_html=True)
        
    with col2:
            st.markdown(f"""
                    <div style="text-align: center;">
                        <h2 style="font-weight: bold; color: #b3b3b3; font-family: sans-serif;">Número de reproducciones</h2>
                        <span style="font-size: 35px; color: #1DB954; font-weight: bold;">
                        {primer_artista_streams:,}
                        </span>
                    </div>
                        """, unsafe_allow_html=True)
    
    with col3:
         st.altair_chart(chart_top_streamed, use_container_width=True)
        

    chart_top_weeks = top_weeks(df)
    primer_artista_nombre, primer_artista_weeks = mas_semanas(df)
    pie_top_weeked = Top_weeked(df)
    col1, col2, col3= st.columns((3))


    with col1:
        st.markdown(f"""

                <div style="text-align: center;">
                    <h2 style="font-weight: bold; color: #b3b3b3; font-family: sans-serif;">Artista con más semanas en el top</h2>
                    <span style="font-size: 35px; color: #1DB954; font-weight: bold;">
                    {primer_artista_nombre}
                    </span>
                </div>
                    """, unsafe_allow_html=True)
        
    with col1:
            st.markdown(f"""
                    <div style="text-align: center;">
                        <h2 style="font-weight: bold; color: #b3b3b3; font-family: sans-serif;">Número de semanas en el top</h2>
                        <span style="font-size: 35px; color: #1DB954; font-weight: bold;">
                        {primer_artista_weeks:,}
                        </span>
                    </div>
                        """, unsafe_allow_html=True)
            
    with col2:
         st.altair_chart(pie_top_weeked, use_container_width=True)

    with col3:
        st.altair_chart(chart_top_weeks, use_container_width=True)


st.write("-----")
st.header("Información por artista")


artistas_unicos = df['first_artist'].unique()

artista_seleccionado = st.selectbox('Selecciona un artista', artistas_unicos)

df_artist = df[df["first_artist"] == artista_seleccionado]
if artista_seleccionado:
#     # Llamar a tus funciones para mostrar datos del artista
#     mostrar_datos_artista(artista_seleccionado)

    col1, col2 = st.columns(2)

    chart_top_weeks = top_weeks(df_artist)
    chart_top_track = top_tracks(df_artist)

    with col1:
        st.altair_chart(chart_top_weeks, use_container_width=True)

    with col2:
        st.altair_chart(chart_top_track, use_container_width=True)