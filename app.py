import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Seiten-Konfiguration
st.set_page_config(page_title="Tennis C-Trainer Interaktiv-Lab", page_icon="🎾", layout="wide")

# Session State für Verzweigungen & Pfade
if "stage" not in st.session_state:
    st.session_state.stage = "start"
if "group_mood" not in st.session_state:
    st.session_state.group_mood = 100  # Trainings-Motivation der Gruppe (0-100%)

st.title("🎾 C-Trainer Praxis-Lab: Interaktive Simulation")
st.markdown("Dieses Tool simuliert praxisnahe Szenarien aus der C-Trainer-Ausbildung.")

st.divider()

# ------------------------------------------------------------------
# ZEICHEN-FUNKTION FÜR DEN ECHTEN TENNISPLATZ
# ------------------------------------------------------------------
def draw_court(trainer_pos, queue_pos):
    fig, ax = plt.subplots(figsize=(6, 8))
    
    # 1. Sandplatz-Hintergrund (BTV-Rot) & Auslaufbereich (Grün)
    ax.set_facecolor("#2E8B57") # Grüner Umfeld-Bereich
    court_bg = patches.Rectangle((0, 0), 10.97, 23.77, linewidth=0, edgecolor='none', facecolor='#D2691E') # Sandplatz
    ax.add_patch(court_bg)
    
    # 2. Spielfeldlinien (Weiß)
    margin = (10.97 - 8.23) / 2 # 1.37m Doppelkorridor
    
    # Außenfeld (Doppel) & Einzel-Seitenlinien
    ax.plot([0, 10.97, 10.97, 0, 0], [0, 0, 23.77, 23.77, 0], color="white", lw=2)
    ax.plot([margin, margin], [0, 23.77], color="white", lw=1.5)
    ax.plot([10.97 - margin, 10.97 - margin], [0, 23.77], color="white", lw=1.5)
    
    # Netz (Mitte bei 11.885m)
    net_y = 23.77 / 2
    ax.plot([-0.5, 11.47], [net_y, net_y], color="black", lw=4, zorder=3)
    ax.plot([-0.5, 11.47], [net_y, net_y], color="white", lw=1.5, ls="--", zorder=4)
    
    # T-Linien (6.40m vom Netz) & Mittellinie
    t_bottom = net_y - 6.40
    t_top = net_y + 6.40
    ax.plot([margin, 10.97 - margin], [t_bottom, t_bottom], color="white", lw=1.5)
    ax.plot([margin, 10.97 - margin], [t_top, t_top], color="white", lw=1.5)
    ax.plot([10.97/2, 10.97/2], [t_bottom, t_top], color="white", lw=1.5)
    
    # 3. Positionen der Personen berechnen
    if "Netz" in trainer_pos:
        tx, ty = 10.97/2, net_y - 1.5
    elif "T-Linie" in trainer_pos:
        tx, ty = 10.97/2, t_bottom
    else: # Grundlinie
        tx, ty = 10.97/2, 1.0

    if "Netzkante" in queue_pos:
        qx, qy = margin - 0.8, net_y - 2.0
    elif "Schläger" in queue_pos:
        qx, qy = tx + 1.2, ty
    else: # Bank
        qx, qy = -1.5, net_y

    # 4. Marker einzeichnen
    ax.scatter([tx], [ty], color="yellow", edgecolor="black", s=250, zorder=6, label="Trainer (Korb)")
    ax.scatter([qx, qx + 0.6], [qy, qy], color="red", edgecolor="black", s=180, zorder=6, label="Wartende Schüler")
    
    # Achsen & Ränder einstellen
    ax.set_xlim(-2.5, 13.5)
    ax.set_ylim(-2, 26)
    ax.set_aspect('equal')
    ax.legend(loc="upper right", framealpha=0.9, fontsize="small")
    ax.axis("off")
    
    return fig


# ------------------------------------------------------------------
# WERKZEUG 1: VISUELLES ORGANISATIONS-LABORATORIUM
# ------------------------------------------------------------------
st.header("1. Visuelles Platz-Setup & Gruppenorganisation")
st.caption("Positioniere deinen Ballkorb und die Wartezone für die Schüler im Kleinfeld/Mid-Court.")

