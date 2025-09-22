from commands.walking import walking_commands
from ai.ai_chat_model import ai
from speech.listener import speech_listener

while True:
    user_input = speech_listener()

    walking_data =  walking_commands(user_input)

    if walking_data is not None:
        if walking_data[0] is None:
            print(type(walking_data))
            print(f"how many {walking_data} do you want me to go?")
            walking_direction_amount = speech_listener()
            if walking_direction_amount is not int:
                print("idiot")
                continue
            print(walking_direction_amount)

    ai(user_input)
