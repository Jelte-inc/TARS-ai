import ollama

message_content = ""

while message_content != "bye bye": 
  
  message_content = input()
 
  message = {'role': 'user', 'content': message_content}
  try:
    for part in ollama.chat(model='gemma3:4b', messages=[message], stream=True):
      print(part['message']['content'], end='', flush=True)
  except Exception as e:
    print("something went wrong")