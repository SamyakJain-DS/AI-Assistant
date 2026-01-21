import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools import get_weather, get_news, get_events
from langchain_core.tools import StructuredTool
from prompt import PLANNER_PROMPT

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
)

tools = [
    StructuredTool.from_function(get_weather),
    StructuredTool.from_function(get_news),
    StructuredTool.from_function(get_events),
]

agent_executor = create_agent(llm, tools)

def run_daily_briefing(city: str, topic: str):
    try:
        messages = PLANNER_PROMPT.format_messages(
            city=city,
            topic=topic
        )
        
        result = agent_executor.invoke(
            {"messages": messages}
        )
        
        output = result["messages"][-1].content[0]['text']
        
        if not output or not output.strip():
            return False, (
                "I checked today's weather, news, and events, but there was not enough "
                "verified information to generate a complete daily plan."
            )

        return True, output

    except Exception as e:
        print(f"Detailed Error: {e}") 
        return False, f"Error occurred: {e}"