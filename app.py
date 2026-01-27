import streamlit as st
from agent import run_daily_briefing

st.set_page_config(page_title="AI Daily Briefing", layout="centered")

st.title("🧠 AI Daily Briefing Agent")
st.caption("A GenAI agent that reasons, selects tools, and synthesizes insights.")

city = st.text_input("Enter your city")
topic = st.text_input("Enter the topic of interest for the day!")

if st.button("Generate Briefing"):
    if city and topic:
        with st.spinner("Thinking..."):
            success, output = run_daily_briefing(city, topic)
        if success:
            st.markdown(output)
            if not output or not output.strip():
                st.warning(
                    "I checked today's information for the provided inputs, "
                    "but could not generate a complete and verified daily plan. "
                    "Please try a different city or topic."
                    )
        else:
            st.error("Failed to generate briefing.")
    else:
        st.error("Please enter a city name and a topic.")
