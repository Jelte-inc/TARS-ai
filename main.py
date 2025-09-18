from commands.walking import walking_commands
from ai.ai_chat_model import ai

while True:
    user_input = input()

    walking_commands(user_input)

    ai(user_input)
