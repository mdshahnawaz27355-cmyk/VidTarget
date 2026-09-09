import streamlit as st
import requests
import json

st.set_page_config(page_title="Creator Niche & Topic Finder", page_icon="🎬")
st.title("🎬 Creator Niche & Daily Topic Finder")
st.write("2026-2027 ki top categories aur daily viral content ideas bilkul free me khojein.")

# Direct API Key embed
GEMINI_API_KEY = "AQ.Ab8RN6Kb-F0YKcn0Rm0BOaIY8QdBhNqKKS1VkIqsQDLZDxAsWw"

user_topic = st.text_input("Apna Topic / Niche likhein (e.g., AI Tools, Indian History, Tech Reviews):")

if st.button("Analyze & Generate Ideas"):
    if user_topic:
        with st.spinner("AI Trending Topics & Viral Ideas Dhoondh Raha Hai..."):
            prompt_text = f"""
            You are an expert Content Strategy AI for YouTube & Social Media Creators in 2026-2027.
            Topic/Niche: {user_topic}
            
            Provide a structured report in Hinglish:
            1. **Niche Potential**: 2026-2027 me is category ka kitna scope hai aur kyu?
            2. **Target Audience**: Is content ko kaun dekhega?
            3. **5 Viral Video Ideas**: Title + High Hook Rate Concept.
            4. **Monetization Ideas**: Sponsorships, Digital Products, AdSense.
            """
            
            # Direct REST API endpoint
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
            headers = {'Content-Type': 'application/json'}
            payload = {
                "contents": [{
                    "parts": [{"text": prompt_text}]
                }]
            }
            
            try:
                res = requests.post(url, headers=headers, json=payload)
                data = res.json()
                
                if res.status_code == 200:
                    output = data['candidates'][0]['content']['parts'][0]['text']
                    st.success("Aapki Content Strategy Taiyar Hai!")
                    st.markdown(output)
                else:
                    st.error(f"Error {res.status_code}: {data.get('error', {}).get('message', 'Unknown Error')}")
            except Exception as e:
                st.error(f"Request failed: {e}")
    else:
        st.warning("Kripya koi Topic ya Niche enter karein.")
