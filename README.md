# 🧠 AI Daily Briefing Agent

An **AI-powered daily planning assistant** that reasons over real-time data sources to generate a **personalized, actionable day plan** using **Google Gemini**, structured tools, and an agent-based architecture. The assistant fetches **live weather**, **recent news**, and **confirmed local events**, then synthesizes them into a concrete, verifiable daily schedule.

[Link for the live website!](https://ai-assistant-samyak-jain.streamlit.app/)

---

## ✨ Features

* 🌤️ **Real-time weather analysis** with actionable recommendations
* 📰 **Top 3 recent news headlines** for a user-selected topic
* 🗓️ **Event-centric daily planning** using verified local events
* 🤖 **Agent-based reasoning** with dynamic tool selection
* 🧠 **Strict prompt constraints** to avoid vague or fabricated suggestions
* ⚡ **Streamlit-based interactive UI**
* ☁️ **Deployed on Streamlit Cloud**

---

## 🧠 How It Works

1. The user provides:

   * A **city** (for weather and events)
   * A **topic of interest** (for news)
2. A **Gemini-powered agent** receives a highly constrained system prompt that enforces:

   * Use of real, current, and verifiable data
   * Explicit rejection of vague or generic recommendations
3. The agent dynamically decides when to call:

   * Weather API tool
   * News API tool
   * Events search tool
4. The agent synthesizes all retrieved information into a **structured daily plan**, divided into:

   * 🌤️ Weather & recommendations
   * 📰 Top 3 news headlines
   * 🗓️ Morning, Afternoon, and Evening schedule

---

## 🗂️ Project Structure

```text
AI_Daily_Briefing/
├── app.py          # Streamlit UI
├── agent.py        # Agent executor and orchestration logic
├── prompt.py       # System prompt with strict planning constraints
├── tools.py        # External tools (weather, news, events)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧩 Tech Stack

### 🤖 LLM & Agent Framework

* **Google Gemini 2.5 Flash**

  * Reasoning and planning
  * Tool selection and synthesis
* **LangChain Agents**

  * Structured tool invocation
  * Multi-step reasoning loop

---

### 🛠️ Tools

* **Weather Tool**

  * OpenWeatherMap API
  * Current temperature, conditions, humidity, wind, sunrise/sunset

* **News Tool**

  * NewsAPI
  * Fetches the 3 most recent and relevant headlines

* **Events Tool**

  * SerpAPI (Google Events engine)
  * Retrieves confirmed local events scheduled for today

---

### 🖥️ Frontend

* **Streamlit**
* Clean, minimal UI
* User-controlled input with real-time feedback

---

Website Demo:
<img width="1880" height="983" alt="Assistant Demo 1" src="https://github.com/user-attachments/assets/c824dc1c-5276-42d7-9188-d0d7ddeb942c" />
> The user interface

<img width="1880" height="983" alt="Assistant Demo 2" src="https://github.com/user-attachments/assets/2a5c11b1-71f8-4f0f-9df2-4613a4b34454" />
>Sample model output

## 🔐 Environment Variables

Create a `.env` file locally or add the following to **Streamlit Cloud → Secrets**:

```env
GOOGLE_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
NEWS_API_KEY=your_newsapi_key
SERPAPI_KEY=your_serpapi_key
```

---

## ⚠️ Design Principles & Constraints

> **This assistant prioritizes correctness over creativity.**

* ❌ No fabricated venues or events
* ❌ No vague phrases like "explore the area" or "visit a local cafe"
* ✅ Only real, named places when verifiable
* ✅ Honest gaps when data is unavailable
* ✅ Plans strictly reflect **today's** conditions

---

## ⚠️ Notes & Limitations

* Runs on **Gemini Free Tier**, which is rate-limited
* Event availability depends on third-party data sources
* If insufficient verified data is available, the assistant will explicitly state so
* Designed for **daily planning**, not long-term scheduling

---

## 👤 Author

**Samyak Jain**
📊 Data Science | 🤖 Generative AI | 🧠 Agentic Systems <br>
GitHub: [https://github.com/SamyakJain-DS](https://github.com/SamyakJain-DS)

---
