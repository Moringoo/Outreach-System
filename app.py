import streamlit as st
import requests
import pandas as pd

# Konfiguration
st.set_page_config(page_title="LeadFinder Pro - Tavario", layout="wide")

st.title("🔍 LeadFinder Pro")

# --- Bereich: KI-Outreach-Assistent ---
st.subheader("🚀 KI-Outreach-Assistent")

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
        st.text_area("Dein Pitch:", value=generate_tavario_pitch(company_name), height=350)
    else:
        st.warning("Bitte gib einen Firmennamen ein.")

st.markdown("---")

# --- Bereich: Apollo.io Lead-Suche ---
st.subheader("🔍 Apollo.io Lead-Suche")

def search_apollo():
    try:
        api_key = st.secrets["APOLLO_API_KEY"]
        url = "https://api.apollo.io/v1/mixed_people/search"
        headers = {"Content-Type": "application/json"}
        payload = {
            "api_key": api_key,
            "person_titles": ["Geschäftsführer"],
            "per_page": 5
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get("people", [])
        else:
            st.error(f"Fehler bei Apollo: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Fehler: {e}")
        return None

if st.button("Leads von Apollo laden"):
    with st.spinner("Suche läuft..."):
        leads = search_apollo()
        if leads:
            df = pd.DataFrame(leads)
            st.write("Gefundene Leads:")
            st.dataframe(df)
        else:
            st.warning("Keine Leads gefunden oder Fehler bei der Verbindung.")
