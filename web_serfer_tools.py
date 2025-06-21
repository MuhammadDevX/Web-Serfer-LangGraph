from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from dotenv import load_dotenv
from langchain.agents import Tool
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_experimental.tools import PythonREPLTool

load_dotenv(override=True)

async def playwright_tools():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
    return toolkit.get_tools(), browser, playwright


def get_file_tools():
    toolkit = FileManagementToolkit(root_dir="sandbox")
    return toolkit.get_tools()


async def other_tools():
    # push_tool = Tool(name="send_push_notification", func=push, description="Use this tool when you want to send a push notification")
    file_tools = get_file_tools()

    python_repl = PythonREPLTool()
    
    return file_tools + [ python_repl]

# How to create tools 
# You would first write the simple function 
# Then you would call the Tool Function with the name, description and func 