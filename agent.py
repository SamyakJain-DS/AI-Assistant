import os
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from tools import get_weather, get_news, get_events
from langchain_core.tools import StructuredTool
from prompt import PLANNER_PROMPT

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found in environment variables")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    api_key=os.getenv("GROQ_API_KEY")
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

        output = None
        if isinstance(result.get("messages", [])[-1].content, list):
            output = result["messages"][-1].content[0].get('text', '')
        else:
            output = result["messages"][-1].content

        
        if not output or not output.strip():
            return False, (
                "I checked today's weather, news, and events, but there was not enough "
                "verified information to generate a complete daily plan."
            )

        return True, output

    except Exception as e:
        print(f"Detailed Error: {e}") 
        return False, f"Error occurred: {e}"
