from commands.walking import walking_commands
from ai.ai_chat_model import ai
from speech.listener import speech_listener

while True:
    user_input = input()

    walking_commands(user_input)

    ai(user_input)
