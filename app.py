import streamlit as st
import pandas as pd
from supabase import create_client

# Seiteneinstellungen
st.set_page_config(page_title="LeadFinder Pro", layout="wide")

st.title("🚀 LeadFinder Pro - Outreach System")

# Platzhalter für die Datenbank-Verbindung
# Hier werden später deine echten Supabase-Daten eingetragen
st.sidebar.header("⚙️ Suchkriterien")
company_name = st.sidebar.text_input("Firmenname", value="Tavario")

# Anzeige von Test-Daten
st.subheader("Gefundene Leads")
data = {
    "Name": ["Max Mustermann", "Erika Musterfrau"],
    "Unternehmen": ["Musterbau GmbH", "Pflegezentrum Nord"],
    "Status": ["Neu", "Kontaktiert"]
}
df = pd.DataFrame(data)

edited_df = st.data_editor(df, use_container_width=True)

if st.button("📋 Nachricht kopieren"):
    st.success("Nachricht für den gewählten Lead kopiert!")
