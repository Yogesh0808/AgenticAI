#It will have Multiple Agents not a Single Agents.To Get details of the Search, Stock.
from phi.agent import Agent
from phi.model.groq import Groq  #AI Model
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
load_dotenv()

web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the Web for the Information",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

## Financial Agent
financial_agent =Agent(
    name="Financial Agent",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,company_news=True, stock_fundamentals=True)],
    instructions=["Format your response and Use Tables to display the Data wherever possible"],
    show_tools_calls=True,
    markdown=True,
)

# multi agent application
multi_ai_agent = Agent(
    team=[web_search_agent, financial_agent],
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    instructions=["Use the web search agent to find information about the company and the financial agent to find information about the stock.",
                  "Use table to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream=True)






