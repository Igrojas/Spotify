import pandas as pd
import altair as alt

def top_weeks(df):
    top_50 = df.head(50)
    top_50.sort_values("weeks_on_chart",ascending=False)

    chart = alt.Chart(top_50.head(20)).mark_bar(
        color='#2E865F',
    ).encode(
        x = alt.X("track_name", sort= '-y', axis=alt.Axis(title="Canción")),
        y = alt.Y("weeks_on_chart", axis=alt.Axis(title="Semanas en el Top")),
        tooltip = ["track_name", "artist_names", "weeks_on_chart"]
    ).properties(
        title="20 canciones con mas semanas en el top del top 200 semanal",
        height = 500,
    )

    return chart

def top_tracks(df):
    top_50 = df.head(50)
    top_50.sort_values("weeks_on_chart",ascending=False)
    
    chart = alt.Chart(top_50.head(15)).mark_bar(
        color='#1DB954',
    ).encode(
        y = alt.Y("track_name", sort= '-x', axis = alt.Axis(title="Canción")),
        x = alt.X('streams', axis=alt.Axis(title = "Número de reproducciones")),
        tooltip = ["track_name", "artist_names", "streams"]
    ).properties(
        title="20 canciones con mas reproducciones del top 200 semanal",
        # height = 400
    )

    return chart

def Top_streamed(df):
    artists_streams = df.groupby("first_artist")["streams"].sum().reset_index()
    artists_streams = artists_streams.sort_values("streams", ascending=False).head(10)

    # Crea el gráfico circular
    chart = alt.Chart(artists_streams).encode(
        alt.Theta("streams:Q",sort='ascending').stack(True),
        alt.Color("first_artist:N").legend(None),
        tooltip=["first_artist:N", "streams:Q"]
    ).properties(
        title='Top 10 mas escuchado',
        width = 600,
        height= 600
    )

    pie = chart.mark_arc(outerRadius=200)
    text = chart.mark_text(radius=250, size=15).encode(text="first_artist:N")

    return pie + text

def mas_escuchado(df):
    mas_escuchados = df.groupby("first_artist")["streams"].sum().sort_values(ascending=False).reset_index().iloc[0]
    primer_artista_nombre = mas_escuchados["first_artist"]
    primer_artista_streams = mas_escuchados["streams"]
    return primer_artista_nombre, primer_artista_streams
