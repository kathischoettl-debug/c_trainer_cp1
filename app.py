import streamlit as st

# Seiten-Konfiguration
st.set_page_config(
    page_title="Tennis C-Trainer Prüfungssimulator",
    page_icon="🎾",
    layout="wide"
)

# Initialisierung des Session-States für Punkte & Fortschritt
if "score" not in st.session_state:
    st.session_state.score = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

st.title("🎾 C-Trainer Anwärter: Interactive Praxis-Simulation")
st.markdown("""
Willkommen zur digitalen Vorbereitung auf die C-Trainer-Praxisprüfung!
Gehe die folgenden Unterrichtsszenarien durch, analysiere die Situationen und wähle die methodisch korrekte Trainer-Handlung aus.
""")

st.divider()

# TAB-NAVIGATION FÜR DIE DREI MODULE
tab1, tab2, tab3, tab_eval = st.tabs([
    "1️⃣ Zuspiel & Zuwurf", 
    "2️⃣ Biomechanik & Technik", 
    "3️⃣ Organisation & Spielformen", 
    "📊 Auswertung"
])

# ---------------------------------------------------------
# MODUL 1: ZUSPIEL & ZUWURF
# ---------------------------------------------------------
with tab1:
    st.header("Modul 1: Zuwurf- & Zuspielkompetenz")
    st.info("Szenario: Du stehst am Korb und spielst Bälle für Anfänger im Kleinfeld/Mid-Court ein.")
    
    st.subheader("Frage 1.1: Zuwurf-Rhythmus")
    q1 = st.radio(
        "Ein Schüler hat Schwierigkeiten mit dem Treffpunkt beim Vorhand-Drive. Wie greifst und wirfst du die Bälle korrekt an?",
        options=[
            "A) Ich greife immer 5 Bälle auf einmal und werfe sie schnell hintereinander ohne Blickkontakt.",
            "B) Ich halte freien Blick zum Schüler, nutze die Auftaktbewegung, greife taktgemäß 2 Bälle nach der VH und werfe 'weg vom Schüler' an.",
            "C) Ich spiele alle Bälle ausschließlich mit maximalem Oberschnitt direkt mit dem Schläger von der Grundlinie ein."
        ],
        key="m1_q1"
    )
    
    st.subheader("Frage 1.2: Positionierung beim Zuspiel")
    q2 = st.radio(
        "Aus welcher Distanz und mit welcher Schlägerfläche wird ein kontrolliertes Einspielen für Anfänger im Kleinfeld empfohlen?",
        options=[
            "A) Aus großer Distanz mit geschlossener Schlägerfläche und hohem Tempo.",
            "B) Aus geringer/mittlerer Distanz (z. B. 3–5m) mit leicht geöffneter Schlägerfläche für flache, kontrollierte Flugkurven.",
            "C) Direkt über dem Netz mit Volley-Stop."
        ],
        key="m1_q2"
    )

# ---------------------------------------------------------
# MODUL 2: BIOMECHANIK & TECHNIKANALYSE
# ---------------------------------------------------------
with tab2:
    st.header("Modul 2: Biomechanik & Technikanalyse (Vorhand-Drive)")
    st.info("Szenario: Ein Schüler schlägt eine Vorhand. Du analysierst die Bewegungsphasen.")
    
    st.subheader("Frage 2.1: Hauptaktion vs. Hilfsaktion")
    q3 = st.radio(
        "Der Schüler trifft den Ball regelmäßig deutlich hinter dem Körper. Welchem Bereich ordnest du diesen Fehler primär zu?",
        options=[
            "A) Ausschwungphase (Hilfsaktion)",
            "B) Hauptaktion (ca. 30–40 cm vor dem Körper bis Treffpunkt) / Falscher Treffpunkt & Vorbereitung",
            "C) Nur der Fußstellung im Treffpunkt"
        ],
        key="m2_q1"
    )
    
    st.subheader("Frage 2.2: Biomechanische Kette")
    q4 = st.radio(
        "Welche Hilfsaktion leitet die Vorhand-Drive-Bewegung nach der Auftaktbewegung ein?",
        options=[
            "A) Sofortiger Ausschwung über die Schulter.",
            "B) Ausholphase mit Oberkörperrotation und Gewichtsverlagerung nach hinten/seitlich.",
            "C) Abstoppen der Beine ohne Hüftdrehung."
        ],
        key="m2_q2"
    )

# ---------------------------------------------------------
# MODUL 3: ORGANISATION & SPIELFORMEN
# ---------------------------------------------------------
with tab3:
    st.header("Modul 3: Organisation im Mid-Court / Kleinfeld")
    st.info("Szenario: Du leitest ein Gruppentraining mit 4 Anwärtern/Schülern auf einem Platz.")
    
    st.subheader("Frage 3.1: Wartezeiten & Intensität")
    q5 = st.radio(
        "Du führst eine Übungsform in Reihe durch (z. B. VH cross / RH longline). Wie vermeidest du lange Stehzeiten für die wartenden Schüler?",
        options=[
            "A) Die Schüler dürfen auf der Bank sitzen und zuschauen.",
            "B) Einbauen von Zusatzbeschäftigungen (z. B. Schattenbewegung, Prellen, Beinarbeit an der Linienecke).",
            "C) Die Gruppe auf 1 Schüler reduzieren."
        ],
        key="m3_q1"
    )

# ---------------------------------------------------------
# EVALUATION & AUSWERTUNG
# ---------------------------------------------------------
with tab_eval:
    st.header("📊 Deine Prüfungsauswertung")
    
    if st.button("Ergebnisse jetzt auswerten", type="primary"):
        score = 0
        total = 5
        
        # Prüfung der Antworten
        if st.session_state.get("m1_q1", "").startswith("B)"):
            score += 1
        if st.session_state.get("m1_q2", "").startswith("B)"):
            score += 1
        if st.session_state.get("m2_q1", "").startswith("B)"):
            score += 1
        if st.session_state.get("m2_q2", "").startswith("B)"):
            score += 1
        if st.session_state.get("m3_q1", "").startswith("B)"):
            score += 1
            
        st.session_state.score = score
        
        # Performance Anzeige
        percent = (score / total) * 100
        st.metric(label="Gesamtergebnis", value=f"{score} / {total} Punkte", delta=f"{percent:.0f}%")
        
        if percent >= 80:
            st.success("🎉 Bestanden! Du zeigst ein sehr gutes Verständnis der BTV-C-Trainer-Methodik.")
        else:
            st.warning("⚠️ Noch nicht ganz bestanden. Überarbeite noch einmal die Skripte zu Zuspielformen und Biomechanik.")
            
        st.subheader("Feedback & Detaillierte Auflösung:")
        st.markdown("""
        * **Zuwurf & Zuspiel:** Freier Blick zum Schüler, Greifen von 2 Bällen nach der VH sowie das Einspielen mit leicht geöffneter Schlägerfläche sichern Präzision und Rhythmus[cite: 1].
        * **Biomechanik:** Die Hauptaktion umfasst die unmittelbare Phase vor und im Treffpunkt (30–40 cm vor dem Körper)[cite: 5].
        * **Organisation:** Zusatzbeschäftigungen sind im Gruppenunterricht essenziell, um die Bewegungskopplung und Intensität hochzuhalten[cite: 3].
        """)
