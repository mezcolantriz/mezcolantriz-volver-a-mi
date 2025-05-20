import streamlit as st
import random
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
import streamlit_js_eval  # acceso a localStorage

# Configuración de la página
st.set_page_config(page_title="Volver a mí", page_icon="🌼", layout="centered")

# Estilo CSS
st.markdown("""
<style>
    body { background-color: #1e1e2f; }
    .stApp { background-color: #1e1e2f; color: #f0f0f0; font-family: 'Segoe UI', sans-serif; }
    h1, h2, h3, label, .css-1aumxhk, .css-1v0mbdj { color: #f9f9f9 !important; }
    .stButton > button { background-color: #4e4b7a !important; color: #ffffff !important; border-radius: 10px; }
    .stTextInput input, .stTextArea textarea, .stSelectbox div { background-color: #2b2b3d !important; color: #f0f0f0 !important; border: 1px solid #5e5b8a; border-radius: 10px; }
    .stAlert, .stInfo, .stSuccess, .stWarning { color: #f0f0f0 !important; }
</style>
""", unsafe_allow_html=True)

# Nombre editable
title = st.text_input("¿Cómo te llamas?", value=st.session_state.get("nombre", "Maria Antonieta"))
if not title:
    st.stop()
st.session_state.nombre = title

# Bienvenida
st.title("🌼 Volver a mí")
st.markdown(f"""
<div style='text-align:center; font-size:20px; padding:10px;'>
Bienvenida, <strong>{title}</strong> 🌷<br>
Tu espacio seguro para reconectar contigo misma.
</div>
""", unsafe_allow_html=True)

# Menú lateral
menu = {
    "🌅 Mañana": ["Ritual de mañana", "Check-in diario"],
    "🌤️ Mediodía": ["Ejercicio de presencia", "Retos"],
    "🌙 Noche": ["Diario emocional", "Carta de amor"],
    "⚡ Crisis emocional": ["Ejercicio de crisis"],
    "📚 Historial y análisis": ["Mis registros", "Mis cartas de amor"]
}

bloques = list(menu.keys())
bloque = st.sidebar.selectbox("Elige tu momento:", bloques)
opcion = st.sidebar.selectbox("Seleccione una sección:", menu[bloque])
choice = opcion

# -----------------
# Sección: Crisis emocional
# -----------------
def crisis_app():
    st.header("⚡ Crisis emocional")
    exercises = [
        {"title": "Carta que no enviarás", "description": "Escribe todo lo que quisieras decirle en un texto. Luego decide si guardarla o soltarla.", "ui": "text_area"},
        {"title": "Modo avión emocional", "description": "Bloquea pensamientos impulsivos durante 5 minutos. Pulsa el botón:", "ui": "button", "button_label": "Activar Modo Avión"},
        {"title": "Yo del futuro", "description": "Escribe un mensaje desde tu Yo del futuro, dándote ánimo y perspectiva.", "ui": "text_area"},
        {"title": "Caja sensorial (5-4-3-2-1)", "description": "5 cosas que ves, 4 que tocas, 3 que oyes, 2 que hueles, 1 pensamiento amable.", "ui": "text_area"},
        {"title": "Diálogo compasivo", "description": "Escribe lo que le dirías a una amiga y luego respóndete con compasión.", "ui": "text_area"},
        {"title": "Mantra de contención", "description": "Repite en voz alta: 'Esto también pasará'. Pulsa el botón:", "ui": "button", "button_label": "Recitar Mantra"},
        {"title": "Dibuja tu tormenta", "description": "Toma papel o usa tu mente para dibujar tu emoción y luego tu calma.", "ui": "text_area"},
        {"title": "No lo haré hoy", "description": "Reafirma que no actuarás impulsivamente hoy. Pulsa:", "ui": "button", "button_label": "Aceptar"},
        {"title": "Semáforo emocional", "description": "Selecciona: Rojo (no actúo), Amarillo (respiro), Verde (actúo con calma).", "ui": "select", "options": ["Rojo", "Amarillo", "Verde"]},
        {"title": "Lista de gratitud", "description": "Escribe 3 cosas pequeñas por las que te sientes agradecida.", "ui": "text_area"},
        {"title": "Memoria refugio", "description": "Recuerda y describe un momento feliz que te sirva de refugio.", "ui": "text_area"},
        {"title": "Piedra en el bolsillo", "description": "Toca un objeto y repite: 'Estoy a salvo, esto pasará'. Pulsa:", "ui": "button", "button_label": "Hecho"},
        {"title": "Puente de sensaciones", "description": "Enumera 5 sentidos y escribe una palabra para cada uno.", "ui": "text_area"},
        {"title": "Afirmaciones de fuerza", "description": "Escoge o escribe 2 afirmaciones que te empoderen.", "ui": "text_area"},
        {"title": "Cambio de perspectiva","description": "Imagina que esta situación le está pasando a una amiga. ¿Qué le dirías? ¿Cambiaría tu visión de lo que está ocurriendo?", "ui": "text_area"},
        {"title": "Respiro de 3 minutos","description": "Concéntrate en tu respiración. Inspira 4, retén 4, exhala 6. Hazlo 3 veces. Pulsa el botón al terminar:", "ui": "button", "button_label": "Terminado"},
        {"title": "Lista de lo que no necesitas","description": "Haz una lista de cosas que no necesitas ahora (como aprobación, respuestas, certezas).","ui": "text_area"},
        {"title": "Checklist de realidad","description": "Anota 3 cosas que sabes con certeza ahora. No lo que temes, sino lo que es real.","ui": "text_area"},
        {"title": "Llamada interna","description": "Imagina que te llamas a ti misma por teléfono. ¿Qué tono usarías? ¿Qué necesitas escuchar?","ui": "text_area"},
        {"title": "Canción de refugio","description": "Piensa o escribe el nombre de una canción que te haya acompañado antes. Déjala sonar dentro de ti.","ui": "text_area"}
        ]
    ex = random.choice(exercises)
    st.subheader(ex["title"])
    st.write(ex["description"])
    if ex["ui"] == "text_area":
        st.text_area("", key="crisis_input")
    elif ex["ui"] == "button":
        if st.button(ex.get("button_label", "Ejecutar")):
            st.success("¡Ejercicio completado! 🙏")
    elif ex["ui"] == "select":
        sel = st.selectbox("Elige:", ex.get("options", []))
        st.write(f"Has seleccionado: {sel}")
    if st.button("Otro ejercicio"): st.rerun()
