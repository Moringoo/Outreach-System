import streamlit as st
import pandas as pd

# Konfiguration
st.set_page_config(page_title="LeadFinder Pro", layout="wide")

# Styling: Layout an das Bild anpassen
st.title("🔍 LeadFinder Pro")

# Metrik-Karten (Reihe 1)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Leads", "0")
with col2:
    st.metric("New", "0")
with col3:
    st.metric("Contacted", "0")
with col4:
    st.metric("Qualified", "0")

st.markdown("---")

# Leads Bereich
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.subheader("Leads")
with header_col2:
    if st.button("🔍 Search Apollo.io", type="primary"):
        st.warning("Suche wird gestartet...")

# Platzhalter-Bereich wenn keine Daten da sind
st.info("No leads found. Configure your search criteria and click Search to find new leads.")

# Hier würde später die Tabelle erscheinen
# df = pd.DataFrame(...)
# st.dataframe(df, use_container_width=True)
