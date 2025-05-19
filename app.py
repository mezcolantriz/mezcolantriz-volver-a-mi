import streamlit as st
import random
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
import streamlit_js_eval   # Nuevo: componente para acceder a localStorage

# Configuración de la página
st.set_page_config(page_title="Volver a mí", page_icon="🌼", layout="centered")

# Estilo CSS aún más oscuro y con contraste mejorado
st.markdown("""
    <style>
        body {
            background-color: #1e1e2f;
        }
        .stApp {
            background-color: #1e1e2f;
            color: #f0f0f0;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, label, .css-1aumxhk, .css-1v0mbdj {
            color: #f9f9f9 !important;
        }
        .stButton > button {
            background-color: #4e4b7a !important;
            color: #ffffff !important;
            border-radius: 10px;
        }
        .stTextInput input, .stTextArea textarea, .stSelectbox div {
            background-color: #2b2b3d !important;
            color: #f0f0f0 !important;
            border: 1px solid #5e5b8a;
            border-radius: 10px;
        }
        .stAlert, .stInfo, .stSuccess, .stWarning {
            color: #f0f0f0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Nombre de usuario editable
nombre_input = st.text_input("¿Cómo te llamas?", value=st.session_state.get("nombre", "Maria Antonieta"))
if nombre_input:
    st.session_state.nombre = nombre_input
else:
    st.stop()

# Título y bienvenida
st.title("🌼 Volver a mí")
st.markdown(f"""
    <div style='text-align: center; font-size: 20px; padding: 10px 20px;'>
        Bienvenida, <strong>{st.session_state.nombre}</strong> 🌷<br>
        Este es tu espacio seguro para reconectar contigo misma, sanar poco a poco y caminar con dulzura hacia tu fortaleza interior.
    </div>
""", unsafe_allow_html=True)

# Menú lateral organizado por momentos del día
menu = {
    "🌅 Mañana": ["Ritual de mañana", "Check-in diario"],
    "🌤️ Mediodía": ["Ejercicio de presencia", "Retos"],
    "🌙 Noche": ["Diario emocional", "Carta de amor"],
    "📚 Historial y análisis": ["Mis registros", "Mis cartas de amor" ]
}

bloques = list(menu.keys())
bloque_actual = st.sidebar.selectbox("✨ Elige tu momento del día", bloques)
opcion = st.sidebar.selectbox("🔹 Elige tu espacio", menu[bloque_actual])
choice = opcion

# Sección: Diario emocional
if choice == "Diario emocional":
    st.header("📓 Diario emocional")
    st.markdown("Escribe con honestidad, este espacio es solo tuyo. 🪷")
    sentimiento = st.text_input("💭 ¿Qué sentiste hoy?")
    cuerpo = st.text_input("🌿 ¿Dónde lo sentiste en tu cuerpo?")
    orgullo = st.text_input("🌟 ¿Qué hiciste que te hizo sentir orgullosa?")
    if st.button("💌 Guardar entrada"):
        texto = f"Sentí: {sentimiento}\nLo sentí en: {cuerpo}\nOrgullo: {orgullo}"
        streamlit_js_eval.streamlit_js_eval(js=f"localStorage.setItem('diario', `{texto}`);", key="guardar_diario")
        os.makedirs("diario", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"diario/{timestamp}.txt", "w", encoding="utf-8") as f:
            f.write(texto)
        st.success("Entrada guardada localmente 🌱. Solo tú puedes verla desde este navegador.")
    if st.button("📂 Ver mi última entrada guardada"):
        diario_guardado = streamlit_js_eval.streamlit_js_eval(js="localStorage.getItem('diario');", key="ver_diario")
        if diario_guardado and isinstance(diario_guardado, str):
            st.info(f"📝 Última entrada guardada:\n\n{diario_guardado}")


# Sección: Check-in diario
elif choice == "Check-in diario":
    st.header("🧠 Check-in diario")
    estado = st.selectbox("📌 ¿Cómo te sientes hoy?", [
        "Triste", "En calma", "Ansiosa", "Motivada", "Cansada", "Frustrada", "Sola",
        "Agradecida", "Energética", "Vacía", "Confundida", "Segura", "Ilusionada",
        "Desconectada", "Serena", "Irritable", "En paz", "Emocionada", "Melancólica",
        "Otra"])
    if estado == "Otra":
        estado = st.text_input("Escríbelo con tus palabras:")
    necesidad = st.selectbox("🪞 ¿Qué necesitas hoy?", [
        "Amor", "Descanso", "Motivación", "Silencio", "Contacto", "Claridad", "Movimiento",
        "Autocompasión", "Inspiración", "Apoyo", "Libertad", "Llorar", "Ternura",
        "Espacio", "Alegría", "Rutina", "Cuidado físico", "Aceptar una emoción", "Otro"])
    if necesidad == "Otro":
        necesidad = st.text_input("Exprésalo tú misma:")
    if st.button("📔 Registrar check-in"):
        texto = f"Estado: {estado}\nNecesito: {necesidad}"
        streamlit_js_eval.streamlit_js_eval(js=f"localStorage.setItem('checkin', `{texto}`);", key="guardar_checkin")
        os.makedirs("checkin", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"checkin/{timestamp}.txt", "w", encoding="utf-8") as f:
            f.write(texto)
        st.success("Check-in guardado localmente 🌺. Solo tú puedes verlo desde este navegador.")
    if st.button("📂 Ver mi último check-in"):
        checkin_guardado = streamlit_js_eval.streamlit_js_eval(js="localStorage.getItem('checkin');", key="ver_checkin")
        if checkin_guardado and isinstance(checkin_guardado, str):
            st.info(f"🧠 Último check-in guardado:\n\n{checkin_guardado}")

# A partir de aquí, siguen las condiciones para ejecutar la sección correspondiente
elif choice == "Ritual de mañana":
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
    carta = st.text_area("Querida " + st.session_state.nombre + ", ...", height=300)
    if st.button("💖 Guardar carta"):
        if not os.path.exists("cartas"):
            os.mkdir("cartas")
        with open(f"cartas/{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", "w", encoding="utf-8") as f:
            f.write(carta)
        st.success("Carta guardada 💖. Puedes volver a leerla cuando lo necesites.")

# Sección: Mis cartas de amor
if choice == "Mis cartas de amor":
    st.header("📂 Mis cartas de amor")
    if os.path.exists("cartas"):
        cartas = sorted(os.listdir("cartas"), reverse=True)
        for c in cartas:
            with open(f"cartas/{c}", "r", encoding="utf-8") as f:
                contenido = f.read()
            st.markdown(f"""---
📅 **{c.replace('.txt','')}**

> {contenido}""")
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button(f"📝 Editar carta: {c}"):
                    nueva_carta = st.text_area("Edita tu carta:", value=contenido, key=f"editar_{c}")
                    if st.button(f"💾 Guardar cambios {c}", key=f"guardar_{c}"):
                        with open(f"cartas/{c}", "w", encoding="utf-8") as f:
                            f.write(nueva_carta)
                        st.success("Cambios guardados ✨")
            with col2:
                if st.button(f"🗑️ Borrar carta: {c}", key=f"borrar_{c}"):
                    os.remove(f"cartas/{c}")
                    st.warning("Carta eliminada 💔")
    else:
        st.info("Aún no has escrito ninguna carta. Ve al apartado 'Carta de amor a ti misma' 💌")


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


elif choice == "Retos":
    st.header("🌱 Microdesafíos de independencia")
    retos = [
        "Enviar una propuesta para dar una clase",
        "Ir a tomar un café sola sin el móvil",
        "Decir 'no' para priorizarte",
        "Programar 15 minutos sin ayuda",
        "Salir a caminar sin música ni móvil",
        "Escribir un poema para ti",
        "Hacer una lista de cosas que amas de ti",
        "Cocinarte algo con cariño",
        "Desconectarte de redes por 4 horas",
        "Mirarte al espejo y decirte 'te amo'",
        "Escribir tu meta del mes",
        "Bailar sola una canción alegre",
        "Ver una peli sin mirar el móvil",
        "Dormir temprano sin excusas",
        "Organizar tu escritorio o rincón favorito",
        "Escribir una carta de despedida a un miedo",
        "Practicar afirmaciones frente al espejo",
        "Tomarte una foto bonita solo para ti",
        "Elegir una frase poderosa y escribirla en grande",
        "Tener una cita contigo misma",
        "Leer 5 páginas de un libro solo por gusto",
        "Anotar 3 logros de la semana",
        "No explicar una decisión que te hace bien",
        "Escribir lo que quieres recibir en una relación",
        "Cantar en voz alta una canción que te empodere",
        "Llamar a alguien que te haga sentir bien",
        "No revisar el móvil antes de dormir",
        "Escribir tu historia como heroína",
        "Decirte algo bonito al despertar",
        "Regalarte flores o algo bonito",
        "Guardar silencio intencional 10 minutos",
        "Decidir no compararte hoy",
        "Comer sin distracciones ni culpa",
        "Pedir ayuda en algo que te cueste",
        "Escribir lo que aprendiste de una herida",
        "Poner límites a algo que te agota",
        "Celebrar un avance pequeño",
        "Decir lo que sientes sin disculparte",
        "Hacer algo que postergabas",
        "Escribir tu versión más libre y feliz",
        "Intenta componer una canción",
        "Aprende una canción con la guitarra o el piano"
    ]
    seleccionados = random.sample(retos, 4)
    if st.button("🎯 Dame mini retos"):
        st.markdown("Hoy podrías intentar uno de estos retos valientes:")
        for r in seleccionados:
            st.markdown(f"- 🌟 {r}")
    if st.button("💪 Lo logré hoy"):
        st.success("¡Wow! Elegirte no es egoísmo. Estoy muy orgullosa de ti 💪")
elif choice == "Mis registros":
    st.header("📖 Mis registros")

    st.subheader("📓 Diario emocional")
    if os.path.exists("diario"):
        diario = sorted(os.listdir("diario"), reverse=True)
        for d in diario:
            with open(f"diario/{d}", "r", encoding="utf-8") as f:
                st.markdown(f"""---\n🗓️ **{d.replace('.txt','')}**\n
{f.read()}""")
    else:
        st.info("Aún no hay entradas en tu diario emocional ✍️")

    st.subheader("🧠 Check-ins diarios")
    estados = []
    necesidades = []
    if os.path.exists("checkin"):
        checks = sorted(os.listdir("checkin"), reverse=True)
        for c in checks:
            with open(f"checkin/{c}", "r", encoding="utf-8") as f:
                contenido = f.read()
                st.markdown(f"""---\n📅 **{c.replace('.txt','')}**\n
{contenido}""")
                for linea in contenido.splitlines():
                    if "Estado" in linea:
                        estados.append(linea.split(": ")[1].strip())
                    elif "Necesito" in linea:
                        necesidades.append(linea.split(": ")[1].strip())

        st.subheader("📊 Análisis emocional")
        if estados:
            estado_count = Counter(estados)
            fig, ax = plt.subplots()
            ax.bar(estado_count.keys(), estado_count.values(), color="#fbd7d7")
            ax.set_title("Estados emocionales más frecuentes")
            ax.set_ylabel("Frecuencia")
            ax.set_facecolor("#1e1e2f")
            fig.patch.set_facecolor('#1e1e2f')
            ax.tick_params(colors='#f0f0f0')
            ax.title.set_color('#f0f0f0')
            ax.yaxis.label.set_color('#f0f0f0')
            st.pyplot(fig)

        if necesidades:
            necesidad_count = Counter(necesidades)
            fig2, ax2 = plt.subplots()
            ax2.pie(necesidad_count.values(), labels=necesidad_count.keys(), autopct="%1.1f%%", colors=plt.cm.Pastel1.colors)
            ax2.set_title("¿Qué necesitas más a menudo?")
            fig2.patch.set_facecolor('#1e1e2f')
            ax2.title.set_color('#f0f0f0')
            st.pyplot(fig2)
    else:
        st.info("Aún no hay check-ins guardados 🕊️")

    st.subheader("🧹 Reiniciar registros")
    opcion_borrar = st.selectbox("¿Qué deseas borrar?", ["Nada", "Solo diario emocional", "Solo check-ins", "Solo cartas", "Todo"])
    if st.button("🗑️ Borrar selección"):
        import shutil
        if opcion_borrar == "Solo diario emocional" and os.path.exists("diario"):
            for archivo in os.listdir("diario"):
                os.remove(os.path.join("diario", archivo))
            st.warning("Entradas del diario eliminadas ✏️")
        elif opcion_borrar == "Solo check-ins" and os.path.exists("checkin"):
            for archivo in os.listdir("checkin"):
                os.remove(os.path.join("checkin", archivo))
            st.warning("Check-ins eliminados 📌")
        elif opcion_borrar == "Solo cartas" and os.path.exists("cartas"):
            for archivo in os.listdir("cartas"):
                os.remove(os.path.join("cartas", archivo))
            st.warning("Cartas eliminadas 💌")
        elif opcion_borrar == "Todo":
            for carpeta in ["diario", "checkin", "cartas"]:
                if os.path.exists(carpeta):
                    shutil.rmtree(carpeta)
            st.error("Todo ha sido eliminado 💣")

