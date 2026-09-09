import streamlit as st
import requests

st.set_page_config(page_title="Creator Niche & Topic Finder", page_icon="🎬")
st.title("🎬 Creator Niche & Daily Topic Finder")
st.write("2026-2027 ki top categories aur daily viral content ideas bilkul free me khojein.")

# Direct Groq API Key Integration
GROQ_API_KEY = "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"

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
            
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": prompt_text}]
            }
            
            try:
                res = requests.post(url, headers=headers, json=payload)
                data = res.json()
                
                if res.status_code == 200:
                    output = data['choices'][0]['message']['content']
                    st.success("Aapki Content Strategy Taiyar Hai!")
                    st.markdown(output)
                else:
                    st.error(f"Error ({res.status_code}): {data.get('error', {}).get('message', 'API Request Failed')}")
            except Exception as e:
                st.error(f"Connection error: {e}")
    else:
        st.warning("Kripya koi Topic ya Niche enter karein.")
