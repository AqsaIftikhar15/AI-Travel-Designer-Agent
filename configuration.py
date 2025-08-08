from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel, AsyncOpenAI , set_tracing_disabled , RunConfig
import os

load_dotenv()
set_tracing_disabled(disabled = True) #while using 3rd party models like openrouter, we need to disable tracing

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

provider = AsyncOpenAI(
    api_key = openrouter_api_key,
    base_url="https://openrouter.ai/api/v1"
)

model_ai = OpenAIChatCompletionsModel(
    model = "openai/gpt-3.5-turbo",
    openai_client = provider,
)

config = RunConfig(
    model=model_ai,
)
