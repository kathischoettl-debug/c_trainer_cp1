import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_court(trainer_pos, queue_pos):
    # Figure mit festem Seitenverhältnis erstellen
    fig, ax = plt.subplots(figsize=(8, 10))
    
    # 1. Sandplatz-Hintergrund (BTV-Rot / Ziegelrot) & Auslaufbereich (Grün)
    ax.set_facecolor("#2E8B57") # Grüner Umfeld-Bereich
    court_bg = patches.Rectangle((0, 0), 10.97, 23.77, linewidth=0, edgecolor='none', facecolor='#D2691E') # Sandplatz
    ax.add_patch(court_bg)
    
    # 2. Spielfeldlinien (Weiß, 2px)
    # Spielfeld-Außenlinien (Einzel: 8.23m x 23.77m, Zentriert auf 10.97m Breite)
    margin = (10.97 - 8.23) / 2 # 1.37m Doppelkorridor
    
    # Außenfeld (Doppel)
    ax.plot([0, 10.97, 10.97, 0, 0], [0, 0, 23.77, 23.77, 0], color="white", lw=2)
    # Einzel-Seitenlinien
    ax.plot([margin, margin], [0, 23.77], color="white", lw=1.5)
    ax.plot([10.97 - margin, 10.97 - margin], [0, 23.77], color="white", lw=1.5)
    
    # Netz (Mitte bei 11.885m)
    net_y = 23.77 / 2
    ax.plot([-0.5, 11.47], [net_y, net_y], color="black", lw=4, zorder=3, label="Netz")
    ax.plot([-0.5, 11.47], [net_y, net_y], color="white", lw=1.5, ls="--", zorder=4)
    
    # T-Linien (6.40m vom Netz)
    t_bottom = net_y - 6.40
    t_top = net_y + 6.40
    ax.plot([margin, 10.97 - margin], [t_bottom, t_bottom], color="white", lw=1.5)
    ax.plot([margin, 10.97 - margin], [t_top, t_top], color="white", lw=1.5)
    # Mittellinie
    ax.plot([10.97/2, 10.97/2], [t_bottom, t_top], color="white", lw=1.5)
    
    # 3. Positionen der Personen berechnen
    # Trainer Position
    if "Netz" in trainer_pos:
        tx, ty = 10.97/2, net_y - 1.5
    elif "T-Linie" in trainer_pos:
        tx, ty = 10.97/2, t_bottom
    else: # Grundlinie
        tx, ty = 10.97/2, 1.0

    # Schüler Position
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
    ax.set_aspect('equal') # Verhindert Verzerrung
    
    # Beschriftung/Legende
    ax.legend(loc="upper right", framealpha=0.9)
    ax.axis("off") # Sicherstellen, dass das Feld trotzdem gezeichnet wird
    
    return fig

# --- STREAMLIT AUFRUF ---
st.title("1. Visuelles Platz-Setup & Gruppenorganisation")

col1, col2 = st.columns([1, 1])

with col1:
    trainer_pos = st.selectbox("Position des Trainers (Korb):", ["Am Netz (Mitte)", "Auf der T-Linie", "An der Grundlinie"], index=0)
    queue_pos = st.selectbox("Wartezone der Schüler:", ["Seitlich an der Netzkante mit Zusatzaufgabe", "Direkt hinter dem Schläger", "Auf der Bank"], index=0)

with col2:
    fig = draw_court(trainer_pos, queue_pos)
    st.pyplot(fig, use_container_width=True)
