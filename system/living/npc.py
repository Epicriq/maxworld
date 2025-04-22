from gpt4all import GPT4All
from transformers import AutoModelForCausalLM, AutoTokenizer

# Выбор модели при инициализации (скачивается автоматически)
model_mini = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

model= model_mini

def get_ai_response(ai, reqest):
    if ai == "gpt":
        print("Дайка подумать...")
        return model.generate(reqest, max_tokens=30)
    elif ai == "deepseek":        
        model_name = "deepseek-ai/deepseek-coder-1.3b"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"  # Автовыбор CPU/GPU
        )

        def generate_npc_response(prompt):
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
            outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.7)
            return tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Диалог с NPC
        response = generate_npc_response("""Ты страж древнего храма. Ответь: "Кто идёт?" (Грозно, 1 предложение):""")
        print(response)