from configuration import config
from agent_needed.dest_agent import DestinationAgent
from chainlit import on_message , Message
from agents import Runner
import os
import chainlit as cl

@cl.on_chat_start
async def handle_start():
    cl.user_session.set("history", [])

@cl.on_message
async def handle_message(message : cl.Message):
    history = cl.user_session.get("history")
    history.append({
        "role": "user",
        "content": message.content
    }) 
    result = await Runner.run(
        starting_agent=DestinationAgent,
        input=history,
        run_config=config,
        max_turns=150
    )
    await cl.Message(content=result.final_output).send()

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8000))
#     cl.run(port=port, host="0.0.0.0")