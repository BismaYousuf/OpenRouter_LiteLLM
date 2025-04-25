import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel   #add krny ka tareeqa"  uv add "openai-agents[litellm]"

load_dotenv()

set_tracing_disabled(disabled=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY is not set")

agent = Agent(
    model =LitellmModel(model="gemini/gemini-2.0-flash", api_key=GEMINI_API_KEY,),
    name = "Bisma_Agent",
    instructions="You are a helpful assistant",
)
#------------------------------------------------------------------
res = Runner.run_sync(agent, "I am Bisma, Who are You?")

print(res.final_output)