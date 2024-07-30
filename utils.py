import pandas as pd
import altair as alt

def top_weeks(df):
    top_50 = df.head(50)
    top_50.sort_values("weeks_on_chart",ascending=False)

    chart = alt.Chart(top_50.head(15)).mark_bar(
        color='#1DB954',
    ).encode(
        y = alt.Y("track_name", sort= '-x', axis=alt.Axis(title="Canción")),
        x = alt.X("weeks_on_chart", axis=alt.Axis(title="Semanas en el Top")),
        tooltip = ["track_name", "artist_names", "weeks_on_chart"]
    ).properties(
        title="20 canciones con mas semanas en el top del top 200 semanal",
    )

    return chart

def top_tracks(df):
    top_50 = df.head(50)
    top_50.sort_values("weeks_on_chart",ascending=False)
    
    chart = alt.Chart(top_50.head(10)).mark_bar(
        color='#1DB954',
    ).encode(
        x = alt.X("track_name", sort= '-y', axis = alt.Axis(title="Canción")),
        y = alt.Y('streams', axis=alt.Axis(title = "Número de reproducciones")),
        tooltip = ["track_name", "artist_names", "streams"]
    ).properties(
        title="20 canciones con mas reproducciones del top 200 semanal",
        height = 400
    ).configure_axis(
        labelFontSize=14,
        titleFontSize=14
    ).configure_title(
        fontSize=15
    )

    return chart

def Top_streamed(df):
    artists_streams = df.groupby("first_artist")["streams"].sum().reset_index()
    artists_streams = artists_streams.sort_values("streams", ascending=False).head(10)

    chart = alt.Chart(artists_streams).encode(
        alt.Theta("streams:Q").stack(True),
        alt.Color("first_artist:N", scale=alt.Scale(
            range=["#1db954", "#212121", "#535353", "#b3b3b3","#1db954", "#212121", "#535353", "#b3b3b3","#1db954", "#212121"],
        ),
            legend=alt.Legend(labelColor="White")  # Color blanco para las leyendas

        ).legend(None),
        tooltip=["first_artist:N", "streams:Q"]
    ).properties(
        title='Top 10 mas escuchado',

    )

    pie = chart.mark_arc(outerRadius=120)
    text = chart.mark_text(radius=143, size=13, fill="white").encode(text="first_artist")

    return pie + text

def Top_weeked(df):
    mas_semanas = df.groupby("first_artist")["weeks_on_chart"].sum().sort_values(ascending=False).reset_index()
    mas_semanas = mas_semanas.sort_values("weeks_on_chart", ascending=False).head(10)

    chart = alt.Chart(mas_semanas).encode(
        alt.Theta("weeks_on_chart:Q").stack(True),
        alt.Color("first_artist:N", scale=alt.Scale(
            range=["#1db954", "#212121", "#535353", "#b3b3b3","#1db954", "#212121", "#535353", "#b3b3b3","#1db954", "#212121"],
        ),
            legend=alt.Legend(labelColor="White")  # Color blanco para las leyendas

        ).legend(None),
        tooltip=["first_artist:N", "weeks_on_chart:Q"]
    ).properties(
        title='Top 10 con más semanas en el top',

    )

    pie = chart.mark_arc(outerRadius=120)
    text = chart.mark_text(radius=143, size=13, fill="white").encode(text="first_artist")

    return pie + text

def mas_escuchado(df):
    mas_escuchados = df.groupby("first_artist")["streams"].sum().sort_values(ascending=False).reset_index().iloc[0]
    primer_artista_nombre = mas_escuchados["first_artist"]
    primer_artista_streams = mas_escuchados["streams"]
    return primer_artista_nombre, primer_artista_streams

def mas_semanas(df):
    mas_semanas = df.groupby("first_artist")["weeks_on_chart"].sum().sort_values(ascending=False).reset_index().iloc[0]
    primer_artista_nombre = mas_semanas["first_artist"]
    primer_artista_weeks = mas_semanas["weeks_on_chart"]
    return primer_artista_nombre, primer_artista_weeks
