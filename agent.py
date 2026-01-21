import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from tools import get_weather, get_news, get_events
from langchain.tools import StructuredTool
from prompt import PLANNER_PROMPT

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.5,
)

tools = [
    StructuredTool.from_function(get_weather),
    StructuredTool.from_function(get_news),
    StructuredTool.from_function(get_events),
]

agent = create_tool_calling_agent(llm, tools, PLANNER_PROMPT)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

def run_daily_briefing(city: str, topic: str):
    try:
        result = agent_executor.invoke(
            {"city": city, "topic": topic}
        )
        
        output = result.get("output")

        if not output or not output.strip():
            return False, (
                "I checked today's weather, news, and events, but there was not enough "
                "verified information to generate a complete daily plan."
            )

        return True, output

    except Exception as e:
        print(f"Detailed Error: {e}") 
        return False, f"Error occurred: {e}"