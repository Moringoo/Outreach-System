import streamlit as st
import pandas as pd

# Konfiguration
st.set_page_config(page_title="Tavario Outreach Manager", layout="wide")

st.title("🚀 Tavario Outreach Manager")

# --- Bereich: CSV-Upload & Pitch-Generator ---
st.subheader("📁 Lead-Liste hochladen")
uploaded_file = st.file_uploader("Lade hier deine CSV-Datei von Apollo hoch:", type="csv")

def generate_tavario_pitch(name, company):
    link = "https://calendly.com/martina-ohrdorf/45min"
    return f"""Sehr geehrte Geschäftsführung von {company},

als Vertriebspartnerin von Tavario unterstütze ich Betriebe dabei, die unbesetzten Ausbildungsplätze durch motivierte internationale Fachkräfte zu besetzen.

Das Besondere an unserem Ansatz: Wir liefern nicht nur startklare Talente, sondern begleiten den gesamten Prozess. Von der bürokratischen Absicherung bis hin zur persönlichen Betreuung des Mitarbeiters. 

Hätten Sie in den nächsten Tagen 10 Minuten Zeit für ein kurzes Gespräch?

Hier finden Sie meinen Kalender: {link}

Beste Grüße,
Martina Ohrdorf
"""

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Vorschau deiner Leads:", df.head())
    
    if st.button("✨ Pitches für alle Leads generieren"):
        # Angenommen, die CSV hat Spalten wie 'First Name' und 'Company Name'
        # Wir passen das dynamisch an, falls die Spalten anders heißen
        for index, row in df.iterrows():
            name = row.get('First Name', 'Interessent')
            company = row.get('Company Name', 'Ihrem Unternehmen')
            
            with st.expander(f"Pitch für {company}"):
                st.text_area(f"Pitch für {company}", value=generate_tavario_pitch(name, company), height=200)

st.markdown("---")
