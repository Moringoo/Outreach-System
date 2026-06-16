import streamlit as st
import pandas as pd

# Konfiguration
st.set_page_config(page_title="LeadFinder Pro - Tavario", layout="wide")

st.title("🔍 LeadFinder Pro")

# Metrik-Karten
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Leads", "0")
col2.metric("New", "0")
col3.metric("Contacted", "0")
col4.metric("Qualified", "0")

st.markdown("---")

# Bereich: KI-Outreach-Assistent
st.subheader("🚀 KI-Outreach-Assistent")
st.info("Generiere hier deinen Tavario-Pitch für einen Lead. Kopiere ihn danach manuell zu LinkedIn.")

company_name = st.text_input("Name des Unternehmens:")

def generate_tavario_pitch(name):
    link = "https://calendly.com/martina-ohrdorf/45min"
    return f"""Sehr geehrte Geschäftsführung von {name},

als Vertriebspartnerin von Tavario unterstütze ich Betriebe dabei, die unbesetzten Ausbildungsplätze durch motivierte internationale Fachkräfte zu besetzen.

Das Besondere an unserem Ansatz: Wir liefern nicht nur startklare Talente, sondern begleiten den gesamten Prozess. Von der bürokratischen Absicherung (Visa & Anerkennung) bis hin zur persönlichen Betreuung des Mitarbeiters, auch wenn dieser bereits in Deutschland ist. So stellen wir sicher, dass die Integration langfristig erfolgreich gelingt und Sie als Betrieb nachhaltig entlastet werden.

Hätten Sie in den nächsten Tagen 10 Minuten Zeit für ein kurzes, unverbindliches Gespräch, um zu prüfen, wie wir Ihren Bedarf decken können?

Hier finden Sie meinen Kalender für eine kurze Terminbuchung: 
{link}

Beste Grüße,
Martina Ohrdorf
"""

if st.button("✨ Pitch für Tavario-Partnerschaft generieren"):
    if company_name:
        text = generate_tavario_pitch(company_name)
        st.text_area("Dein Pitch (zur Bearbeitung und zum Kopieren):", value=text, height=350)
    else:
        st.warning("Bitte gib einen Firmennamen ein.")

st.markdown("---")

# Bereich: Lead-Tabelle
st.subheader("Leads")
st.button("🔍 Search Apollo.io")
st.info("No leads found. Configure your search criteria and click Search to find new leads.")
