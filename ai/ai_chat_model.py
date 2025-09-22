import ollama


# Functie om modeloutput te verwerken
def execute_model_output(model_output: str) -> str:
    if model_output.strip() == "call_say_hi()":    
      return "hoi"
    else:
        return model_output

# Hoofdloop
message_content = ""
while message_content.lower() != "bye bye":
    message_content = input("You: ")
    message = {'role': 'user', 'content': message_content}
    try:
        full_response = ""
        for part in ollama.chat(model='tars', messages=[message], stream=True):
            full_response += part['message']['content']
            print(part['message']['content'], end='', flush=True)
        print('')  # Nieuwe regel na streaming
        # Verwerk de output voor functieaanroep
        result = execute_model_output(full_response)
        if result != full_response:
            print(f"Function result: {result}")
    except Exception as e:
        print("Something went wrong:", e)
    print('')