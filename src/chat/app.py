from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
import os
import asyncio

load_dotenv()
set_tracing_disabled(True)

provider = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client=provider,
)

async def myAgent(user_input):
    Agent1 = Agent(
        name="MyAgent",
        instructions="An agent that processes input text and returns a response.",
        model=model,
    )

    response = await Runner.run(
        Agent1,
        user_input)
    return response.final_output