import os
import requests
import streamlit as st

st.set_page_config(
    page_title="Creator Niche & Topic Finder",
    page_icon="🎬",
    layout="centered",
)

st.title("🎬 Creator Niche & Daily Topic Finder")
st.write("2026–2027 ke liye YouTube & Social Media content ideas generate karein.")

# API key must be stored in Streamlit Secrets:
# GROQ_API_KEY = "your_gsk_key_here"
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

topic = st.text_input(
    "Apna Topic / Niche likhein",
    placeholder="e.g. AI Tools, Indian History, Tech Reviews",
)

if st.button("🚀 Analyze & Generate Ideas", type="primary"):
    if not topic.strip():
        st.warning("Kripya koi Topic ya Niche enter karein.")
        st.stop()

    if not GROQ_API_KEY:
        st.error(
            "GROQ_API_KEY nahi mili. Streamlit → Manage app → Settings → Secrets "
            "me GROQ_API_KEY save karein."
        )
        st.stop()

    prompt = f"""
You are an expert Content Strategy AI for YouTube and Social Media creators.

Topic/Niche: {topic}

Create a practical report in simple Hinglish:

1. Niche Potential — 2026–2027 me scope aur reasons
2. Target Audience
3. 5 Viral Video Ideas — each with Title + Hook + basic angle
4. 5 Shorts/Reels Ideas
5. Monetization Ideas — AdSense, sponsorships, affiliate marketing, digital products
6. A simple 7-day content plan

Do not invent current news or statistics. If a claim needs current verification,
clearly say that it should be checked before publishing.
"""

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful content-strategy assistant.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
    }

    try:
        with st.spinner("AI ideas generate kar raha hai..."):
            response = requests.post(
                url, headers=headers, json=payload, timeout=60
            )

        try:
            data = response.json()
        except ValueError:
            data = {}

        if response.ok:
            choices = data.get("choices", [])
            if choices:
                output = choices[0]["message"]["content"]
                st.success("✅ Aapki Content Strategy Taiyar Hai!")
                st.markdown(output)
            else:
                st.error("API ne usable response nahi diya.")
        else:
            message = data.get("error", {}).get("message", "API request failed.")
            st.error(f"API Error ({response.status_code}): {message}")

    except requests.Timeout:
        st.error("Request timeout ho gaya. Dobara try karein.")
    except requests.RequestException as exc:
        st.error(f"Connection error: {exc}")

st.caption("Tip: API key ko app.py me kabhi hard-code na karein.")

