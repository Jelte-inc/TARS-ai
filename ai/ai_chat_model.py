import ollama

def ai(user_input:str):
  message = {'role': 'user', 'content': user_input}
  if user_input == "bye bye":
    return
  try:
    for part in ollama.chat(model='gemma3:4b', messages=[message], stream=True):
      print(part['message']['content'], end='', flush=True)
  except Exception as e:
    print("something went wrong")
  print()