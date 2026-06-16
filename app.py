def search_apollo():
    try:
        api_key = st.secrets["APOLLO_API_KEY"]
        url = "https://api.apollo.io/v1/mixed_people/search"
        headers = {"Content-Type": "application/json"}
        
        # Diese Struktur entspricht den Anforderungen für Apollo v1/mixed_people/search
        payload = {
            "api_key": api_key,
            "q_organization_num_employees_ranges": ["11-50"],
            "person_titles": ["Geschäftsführer", "Inhaber"],
            "page": 1,
            "per_page": 10
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return response.json().get("people", [])
        else:
            # Hier sehen wir nun die exakte Fehlermeldung von Apollo
            st.error(f"Apollo API Fehler ({response.status_code}): {response.text}")
            return None
    except Exception as e:
        st.error(f"Fehler: {e}")
        return None
            
