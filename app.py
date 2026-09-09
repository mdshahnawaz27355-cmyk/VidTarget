import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Creator Niche & Topic Finder", page_icon="🎬")
st.title("🎬 Creator Niche & Daily Topic Finder")
st.write("2026-2027 ki top categories aur daily viral content ideas bilkul free me khojein.")

api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

niche = st.text_input("Apna Topic / Niche likhein (e.g., AI Tools, Indian History, Tech Reviews):")

if st.button("Analyze & Generate Ideas"):
    if not api_key:
        st.error("Kripya pehle left sidebar me apni Gemini API Key daalein!")
    elif not niche:
        st.warning("Kripya ek topic/niche enter karein.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-3.6-flash')
            
            with st.spinner("Analyzing market trends..."):
                prompt = f"""
                Act as an expert content strategist for social media creators in 2026-2027.
                Topic/Niche: '{niche}'
                
                Provide:
                1. 2026-2027 Growth & Monetization Potential (High Demand, Competition, Future scope)
                2. 5 Viral Daily Video Ideas with Catchy Hooks
                3. Best Content Source Ideas (Kaha se daily news/topics mileinge)
                
                Format the output nicely in Hindi/Hinglish with bullet points and clear headers.
                """
                response = model.generate_content(prompt)
                st.success("Analysis Complete!")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
