import chainlit as cl

# chat life cycle
# 1. on chat start
# 2. on message
# 3. on stop
# 4. on chat end
# 5. on chat resume


@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")

@cl.on_message
def on_message(msg: cl.Message):
    print("The user sent: ", msg.content)

@cl.on_stop
def on_stop():
    print("The user wants to stop the task!")

@cl.on_chat_end
def on_chat_end():
    print("The user disconnected!")

from chainlit.types import ThreadDict

@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    print("The user resumed a previous chat session!")

