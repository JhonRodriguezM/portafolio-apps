from pathlib import Path

import streamlit as st
from PIL import Image

AQUI = Path(__file__).parent

st.set_page_config(page_title="Portafolio — Computación Avanzada", page_icon="🧠")

st.title("Portafolio de Computación Avanzada.")

with st.sidebar:
    st.subheader("Aplicaciones de portafolio — Jhon Alexander Rodríguez Montoya")
    parrafo = (
        "Las aplicaciones de esta página las desarrollé durante el semestre en el curso de "
        "Computación Avanzada de la I.U. Pascual Bravo. Cada una acompaña una sesión del curso: "
        "álgebra lineal, cálculo, complejidad, preparación de datos, regresión, series de tiempo, "
        "clasificación y PCA, desplegadas en Streamlit Cloud."
    )
    st.write(parrafo)

url_curso = "https://sites.google.com/view/computacinavanzada/inicio"
st.subheader("En el siguiente enlace puedes encontrar las sesiones y ejercicios del curso")
st.write(f"Página del curso: [Enlace]({url_curso})")

# Cada tarjeta: título, imagen (carpeta img/), descripción, texto del enlace y URL.
# Las URL que empiezan por "pages/" son páginas internas de este mismo portafolio.
APPS = [
    {
        "titulo": "Analizador de frutas",
        "imagen": "frutas.jpg",
        "texto": "Cada fruta es un vector (peso, diámetro, dulzor) y la distancia euclidiana "
                 "dice a cuál se parece más la fruta que ingresas. Incluye la pera.",
        "etiqueta": "Frutas",
        "url": "https://jhonrodriguez-frutas.streamlit.app/",
    },
    {
        "titulo": "Descenso de gradiente",
        "imagen": "gradiente.jpg",
        "texto": "El gradiente guía paso a paso hasta el mínimo de f(x, y) = (x − 3)² + (y + 2)²; "
                 "puedes ver el efecto de la tasa de aprendizaje y del punto inicial.",
        "etiqueta": "Gradiente",
        "url": "https://mipstr-48bnwbq5fvrhotgptsok2b.streamlit.app/",
    },
    {
        "titulo": "Detector de anomalías",
        "imagen": "anomalias.jpg",
        "texto": "Alarma con lógica proposicional (T > 30 ∧ H < 40 ∧ ¬ fin de semana), "
                 "notación Big-O y comparación de tiempos loop vs. NumPy.",
        "etiqueta": "Big-O",
        "url": "https://jhonrodriguez-anomalias.streamlit.app/",
    },
    {
        "titulo": "Preparación de datos",
        "imagen": "preparacion.jpg",
        "texto": "Tipos de datos, valores faltantes, outliers con IQR, normalización y "
                 "división train/val/test sobre lecturas de sensores IoT.",
        "etiqueta": "Datos",
        "url": "https://pa-modulo5-lvhxpwn7bazvpz6rkgkftr.streamlit.app/",
    },
    {
        "titulo": "Nivel del río — CORNARE",
        "imagen": "lluvia.jpg",
        "texto": "Datos reales de la estación 43 (San Francisco, río Santo Domingo) de la red "
                 "MARCO de CORNARE, con limpieza y un índice de calidad de datos.",
        "etiqueta": "CORNARE",
        "url": "https://lluvia-n6dhuriuxtbsup54vkgcbr.streamlit.app/",
    },
    {
        "titulo": "Regresión lineal",
        "imagen": "regresion.jpg",
        "texto": "Regresión simple y múltiple, función de costo, gradiente y métricas "
                 "R², MAE y RMSE con datos de vivienda de California.",
        "etiqueta": "Regresión",
        "url": "https://regresion-prog-avan-yanwwizkyhepbdtyn4ym2y.streamlit.app/",
    },
    {
        "titulo": "Series de tiempo",
        "imagen": "series.jpg",
        "texto": "Tendencia, estacionalidad, ACF/PACF y pronóstico con media móvil, "
                 "Holt-Winters, ARIMA y SARIMA para un sensor IoT simulado.",
        "etiqueta": "Series",
        "url": "https://jhonrodriguez-series-tiempo.streamlit.app/",
    },
    {
        "titulo": "Calidad del aire PM2.5 / PM10",
        "imagen": "aire.jpg",
        "texto": "Carga modelos entrenados con datos de CORNARE (estaciones 301 y 309) "
                 "y pronostica material particulado hacia adelante.",
        "etiqueta": "Aire",
        "url": "https://pronostico-p-a-8xvaefw3ao5iokovm2c4hd.streamlit.app/",
    },
    {
        "titulo": "Sensación térmica IoT",
        "imagen": "iot.jpg",
        "texto": "Lee temperatura y humedad de un ESP32 en InfluxDB, entrena una regresión "
                 "lineal y predice la sensación térmica.",
        "etiqueta": "IoT",
        "url": "https://iotthermalpredictionpipeline-ikvjxgzxcttxjfd6xrrag9.streamlit.app/",
    },
    {
        "titulo": "¿Lloverá mañana?",
        "imagen": "logistica.jpg",
        "texto": "Regresión logística que estima la probabilidad de lluvia a partir de "
                 "humedad, temperatura y viento, con umbral de decisión ajustable.",
        "etiqueta": "Logística",
        "url": "https://jhonrodriguez-logistica.streamlit.app/",
    },
    {
        "titulo": "KNN: ¿de qué grupo soy?",
        "imagen": "knn.jpg",
        "texto": "Clasificación por votación de vecinos: efecto de K, datos erróneos, "
                 "empates, frontera de decisión y un caso de lluvia.",
        "etiqueta": "KNN",
        "url": "pages/1_KNN_de_que_grupo_soy.py",
    },
    {
        "titulo": "Fertilidad de suelos con KNN",
        "imagen": "suelos.jpg",
        "texto": "KNN con datos reales de AGROSAVIA: escalado, elección de k, exactitud "
                 "vs. F1, matriz de confusión y fuga de datos.",
        "etiqueta": "Suelos",
        "url": "https://delatierraalalgoritmo-wvd8ar3alxnqq9n5thg5bw.streamlit.app/",
    },
    {
        "titulo": "Vectores propios y PCA",
        "imagen": "pca.jpg",
        "texto": "De la matriz al PCA: transformaciones lineales, valores y vectores propios, "
                 "covarianza y reducción de dimensiones.",
        "etiqueta": "PCA",
        "url": "pages/2_Vectores_propios_y_PCA.py",
    },
]

for inicio in range(0, len(APPS), 3):
    columnas = st.columns(3)
    for col, app in zip(columnas, APPS[inicio:inicio + 3]):
        with col:
            st.subheader(app["titulo"])
            imagen = AQUI / "img" / app["imagen"]
            if imagen.exists():
                st.image(Image.open(imagen), width=200)
            st.write(app["texto"])
            if app["url"].startswith("pages/"):
                st.page_link(app["url"], label=f"{app['etiqueta']}: abrir aquí", icon="➡️")
            elif app["url"]:
                st.write(f"{app['etiqueta']}: [Enlace]({app['url']})")
            else:
                st.caption("Enlace pendiente.")
