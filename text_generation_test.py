from transformers import pipeline

generator = pipeline('text-generation', model = 'EleutherAI/gpt-neo-2.7B')
prompt = "Write a motivational paragraph about penguins"
text_results = generator(prompt, max_length = 50, temperature=0.9)
print(text_results[0]['generated_text'])