import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Creator Niche & Topic Finder", page_icon="🎬")
st.title("🎬 Creator Niche & Daily Topic Finder")
st.write("2026-2027 ki top categories aur daily viral content ideas bilkul free me khojein.")

# Direct API Key embed (AQ.Ab8RN6L1qnCp6l3sAoIsvvj4k0o-TSe72gf1nLen7lSTvkoH0Q)
GEMINI_API_KEY = "YAHAN_APNI_GEMINI_API_KEY_PASTE_KAREIN"

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    
    # Model
    model = genai.GenerativeModel('gemini-3.6-flash')

    user_topic = st.text_input("Apna Topic / Niche likhein (e.g., AI Tools, Indian History, Tech Reviews):")

    if st.button("Analyze & Generate Ideas"):
        if user_topic:
            with st.spinner("AI Trending Topics & Viral Ideas Dhoondh Raha Hai..."):
                prompt = f"""
                You are an expert Content Strategy AI for YouTube & Social Media Creators in 2026-2027.
                Topic/Niche: {user_topic}
                
                Provide a structured report in Hinglish:
                1. **Niche Potential**: 2026-2027 me is category ka kitna scope hai aur kyu?
                2. **Target Audience**: Is content ko kaun dekhega?
                3. **5 Viral Video Ideas**: Title + High Hook Rate Concept.
                4. **Monetization Ideas**: Sponsorships, Digital Products, AdSense.
                """
                
                try:
                    response = model.generate_content(prompt)
                    st.success("Aapki Content Strategy Taiyar Hai!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Kripya koi Topic ya Niche enter karein.")
