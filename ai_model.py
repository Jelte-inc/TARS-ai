import ollama

message = {'role': 'user', 'content': 'Why is the sky blue?'}
for part in ollama.chat(model='gemma2:latest', messages=[message], stream=True):
  print(part['message']['content'], end='', flush=True)