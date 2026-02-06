import streamlit as st
import google.generativeai as genai

st.title("🛠️ Model Bulucu")

# API Key Kontrolü
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("API Key yok.")
    st.stop()

if st.button("Hangi Modellerim Açık?"):
    try:
        st.write("Google'ın senin için izin verdiği modeller:")
        found = False
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                st.code(m.name) # Ekrana model ismini yazar
                found = True
        
        if not found:
            st.error("Hiçbir model bulunamadı! API Key'in 'Generative Language' yetkisi kapalı olabilir.")
            
    except Exception as e:
        st.error(f"Hata detayı: {e}")
