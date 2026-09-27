import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(page_title="Tennis C-Trainer Interaktiv-Lab", page_icon="🎾", layout="wide")

# Session State für Verzweigungen & Pfade
if "stage" not in st.session_state:
    st.session_state.stage = "start"
if "group_mood" not in st.session_state:
    st.session_state.group_mood = 100  # Trainings-Motivation der Gruppe (0-100%)

st.title("🎾 C-Trainer Praxis-Lab: Interaktive Simulation")

# ------------------------------------------------------------------
# WERKZEUG 1: VISUELLER ORGANISATIONS-LABORATORIUM (Mid-Court Aufbauten)
# ------------------------------------------------------------------
st.header("1. Visuelles Platz-Setup & Gruppenorganisation")
st.caption("Positioniere deinen Ballkorb (K) und die Wartezone für die Schüler im Kleinfeld/Mid-Court.")

col1, col2 = st.columns([1, 1])

with col1:
    trainer_pos = st.selectbox("Position des Trainers (Korb):", ["Am Netz (Mitte)", "Auf der T-Linie", "An der Grundlinie"], index=0)
    queue_pos = st.selectbox("Wartezone der Schüler:", ["Direkt hinter dem Schläger", "Seitlich an der Netzkante mit Zusatzaufgabe", "Auf der Bank"], index=1)
    feed_type = st.radio("Zuspielform:", ["Zuwurf von unten ('weg vom Schüler')", "Harter Schlag von der Grundlinie"], index=0)

with col2:
    # Dynamische Generierung des Tennisplatzes basierend auf Trainer-Auswahl
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_facecolor("#4CAF50") # Grüner Platz
    # Platzlinien
    plt.plot([0, 0, 10, 10, 0], [0, 20, 20, 0, 0], color="white", lw=2) # Außenlinie
    plt.plot([0, 10], [10, 10], color="white", lw=3) # Netz
    plt.plot([0, 10], [5, 5], color="white", lw=1.5) # T-Linie unten
    plt.plot([0, 10], [15, 15], color="white", lw=1.5) # T-Linie oben
    
    # Visualisierung der Trainer- und Schülerposition
    t_y = 10 if "Netz" in trainer_pos else (5 if "T-Linie" in trainer_pos else 1)
    ax.scatter([5], [t_y], color="yellow", s=200, zorder=5, label="Trainer (Korb)")
    
    q_y = 12 if "Netzkante" in queue_pos else (2 if "Schläger" in queue_pos else 0)
    ax.scatter([2, 2.5], [q_y, q_y], color="red", s=150, zorder=5, label="Wartende Schüler")
    
    plt.xlim(-1, 11)
    plt.ylim(-1, 21)
    plt.axis("off")
    plt.legend(loc="upper right", fontsize="small")
    st.pyplot(fig)

# Auswertung des Visuellen Setups
if "Netzkante" in queue_pos and "weg vom Schüler" in feed_type:
    st.success("✅ Hervorragend! Minimale Wartezeiten, hohe Intensität und die richtige Zuwurfrichtung zur Bewegungskopplung.")
else:
    st.warning("⚠️ Vorsicht: Achte auf die Sicherheitsabstände und Vermeidung von langen Schlangen!")

st.divider()

# ------------------------------------------------------------------
# WERKZEUG 2: DYNAMISCHE BIOMECHANIK-ZEITLEISTE (Vorhand-Drive)
# ------------------------------------------------------------------
st.header("2. Biomechanik-Stop-Motion Analysis")
st.caption("Bewege den Slider, um die Vorhand-Bewegung zu analysieren. Stoppe exakt an der **Hauptaktion**!")

frame = st.slider("Bewegungsphase (Frames 0 - 100):", 0, 100, 10)

# Visuelle Rückmeldung je nach Frame-Bereich (Simulierte Videosequenz)
if frame < 30:
    st.info("🔄 **Ausholphase (Hilfsaktion):** Oberkörperrotation, Gewichtsverlagerung nach hinten.")
elif 30 <= frame <= 65:
    st.warning("⚡ **Hauptaktion:** Schlagphase ab ca. 30–40 cm vor dem Treffpunkt bis zum Treffpunkt!")
    st.markdown("🎯 *Prüfkriterium:* Steht die Schlägerfläche im Treffpunkt im richtigen Winkel zum Ball?")
else:
    st.info("↩️ **Ausschwungphase (Hilfsaktion):** Ausschwung über die Schulter, Ausschwingen des Körpers.")

st.divider()

# ------------------------------------------------------------------
# WERKZEUG 3: INTERAKTIVES BRANCHING-SZENARIO (Verzweigte Simulation)
# ------------------------------------------------------------------
st.header("3. Live-Entscheidungsszenario im Gruppentraining")
st.caption("Reagiere auf das Verhalten deiner Trainingsgruppe im Mid-Court.")

st.metric("Gruppen-Motivation & Disziplin", f"{st.session_state.group_mood}%")

if st.session_state.stage == "start":
    st.markdown("**Szenario:** Du führst die Übungsform *'Vorhand cross / Rückhand longline'* im Mid-Court durch. Ein Schüler trifft den Ball ständig im Rücken und verliert die Lust.")
    col_a, col_b = st.columns(2)
    if col_a.button("Option A: Ich korrigiere den Ausschwung über die Schulter."):
        st.session_state.group_mood -= 20
        st.session_state.stage = "path_a"
        st.rerun()
    if col_b.button("Option B: Ich passe die Zuspieldistanz an & korrigiere den Treffpunkt (Hauptaktion)."):
        st.session_state.group_mood += 10
        st.session_state.stage = "path_b"
        st.rerun()

elif st.session_state.stage == "path_a":
    st.error("❌ Die Korrektur des Ausschwungs hilft nicht! Der Schüler trifft den Ball weiterhin zu spät. Die Stimmung sinkt.")
    if st.button("Zurück und Methodik überdenken"):
        st.session_state.stage = "start"
        st.rerun()

elif st.session_state.stage == "path_b":
    st.success("🎯 Richtig! Durch das Anpassen des Zuspielwinkels ('weg vom Schüler') trifft er den Ball wieder 30–40 cm vor dem Körper. Die Ballwechsel klappen wieder!")
    if st.button("Nächste Trainingsphase starten"):
        st.session_state.stage = "start"
        st.session_state.group_mood = 100
        st.rerun()
