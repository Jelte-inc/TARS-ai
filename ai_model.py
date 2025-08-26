from llama_cpp import Llama

# Laad het gequantiseerde Mistral 7B model
model_path = "./mixtral-8x7b-instruct-v0.1.Q4_0.gguf"  # Pas dit aan naar de locatie van je model
llm = Llama(model_path=model_path, n_ctx=512, n_threads=4, n_gpu_layers=0)  # n_gpu_layers=0 omdat Raspberry Pi geen GPU-ondersteuning heeft

# Definieer de prompt
prompt = "Schrijf een korte paragraaf over waarom de Raspberry Pi geschikt is voor AI-projecten."

# Genereer tekst
output = llm(
    prompt,
    max_tokens=150,  # Maximaal aantal tokens in de uitvoer
    temperature=0.7,  # Controleert de creativiteit (0.0 = deterministisch, 1.0 = zeer creatief)
    top_p=0.9,  # Nucleus sampling parameter
    echo=False  # Niet de prompt herhalen in de uitvoer
)

# Print de gegenereerde tekst
print(output["choices"][0]["text"])