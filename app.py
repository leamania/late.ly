import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Geç Kaldım!", page_icon="🏃")

# Başlık ve Açıklama
st.title("🏃 Geç Kaldım Generator")
st.write("Patrona yakalanmadan önce buradan bir yalan seç!")

# API Key Ayarı (Bunu sonra gizleyeceğiz)
# Buraya kendi API Key'ini yapıştırma, aşağıda anlatacağım "Secrets" kısmından çekeceğiz.
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Kullanıcı Girdileri
col1, col2 = st.columns(2)
with col1:
    sure = st.selectbox("Ne kadar geciktin?", ["15 Dakika", "30 Dakika", "1 Saat", "Yarım Gün", "Bütün Gün Yokum"])
    tema = st.selectbox("Bahane ne olsun?", ["Trafik/Yol", "Araba Arızası", "Hastalık", "Uyuya Kaldım (Gizle)", "Ev Tesisatı/Usta", "Ailevi Durum"])

with col2:
    patron = st.selectbox("Patronun Tipi Nasıl?", ["Sert/Takıntılı (Risk yok)", "Kurumsal/Beyaz Yaka (Resmi)", "Anlayışlı/Kanka (Samimi)", "Kaotik/Panik (Acil Durum)"])

# Buton
if st.button("Bahaneyi Üret"):
    model = genai.GenerativeModel('gemini-2.0-flash') # Modeli seçtik
    
    # Senin Prompt Yapın
    prompt = f"""
    Sen 'Geç Kaldım' uygulamasısın.
    Girdi: {sure} gecikme, {tema} konulu, {patron} tipinde patrona uygun Türkçe bahane.
    Görev: Türkiye şartlarına uygun (trafik, metrobüs vb.) 2 seçenek üret.
    Seçenek A (Garanti):
    Seçenek B (Yaratıcı):
    Sadece bu iki seçeneği çıktı olarak ver.
    """
    
    with st.spinner('Yalanlar pişiriliyor...'):
        response = model.generate_content(prompt)
        st.write(response.text)