()

if choice == "Ejercicio de crisis":
    crisis_app()

# -----------------
# Sección: Ritual de mañana
# -----------------
elif choice == "Ritual de mañana":
    st.header("🧘‍♀️ Ritual de mañana")
    st.markdown(
        "- Coloca una mano en el pecho y otra en el abdomen.\n"
        "- Repite: **Este es mi cuerpo. Este es mi día...**\n"
        "- Respira 3 veces (4-4-6)."
    )
    if st.button("🌞 Hecho"): st.success("¡Buen comienzo! 💛")

# -----------------
# Sección: Check-in diario
# -----------------
elif choice == "Check-in diario":
    st.header("🧠 Check-in diario")
    estado = st.selectbox("📌 ¿Cómo te sientes hoy?", [
        "Triste", "En calma", "Ansiosa", "Motivada", "Cansada", "Frustrada",
        "Sola", "Agradecida", "Energética", "Confundida", "Serena", "Emocionada",
        "Otra"
    ])
    if estado == "Otra":
        estado = st.text_input("Escríbelo:")
    necesidad = st.selectbox("🪞 ¿Qué necesitas hoy?", [
        "Amor", "Descanso", "Motivación", "Silencio", "Contacto", "Claridad",
        "Autocompasión", "Apoyo", "Rutina", "Otro"
    ])
    if necesidad == "Otro":
        necesidad = st.text_input("Exprésalo:")
    if st.button("📔 Registrar check-in"):
        text = f"Estado: {estado}\nNecesito: {necesidad}"
        os.makedirs("checkin", exist_ok=True)
        dt = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"checkin/{dt}.txt","w",encoding="utf-8") as f: f.write(text)
        st.success("Check-in guardado 🌺")

# -----------------
# Sección: Diario emocional
# -----------------
elif choice == "Diario emocional":
    st.header("📓 Diario emocional")
    senti = st.text_input("💭 ¿Qué sentiste hoy?")
    cuerpo = st.text_input("🌿 ¿Dónde lo sentiste en tu cuerpo?")
    orgullo = st.text_input("🌟 ¿Qué te hace sentir orgullosa?")
    if st.button("💌 Guardar entrada"):
        txt = f"Sentí: {senti}\nEn: {cuerpo}\nOrgullo: {orgullo}"
        os.makedirs("diario", exist_ok=True)
        tm = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"diario/{tm}.txt","w",encoding="utf-8") as f: f.write(txt)
        st.success("Entrada guardada 🌱")