col1, col2 = st.columns([1, 1])

with col1:
    trainer_pos = st.selectbox(
        "Position des Trainers (Korb):", 
        ["Am Netz (Mitte)", "Auf der T-Linie", "An der Grundlinie"], 
        index=0
    )
    queue_pos = st.selectbox(
        "Wartezone der Schüler:", 
        ["Seitlich an der Netzkante mit Zusatzaufgabe", "Direkt hinter dem Schläger", "Auf der Bank"], 
        index=0
    )
    feed_type = st.radio(
        "Zuspielform:", 
        ["Zuwurf von unten ('weg vom Schüler')", "Harter Schlag von der Grundlinie"], 
        index=0
    )

with col2:
    fig = draw_court(trainer_pos, queue_pos)
    st.pyplot(fig, use_container_width=True)

# Methodische Auswertung des Setups
if "Netzkante" in queue_pos and "weg vom Schüler" in feed_type:
    st.success("✅ Hervorragend! Minimale Wartezeiten, hohe Intensität und die richtige Zuwurfrichtung zur Bewegungskopplung[cite: 1, 3].")
else:
    st.warning("⚠️ Vorsicht: Achte auf Sicherheitsabstände, Bewegungskopplung und die Vermeidung langer Schlangen[cite: 1, 3]!")

st.divider()

# ------------------------------------------------------------------
# WERKZEUG 2: DYNAMISCHE BIOMECHANIK-ZEITLEISTE (Vorhand-Drive)
# ------------------------------------------------------------------
st.header("2. Biomechanik-Stop-Motion Analysis")
st.caption("Bewege den Slider, um die Vorhand-Bewegung zu analysieren. Stoppe exakt an der **Hauptaktion**!")

frame = st.slider("Bewegungsphase (Frames 0 - 100):", 0, 100, 10)

if frame < 30:
    st.info("🔄 **Ausholphase (Hilfsaktion):** Oberkörperrotation, Gewichtsverlagerung nach hinten[cite: 5].")
elif 30 <= frame <= 65:
    st.warning("⚡ **Hauptaktion:** Schlagphase ab ca. 30–40 cm vor dem Treffpunkt bis zum Treffpunkt![cite: 5]")
    st.markdown("🎯 *Prüfkriterium:* Steht die Schlägerfläche im Treffpunkt im richtigen Winkel zum Ball[cite: 5]?")
else:
    st.info("↩️ **Ausschwungphase (Hilfsaktion):** Ausschwung über die Schulter, Ausschwingen des Körpers[cite: 5].")

st.divider()

# ------------------------------------------------------------------
# WERKZEUG 3: INTERAKTIVES BRANCHING-SZENARIO
# ------------------------------------------------------------------
st.header("3. Live-Entscheidungsszenario im Gruppentraining")
st.caption("Reagiere auf das Verhalten deiner Trainingsgruppe im Mid-Court.")

st.metric("Gruppen-Motivation & Disziplin", f"{st.session_state.group_mood}%")

if st.session_state.stage == "start":
    st.markdown("**Szenario:** Du führst die Übungsform *'Vorhand cross / Rückhand longline'* im Mid-Court durch[cite: 3]. Ein Schüler trifft den Ball ständig im Rücken und verliert die Lust.")
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
    st.error("❌ Die Korrektur des Ausschwungs hilft nicht! Der Fehler liegt in der Hauptaktion (Treffpunkt)[cite: 4, 5]. Der Schüler trifft weiterhin zu spät. Die Stimmung sinkt.")
    if st.button("Zurück und Methodik überdenken"):
        st.session_state.stage = "start"
        st.rerun()

elif st.session_state.stage == "path_b":
    st.success("🎯 Richtig! Durch das Anpassen des Zuspielwinkels ('weg vom Schüler') trifft er den Ball wieder 30–40 cm vor dem Körper[cite: 1, 5]. Die Ballwechsel klappen wieder!")
    if st.button("Nächste Trainingsphase starten"):
        st.session_state.stage = "start"
        st.session_state.group_mood = 100
        st.rerun()
