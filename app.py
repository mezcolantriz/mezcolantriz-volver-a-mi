import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Volver a mí", page_icon="🌼", layout="centered")

# Estilo CSS para darle un diseño más cálido
st.markdown("""
    <style>
        body {
            background-color: #fef8f5;
        }
        .stApp {
            background-image: linear-gradient(to bottom right, #fff6f0, #f3f7ff);
            color: #333333;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3 {
            color: #4e4b7a;
        }
        .stButton > button {
            background-color: #fbd7d7;
            color: #4e4b7a;
            border-radius: 10px;
        }
        .stTextInput input, .stTextArea textarea, .stSelectbox div {
            background-color: #fff;
            border: 1px solid #e6d8d8;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Título y bienvenida
st.title("🌼 Volver a mí")
st.markdown("""
    <div style='text-align: center; font-size: 20px; padding: 10px 20px;'>
        Bienvenida, <strong>Maria Antonieta</strong> 🌷<br>
        Este es tu espacio seguro para reconectar contigo misma, sanar poco a poco y caminar con dulzura hacia tu fortaleza interior.
    </div>
""", unsafe_allow_html=True)

# Menú lateral
menu = ["Ritual de mañana", "Diario emocional", "Carta de amor", "Ejercicio de presencia", "Check-in diario", "Retos"]
choice = st.sidebar.selectbox("✨ Elige tu práctica de hoy:", menu)

if choice == "Ritual de mañana":
    st.header("🧘‍♀️ Ritual de mañana")
    st.markdown("""
    - Coloca una mano en el pecho y otra en el abdomen.
    - Repite: **Este es mi cuerpo. Este es mi día. Hoy no necesito correr tras nada. Estoy conmigo.**
    - Respira profundo 3 veces (inhala 4, retén 4, exhala 6).
    """)
    if st.button("🌞 Hecho"):
        st.success("¡Muy bien! Hoy has elegido empezar contigo. Estoy orgullosa de ti 💛")

elif choice == "Diario emocional":
    st.header("📓 Diario emocional")
    st.markdown("Escribe con honestidad, este espacio es solo tuyo. 🪷")
    sentimiento = st.text_input("💭 ¿Qué sentiste hoy?")
    cuerpo = st.text_input("🌿 ¿Dónde lo sentiste en tu cuerpo?")
    orgullo = st.text_input("🌟 ¿Qué hiciste que te hizo sentir orgullosa?")
    if st.button("💌 Guardar entrada"):
        st.success("Entrada guardada 🌱. Estás cultivando conciencia y amor propio.")

elif choice == "Carta de amor":
    st.header("💌 Carta de amor a ti misma")
    st.markdown("Escribe una carta como si fueras tu mejor amiga. Trátate con ternura:")
    carta = st.text_area("Querida Maria Antonieta, ...", height=300)
    if st.button("💖 Guardar carta"):
        st.success("Carta guardada 💖. Puedes volver a leerla cuando lo necesites.")

elif choice == "Ejercicio de presencia":
    st.header("🌬️ Ejercicio de presencia - 5-4-3-2-1")
    st.markdown("""
    Cuando sientas ansiedad, haz este ejercicio para volver al presente:
    - 👀 **5 cosas que puedes ver**
    - ✋ **4 cosas que puedes tocar**
    - 👂 **3 cosas que puedes oír**
    - 👃 **2 cosas que puedes oler**
    - 💚 **1 cosa buena que hiciste hoy**
    """)
    if st.button("🕊️ Finalizar ejercicio"):
        st.success("Estás aquí, estás a salvo. Bien hecho ✨")

elif choice == "Check-in diario":
    st.header("🧠 Check-in diario")
    estado = st.selectbox("📌 ¿Cómo te sientes hoy?", ["Triste", "En calma", "Ansiosa", "Motivada", "Cansada", "Otra"])
    necesidad = st.selectbox("🪞 ¿Qué necesitas hoy?", ["Amor", "Descanso", "Motivación", "Silencio", "Contacto", "Otro"])
    if st.button("📔 Registrar check-in"):
        st.success(f"Has reconocido que te sientes {estado.lower()} y necesitas {necesidad.lower()}. Gracias por escucharte 🪷")

elif choice == "Retos":
    st.header("🌱 Microdesafíos de independencia")
    st.markdown("Hoy podrías intentar uno de estos retos valientes:")
    st.markdown("""
    - 💼 Enviar una propuesta para dar una clase
    - ☕ Ir a tomar un café sola sin el móvil
    - 🚫 Decir 'no' para priorizarte
    - 💻 Programar 15 minutos sin ayuda
    """)
    if st.button("🌟 Lo logré hoy"):
        st.success("¡Wow! Elegirte no es egoísmo. Estoy muy orgullosa de ti 💪")