# -----------------
# Sección: Carta de amor
# -----------------
elif choice == "Carta de amor":
    st.header("💌 Carta de amor a ti misma")
    carta = st.text_area("Escríbela:", height=250)
    if st.button("💖 Guardar carta"):
        os.makedirs("cartas",exist_ok=True)
        fn = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"cartas/{fn}.txt","w",encoding="utf-8") as f: f.write(carta)
        st.success("Carta guardada 💖")

# -----------------
# Sección: Mis cartas de amor
# -----------------
elif choice == "Mis cartas de amor":
    st.header("📂 Mis cartas de amor")
    if os.path.exists("cartas"):
        for c in sorted(os.listdir("cartas"),reverse=True):
            with open(f"cartas/{c}","r",encoding="utf-8") as f: cont=f.read()
            st.markdown(f"---\n📅 **{c.replace('.txt','')}**\n> {cont}")
            col1,col2=st.columns(2)
            with col1:
                if st.button(f"📝 Editar {c}",key=f"edit_{c}"):
                    edit=st.text_area("Edita:",value=cont,key=f"area_{c}")
                    if st.button(f"💾 Guarda {c}",key=f"save_{c}"):
                        with open(f"cartas/{c}","w",encoding="utf-8") as fx: fx.write(edit)
                        st.success("Carta actualizada✨")
            with col2:
                if st.button(f"🗑️ Borrar {c}",key=f"del_{c}"):
                    os.remove(f"cartas/{c}")
                    st.warning("Carta eliminada💔")
    else:
        st.info("No hay cartas. Ve a 'Carta de amor'.")

# -----------------
# Sección: Retos y Ejercicio de presencia
# -----------------
elif choice == "Ejercicio de presencia":
    st.header("🌬️ 5-4-3-2-1")
    st.markdown("5 cosas que ves... 4 que tocas... etc.")
    if st.button("🕊️ Hecho"): st.success("Estás aquí y a salvo✨")
elif choice == "Retos":
    st.header("🌱 Microretos")
    retos=["Ir a un café sola","Escribir un poema","Salir sin móvil","Decir no"]
    if st.button("🎯 Nuevo reto"):
        st.info(random.choice(retos))

# -----------------
# Sección: Mis registros
# -----------------
elif choice == "Mis registros":
    st.header("📖 Mis registros")
    # Diario
    st.subheader("Diario emocional")
    if os.path.exists("diario"):
        for d in sorted(os.listdir("diario"),reverse=True):
            with open(f"diario/{d}","r") as f: st.write(f"{d}: {f.read()}")
    else: st.info("Sin entradas.")
    # Check-in
    st.subheader("Check-ins")
    if os.path.exists("checkin"):
        for c in sorted(os.listdir("checkin"),reverse=True):
            with open(f"checkin/{c}","r") as f: st.write(f"{c}: {f.read()}")
    else: st.info("Sin check-ins.")
    # Gráficas
    estados=[]; necesidades=[]
    if os.path.exists("checkin"):
        for c in os.listdir("checkin"):
            for l in open(f"checkin/{c}"): 
                if "Estado" in l: estados.append(l.split(": ")[1].strip())
                if "Necesito" in l: necesidades.append(l.split(": ")[1].strip())
        if estados:
            fig,ax=plt.subplots(); ax.bar(*zip(*Counter(estados).items())); st.pyplot(fig)
        if necesidades:
            fig2,ax2=plt.subplots(); ax2.pie(Counter(necesidades).values(),labels=Counter(necesidades).keys(),autopct="%1.1f%%"); st.pyplot(fig2)
    # Reiniciar
    st.subheader("🧹 Reiniciar registros")
    opt=st.selectbox("Borrar:",["Nada","Diario","Check-ins","Cartas","Todo"])
    if st.button("🗑️ Borrar selección"):
        import shutil
        mapping={"Diario":"diario","Check-ins":"checkin","Cartas":"cartas"}
        if opt in mapping and os.path.exists(mapping[opt]): shutil.rmtree(mapping[opt])
        if opt=="Todo": shutil.rmtree("diario",ignore_errors=True);shutil.rmtree("checkin",ignore_errors=True);shutil.rmtree("cartas",ignore_errors=True)
        st.warning(f"Borrado: {opt}")
